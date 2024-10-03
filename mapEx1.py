#program for to accept a list of number and print square and square root
squre=lambda num: num*num
squreroot=lambda num:num**(0.5)

#main program
lst=[int(num) for num in input().split() if num.isdigit()]
sqrnum=list(map(squre,lst))
sqrtnum=list(map(squreroot,lst))
print("------------------------------------------------")
print("Number\t\t\tSquare\t\t\tsquare root")
print("------------------------------------------------")
for num,sqr,sqrt in zip(lst,sqrnum,sqrtnum):
    print("\t{}\t\t\t{}\t\t\t\t{}".format(num,sqr,"%0.2f"%sqrt))
print("--------------------------------------------------------")
