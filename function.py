""" ="hello"
x=list(x)
print(x[]) """



""" #Q7
a=list("hello")

b=[]
for x in a:
    if x=="a"or  x=="e" or  x=="i"  or x=="o" or  x=="u":
        x=list(x)        
        b.append(x)
print(len(b))

#Q8
a=(1,2,3)
print("largest num is")
if a[1]>a[2]and a[1]>a[0]:
    print(a[1]) 
elif a[2]>a[1]and a[2]>a[0]:
    print(a[2])
else:
    print(a[0])

#Q10
a=int(input("ener num "))
b=a+1
if a%b==0:
    print("not")
else:
    (print("prime") """
""" def sum(a,b):
    c=a+b
    return(c)

a=int(input("num "))
b=int(input("num2 "))
print(sum(a,b)) """
#Q1
""" def c(a):
    print(f"hello {a}!!")

a=input("ener name ")
c(a)

#Q2
def d(a,b):
    c=a*b
    return(c)

a=int(input("num "))
b=int(input("num2 "))
print(d(a,b))

#q3
def a(b):
    if b%2==0:
        print("even")
    else:
        print("odd")
b=int(input("ener num  "))       
a(b) """

""" #q4
def i():
    g=[]
    for x in range(5):
        a=int(input("ener num"))
        g.append(a)
    w=g[0]
    for y in g:
        if y > w:
            w=y
    print(w)
 """
""" 
#q5
def b():
    c=0
    a="hello"
    b="aeiou"
    for x in a:
        if x in b:
            c=c+1
    print(c)
b()
 """
 #q7
""" ef a(*num):
    num=list(num)
    for y in num:
        print(y/5)

for x in range(5):
    b=int(input(""))

a(x) """
 

""" def find_average(*args):
    if len(args) == 0:
        return 0  # to avoid division by zero
    
    total = sum(args)
    avg = total / len(args)
    return avg
for x in range(5):
    b=int(input(""))

find_average(x) """
#Q8
""" def a():
    d={a:1,b:2,c:3}
    if d[a]>d[b]
    print(d[a]) """

""" ef a(*num):
    print(num)
    b=0
    for i in num:
       b+=i
    return b
    
print(a(10,20,30,12,2)) 


def a(*num):
    for i in num:
        if i>num[0]:
            b=i
    return b 

print(a(10,20,30,40,2))

 """
""" def a(f):
    def b():
        return f().upper()
    return b
@a
def c():
    return "hell o"
print(c()) """

def sum():
    global a,x
    a=10
    x=23
    return a+x
print(sum())


def sub():
    
    return a-x
print(sub())


































































