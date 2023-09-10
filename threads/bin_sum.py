#!/usr/bin/env python

def bin_sum(b1:str, b2:str) -> str:
    max_len = max(len(b1), len(b2))
    b1 = b1.zfill(max_len)
    b2 = b2.zfill(max_len)

    carry = 0
    res=''

    for i in range(max_len-1,-1,-1):
        r=0
        r+=1 if b1[i]=='1' else 0
        r+=1 if b2[i]=='1' else 0
        res=('1' if (r+carry)%2==1 else '0') +res
        carry = 0 if (r+carry)<2 else 1
    return '1' + res if carry !=0 else res


if __name__=='__main__':
    print(bin_sum('1111','1111'))
    print(bin_sum('100101', '10101'))
    print(bin_sum('11', '1'))
    print(bin_sum('1010', '11'))