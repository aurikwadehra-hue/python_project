""" b="Python - Slicing Strings"
print(b[-15:-9])
# Slicin 
name="rohan"
std=6
school="abcd"
txt=f"my name is {name},i study in {std} in {school}"
print(txt) """
""" #q1
a="hello I am Aurik"
b=(a.lower())
print(b.replace("h","H"))
#q3
c=i am aurik 
i study in 8 class 
i like soccer

d=(c.split(" "))
print(len(d))
#q4
f="1 2 3 4"
e=(f.split(" "))
if len(e)>=5:
    print("strong")
else:
    print("not")
#Q5
file=input("enter file name")
file2=(file.split("."))
print(file2[1])
 
# q7q10
g="best traning institute in greater noida"
print(g.replace(" ","-"))

#q9
k="product is nice and good"
j=(k.split(" "))
if j=="good":
    print("feedback is good")
else :
    print ("bad feed back")

 """
 #q10
sms="hello i am aurik"
m=(sms.split(" "))
s=len(m)
if s>=160:
    print("exeed") 
else:
    print("not exeed")
#q12
phone="12345"
r=(phone.replace("123","xxx"))
print(r)
#q14
tx="I love apples, apple are my favorite fruit"
print(tx.count("apple"))
