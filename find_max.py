#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a~bの最大値を探して表示する

def find_max(a,b,c,d,e):
    numbers = [a,b,c,d,e]
    max = 0
    for i in range( len(numbers) ):
        if max < numbers[i]:
            max = numbers[i]

    return max

ans = find_max(12,6,1,3,9)
print ans
