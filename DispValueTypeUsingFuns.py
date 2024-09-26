#OProhgram accepting a Value and Display Its Type
def dispvaluetype(obj):
    if(type(obj)==int):
        print("{} is an int type value".format(obj))
    elif (type(obj) == float):
        print("{} is an float type value".format(obj))
    elif (type(obj) == bool):
        print("{} is an bool type value".format(obj))
    elif (type(obj) == complex):
        print("{} is an complex type value".format(obj))
        print("\tReal part={}".format(obj.real))
        print("\tImaginary Part={}".format(obj.imag))
    elif (type(obj) == str):
        print("{} is an str type value".format(obj))
        print("\tLength of {}={}".format(obj,len(obj)))
    elif (type(obj) == bytes):
        print("{} is an bytes type value".format(obj))
        for val in obj:
            print(" {}".format(val),end=" ")
        print()
    elif (type(obj) == bytearray):
        print("{} is an bytearray type value".format(obj))
        for val in obj:
            print(" {}".format(val),end=" ")
        print()
    elif (type(obj) == range):
        print("{} is an range type value".format(obj))
        for val in obj:
            print(" {}".format(val),end=" ")
        print()
    elif (type(obj) == list):
        print("{} is  list type value".format(obj))
    elif (type(obj) == tuple):
        print("{} is  tuple type value".format(obj))
    elif (type(obj) == set):
        print("{} is  set type value".format(obj))
    elif (type(obj) == frozenset):
        print("{} is  frozenset type value".format(obj))
    elif(type(obj)==dict):
        print("{} is  dict type value".format(obj))
        for k,v in obj.items():
            print("\t{}-->{}".format(k,v))
    else:
        print("{} is  NoneType type value".format(obj))

#Main Program
a=10
dispvaluetype(a)
b=12.34
dispvaluetype(b)
c=True
dispvaluetype(c)
d=2+3j
dispvaluetype(d)
s="PYTHON PROG"
dispvaluetype(s)
bts=bytes([10,20,30,40])
dispvaluetype(bts)
bta=bytearray([10,20,30,40])
dispvaluetype(bta)
r=range(10,21,2)
dispvaluetype(r)
lst=[10,"RS",34.56,True,2+3j]
dispvaluetype(lst)
tpl=(100,"TR",3.4,"Python")
dispvaluetype(tpl)
st={10,20,30,40,50,10,20}
dispvaluetype(st)
fst=frozenset({10,20,30,40,50,10,20,"Python"})
dispvaluetype(fst)
d={10:"Rossum",20:"Travis",30:"Hunter",40:"Ritche"}
dispvaluetype(d)
n=None
dispvaluetype(n)
