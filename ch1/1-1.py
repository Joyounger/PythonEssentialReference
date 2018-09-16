#!/usr/bin/env python

#$ python 1-1.py
#1 1050.0
#2 1102.5
#3 1157.625
#4 1215.5062500000001
#5 1276.2815625000003


principal = 1000	# 初始金额
rate      = 0.05	# 利率
numyears  = 5		# 年数
year = 1
while year <= numyears:
	principal = principal * (1 + rate) # python的变量名称是无类型的,在执行过程中可以引用任意类型的数据
	print(year, principal)
	year += 1