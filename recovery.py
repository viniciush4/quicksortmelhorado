#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from plotpoint import plot

	
def recovery():
	f = open(sys.argv[1],'r')
	string = f.read()
	l1 = string.split('\n')
	l2 = []
	h = ''
	m = int(l1[0])
	for x in l1[1:]:
		try:
			h,t = x.split(':')
			l = [(h,x) for x in t.split(',') if x != '']
			l2 += l
		except:
			continue
	
	f.close()
	plot(l2,int(h),m)

recovery()
