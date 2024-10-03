#program for to filter the words whose content alpha,special symbol and degit

alpha=lambda letter:letter.isalpha()
digit=lambda letter:letter.isdigit()
specialSym=lambda letter:not letter.isalnum()

#main program
s=list(input())
aw=list(filter(alpha,s))
dw=list(filter(digit,s))
ssw=tuple(filter(specialSym,s))

print(aw)
print(dw)
print("special Symbol ={}".format("".join(ssw)))
