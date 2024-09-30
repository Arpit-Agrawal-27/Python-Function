#Program for calculate the all arithmetic operation with anonymous Function
sumop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
floordivop=lambda a,b:a//b
modop=lambda a,b: a%b
powop=lambda a,b: a**b

#main Program
print("=" * 50)
print("Arithmetic Operations by using Anonymous Functions")
while True:
    print("=" * 50)
    print("Enter Two Numerical value")
    print("-"*50)
    a,b=float(input()),float(input())
    op=input("Enter any Arithmetic Operator:")
    if op in ["+","-","*","**","/","//","%"]:
        match op:
            case "+":
                print("\tsum {},{}={}".format(a,b,sumop(a,b)))
            case "-":
                print("\tsubtraction {},{}={}".format(a,b,subop(a,b)))
            case "*":
                print("\tMultiplication {},{}={}".format(a,b,mulop(a,b)))
            case "/":
                print("\tDivision {},{}={}".format(a,b,divop(a,b)))
            case "//":
                print("\tFloorDivision {},{}={}".format(a,b,floordivop(a,b)))
            case"%":
                print("\tmodules {},{}={}".format(a,b,modop(a,b)))
            case"**":
                print("\t{} to the Power of {} = {}".format(a,b,powop(a,b)))
        break
    else:
        print("{} is Invalid Arithmatic Operator please Try again".format(op))
