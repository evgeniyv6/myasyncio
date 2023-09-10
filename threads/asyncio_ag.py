import asyncio

async def coro():
    print('in coro sleep')
    print('One')
    await asyncio.sleep(5)
    print('two')
    return '<<res>>'

async def main():
    await asyncio.gather(coro(), coro())

if __name__=='__main__':
    el=asyncio.get_event_loop()
    try:
        print('start coro')
        mycoro = main()
        print('enter event loop')
        res = el.run_until_complete(mycoro)
        print(f'res is {res}')
    finally:
        print('close ev loop')
        el.close()