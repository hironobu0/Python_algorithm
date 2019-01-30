#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a~bの最大値を探して表示する

def find_max(a,b,c,d,e):
    numbers = [a,b,c,d,e]
    max = numbers[0]
    for i in numbers:
    if numbers[i] > max:
       max = numbers[i+1]
       if i > 4:
           break
    else:
        continue

    break




ans = find_max(3,6,1,3,9)
print ans
