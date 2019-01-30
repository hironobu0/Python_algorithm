#!/usr/bin/env python
# -*- coding: utf-8 -*-

def compare_ab(a,b):
    if a > b:
        print a
    elif a == b:
        print "aとbは同じです"
    else:
        print b

n = compare_ab(10,20)
