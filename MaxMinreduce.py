#program for to accept two lists and find product
import functools
max=lambda x,y: x if x>y else y
min=lambda x,y: y if x>y else x
#main program
lst1=[float(val) for val in input().split()]

rs1=functools.reduce(max,lst1)
rs2=functools.reduce(min,lst1)

print("Max ={}".format(rs1))
print("Min ={}".format(rs2))
