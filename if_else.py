""" a=int(input("enter value of a"))
if a > 0:
    print("a is positive")
else:
    print("a is negitive") """
""" a=input("enter value of a" )
b=input("enter value of b") """
""" a=.
b=-
if a>b:
    print("a is greater")
elif a<b:
    print("b is greater")
elif a==b:
    print("b and a are equal")
else :
    print("these are not Number") """
""" 
a=.
if a.isdigit():
    print("this is a Number")
else :
    print("this is not a number") """
""" core=int(input("enter score"))
if score >=90:
    print("a")
elif score>=70:
    print("b")
elif score>=60:
    print("c")
elif score>=50:
    print("d")
else :
    print("f")  """
""" #    Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if a==c or b==c:
"""
""" #q2
a=int(input("enter value of a"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")

#q3
age=int(input("enter age"))
if age<18:
    print("minor")
elif age<=60:
    print("adult")
else :
    print("senior")
#q4
p=(input("enter a letter"))
if p=="A" or p== "E" or p=="I" or p=="O" or "U":
    print("vowal")
else:
    print("consonaent") 
#q5
b=int(input("enter a no"))
if b%3==0:
    print("divisable by 3")
elif b%5==0:
    print("divisabl
    print("not divisable")
#q7
c=int(input("enter a no2"))
d=int(input("enter a no1"))
if c>d:
    print("c>d")
elif c<d:
    print("d>c")
else:
    print("both are equal")
#q8
year=int(input("enter year"))
if year%4==0:
    print("leap")
else:
    print("normal")
#q9
l=input("enter name")
pa=input("enter paswered")
if l=="admin" and pa="1234":
    print("scsessfull")
else:
    print("not scscesful")"""
""""#Q10
a=int(input("enter no1"))
b=int(input("enter no2"))
c=input("enter operator")
if c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
else:
    print("enter an opeerator")"""
""" #BMI Calculator: weight / (height * height)
a=float(input("enter hight"))
b=float(input("enter wieght"))
c=b/(a*a)
if c<=14:
    print("under weight")
elif c>=14.5:
    print("normal")
elif c>=25:
    print("over weight")
elif c>= 30:
    print("obase")
else:
    print("enter proper hight or wight")""
 """
a=int(input("enter math marks"))
b=int(input("enter english marks"))
c=int(input("enter sst marks"))
d=int(input("enter hindi marks"))
e=int(input("enter it"))
total=a+b+c+d+e
av=(total/5)
print(av)
if av<=100 and av>90:
    print("A")
elif av<=90 and av>80:
    print("B")
elif av<=80 and av>60:
    print("C")
elif av<=60 and av>40:
    print("D")
elif av<40:
    print("F")