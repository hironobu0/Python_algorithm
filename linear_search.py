#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 線形探索のアルゴリズム

def linear_search(a,b,c,d,e):
    list = [a,b,c,d,e]
    target = 5

    j = 0
    for i in range( len(list) ):
        if  list[i] == target:
            print ("%d は %d 番目です。" % (target,i+1) )
            break
        else:
            j += 1
            if j == len(list):
                print ("リストの中にはありませんでした。")

linear_search(1,5,3,2,8)
