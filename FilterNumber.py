#Program for Filtering +Ve Values and -Ve Values by using filter()
pos= lambda val:val>0 # Anonymous Function
neg= lambda val:val<0 # Anonymous Function

#Main Program
print("Enter List of Numerical Values separated by space")
lst=[float(val) for val in input().split()]
pslist=list(filter(pos,lst))
nglist=list(filter(neg,lst))
print("+Ve Elements=",pslist)
print("-Ve Elements=",nglist)

