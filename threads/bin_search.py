#!/usr/bin/env python

# def bin_sorted_search(l,e):
#     l = sorted(l)
#     low, high = 0, len(l)-1
#     while low <= high:
#         mid = (low+high)//2
#         if e < l[mid]: high=mid-1
#         elif e > l[mid]: low=mid+1
#         else:
#             return True
#     return False
#
# print(bin_sorted_search([-1,6],6))
#
# def another_bin(l: list,e: int) -> bool:
#     l = sorted(l)
#     lidx, hidx = 0, len(l)-1
#     while lidx <= hidx:
#         midx = (lidx + hidx) // 2
#         if e < l[midx]: hidx = midx - 1
#         elif e > l[lidx]: lidx = midx + 1
#         else:
#             return True
#     return False
#
# print(another_bin([1,2,3,4],4))
#
#
# def buble_sort(l):
#     n = 1
#     while n <= len(l):
#         for i in range(len(l)-n-1):
#             if l[i] > l[i+1]:
#                 l[i], l[i+1] = l[i+1], l[i]
#         n+=1
#     return l
#
# print(buble_sort([2,3,6,5,4,5,6,9]))
#
#
# '''
# 1 2 3
# 4 5 6
# 7 8 9
# '''
#
# def sum_diags(l):
#     n = len(l)
#     sum=0
#     for i,_ in enumerate(l):
#         sum += l[i][i] + l[i][n-1 -i]
#     if n %2 != 0:
#         sum -= l[n//2][n//2]
#     return sum
#
# print(sum_diags([[1,2,3], [4,5,6], [7,8,9]]))
#
#
# def sort_ins(l):
#     n = len(l)
#     for i in range(1,n):
#         j=i
#         while j>0 and l[j] < l[j-1]:
#             l[j], l[j-1]=l[j-1],l[j]
#             j-=1
#
# def buble_new(l):
#     n=1
#     while n < len(l):
#         for i in range(len(l)-1-n):
#             if l[i]>l[i+1]:
#                 l[i], l[i+1]=l[i+1],l[i]
#         n+=1
#     return l
#
# nl=['192.168.1.2','192.168.1.3', '10.15.15.10']
# print(sort_ins(nl))
# print(nl)
# print(buble_new(['had','and', 'but', 'was']))
#
# def _merge(l,s,m,e,tmp):
#     n=e-s
#     i=s
#     j=m
#     for k in range(n):
#         if i==m:        tmp[k] = l[j]; j+=1
#         elif j==e:      tmp[k] = l[i]; i+=1
#         elif l[j]<l[i]: tmp[k] = l[j]; j+=1
#         else:           tmp[k] = l[i]; i+=1
#     l[s:e]=tmp[:n]
#
# def _sort(l,s,e,tmp):
#     n=e-s
#     if n<=1: return
#     m=(s+e)//2
#     _sort(l,s,m,tmp)
#     _sort(l,m,e,tmp)
#     _merge(l,s,m,e,tmp)
#
# def union_sort(l):
#     n=len(l)
#     tmp=[None]*n
#     _sort(l,0,n,tmp)
#
# union_l=[2,3,2,5,6,7,8,9,1,2,1,2,1,2]
# union_w=['had','and', 'but', 'was']
# print('union sort')
# union_sort(union_w)
# print(union_w)
#
# def another_buble(l):
#     n = len(l)
#     for i in range(1,n):
#         j=i
#         while j>0 and l[j]<l[j-1]:
#             l[j],l[j-1] = l[j-1], l[j]
#             j-=1
#     return l
#
# # sprint(another_buble([2,3,1,2,3,4,8,7,8,6,4,7,8,9]))
# import random
# def slow_sort_q(l):
#     n=len(l)
#     if n <= 1: return l
#     else:
#         p = random.choice(l)
#         return slow_sort_q([x for x in l if x <p]) + [p]*l.count(p) + slow_sort_q([x for x in l if x >p])
#     return l
#
# print(slow_sort_q([2,3,1,2,3,4,8,7,8,6,4,7,8,9]))
#
# import threading
#
# def veryq(l,b,e):
#     n = len(l)
#     if b>=e: return
#     i,j,p=b,e, l[random.randint(b,e)]
#     while i<=j:
#         while l[i]<p: i+=1
#         while l[j]>p: j-=1
#         if i<=j:
#             l[i], l[j] = l[j], l[i]
#             i, j=i+1, j-1
#     veryq(l,b,j)
#     veryq(l,i,e)
#
# ll=[9,3,2,3,3,2]
# #veryq(ll, 0, len(ll)-1)
# #print(ll)
#
# def o_b(l):
#     n = len(l)
#     count=1
#     while count <= n:
#         for i in range(n-count):
#             if l[i]>l[i+1]:
#                 l[i], l[i+1]=l[i+1], l[i]
#         count+=1
#     return l
# print('lllllllll')
# print(o_b(ll))
#
# def book_buble(l):
#     n = len(l)
#     for i in range(n):
#         j=i
#         while j>0 and l[j]<l[j-1]:
#             l[j], l[j-1]=l[j-1], l[j]
#             j-=1
#     return l
# print(book_buble([7,8,6,4,5,6,7]))
#
# print(*range(1,3), sep='')
#
# print('substr')
def substr(s,ss):
    count = 0
    if s==ss:
        count
    else:
        for i in range(len(s)):
            print(''.join(s[:-i]))
            if ''.join(s[:-i]) == ss:
                count+=1
    return count
# print(substr('12jlka445kljakldfjlaksjdfdka3942', '3942'))
'''
12jlka445kljakldfjlaksjdfdka3942
3942
'''
# print('12jlka445kljakldfjlaksjdfdka3942'.find('3924'))

def ff_ss(s,ss):
    count=0
    for i in range(len(s)-len(ss)+1):
        print(s[i:i+len(ss)])
        if s[i:i+len(ss)]==ss:
            count+=1
    return count
def gen_ff(s,ss):
    return sum([1 for i in range(len(s)-len(ss)+1) if s[i:i+len(ss)]==ss])

print(ff_ss('ABCDCDC', 'CDC'))
s='123e'
t = type(s)
for m in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
    print(any(m(c) for c in s))









