#!/usr/bin/env python


import os
import queue
import argparse
import multiprocessing
import threading
import qreport
import webbrowser
import concurrent.futures
import tempfile
import Feed
import futur

def handle_cmd():
    parser=argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int,default=multiprocessing.cpu_count()*4, help="specify the concurrency for "
                        "debug and timing [default: %(default)d]")
    parser.add_argument("-l", "--limit", type=int, default=0,help="the max items per feed [default: unlimited]")
    args=parser.parse_args()
    return args.limit, args.concurrency

def create_threads(limit, jobs, results, concurrency):
    for _ in range(concurrency):
        thread = threading.Thread(target=worker, args=(limit, jobs, results))
        thread.daemon = True
        thread.start()

def worker(limit, jobs, results):
    while 1:
        try:
            feed = jobs.get()
            ok, res = Feed.read(feed, limit)
            if not ok: qreport.report(results, True)
            elif res is not None:
                qreport.report("read {}".format(res[0][4:-6]))
                results.put(res)
        finally:
            jobs.task_done()

def add_jobs(filename, jobs):
    for todo, feed in enumerate(Feed.iter(filename), start=1):
        jobs.put(feed)
    return todo

def process(todo, jobs, results, concurrency):
    canceled = False
    try:
        jobs.join()
    except KeyboardInterrupt:
        qreport.report("canceling...")
        canceled = True
    if canceled:
        done = results.qsize()
    else:
        done, filename = output(results)
        qreport.report("read {}/{} feeds using {} threads{}".format(done, todo, concurrency,"[canceled]" if canceled else ""))
    print()
    if not canceled:
        webbrowser.open(filename)

def output(results):
    done = 0
    filename = os.path.join(tempfile.gettempdir(), "whatsnew.html")
    with open(filename, "wt", encoding="utf-8") as file:
        file.write("<!doctype html>\n")
        file.write("<html><head><title>What's new</title></head>\n")
        file.write("<body><h1>What's new</h1>\n")
        while not results.empty():
            result = results.get_nowait()
            done += 1
            for i in result:
                file.write(i)
        file.write("</body></html>\n")
    return done, filename

def main():
    limit, concurrency = handle_cmd()
    qreport.report("starting...")
    filename = os.path.join(os.path.dirname(__file__), "whatsnew.dat")
    jobs = queue.Queue()
    results = queue.Queue()
    create_threads = (limit, jobs, results, concurrency)
    todo = add_jobs(filename, jobs)
    process(todo, jobs, results, concurrency)


def maintwo():
    limit, concurrency = handle_cmd()
    qreport.report("starting...")
    filename = os.path.join(os.path.dirname(__file__), "whatsnew.dat")
    futures = set()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        for feed in Feed.iter(filename):
            future = executor.submit(Feed.read, feed, limit)
            futures.add(future)
        done, filename, canceled = futur.process(futures)
        if canceled:
            executor.shutdown()
    qreport.report("read {}/{} feeds using {} threads{}".format(done, len(futures), concurrency,"[canceled]" if canceled else ""))
    print()
    if not canceled: webbrowser.open(filename)


if __name__=='__main__':
    maintwo()