#!/usr/bin/env python

# 列表的高级特性
import sys
if len(sys.argv) != 2:
	print('please supppl a filename')
	raise SystemExit(1)
f = open(sys.argv[1])
lines = f.readLines()
f.close()

fvalues = [float(line) for line in lines]

print("the minimum value is ", min(fvalues))
print("the maximum value is ", max(fvalues))