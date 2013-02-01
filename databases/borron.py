#!/usr/bin/env python
#-*- coding:utf-8 -*-

f = open('prueba4.csv')
for line in map(lambda x: x.strip(), f.readlines()):
    if len(line) > 0:
        print line
