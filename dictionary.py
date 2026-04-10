""" a={"name":"aurik",
"class":8,
"sec":"b",
"teacher":["a","b","c"]}
print(a["class"])

b=f"hi! i am {a["name"]} i am in {a["class"]} in sec{["sec"]}"
print(b)
a["school"]="abcd"
print(a)
 
#q2
person = {'name': 'Bob', 'age': 30}
print(person['name'])
print(person.get('age'))

#q3
a={1:2}
a[2]=3
print(a)

#q4
a={'a':1}
a["a"]=2
print(a)

#q5

a={1:2,2:3,3:4}
del a[1]
a.pop(2)
print(a)
#Q6
print(len(a))

#Q7
a={'a': 1,"b": 2}
print("a" in a)
print("c"in a)

#q8
x=a.items()
y=a.values()
z=a.keys()
print(x)
print(y)
print(z)

#Q9
x=a.get('a')
print(x)

#Q10
b={}
print(len(a))


#Q11
b={5:5}
a.update(b)
print(a)


#Q12
a={1:1,2:2,3:3}
a.setdefault(4,4)
print(a)

#Q14
c=a | b
print(c)

#Q15
a={
1:1,
2:2,
3:{4:4,5:5}
}
print(a)"""

#Q16
a="aurik wadehra"
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)

""" #17
d={1:1}
d.pop("b")
print(d) """
#Q18!!
scores = {'Alice': 85, 'Bob': 92, 'Carol': 78}
""" a={"A":3,"B":2,"C":8}
if a["A"]and a["B"]> a["C"]:
    a["C"]=a[0]
elif a["B"]and a["C"] > a["A"]:
    a["A"]=a[0]
elif a["A"] and a["C"]> a["B"]:
    a["B"]= a[0] """
""" sorted_d = dict(sorted(scores.items(),
key=lambda x: x[1]))
print(sorted_d)

#q19
d = {'a': [1, 2], 'b': [3, 4]}
d['a'].append(99)
print(d)

#Q20
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()} # {1:'a', 2:'b', 3:'c'}
print(inverted)
 """
""" a=int(input("enter num "))
b=int(input("enter num2 "))
c=input("enter *,/,+,- ")
if c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='-':
    print(a-b)
elif c=='+':
    print(a+b)
 """
#example11
a=250010
    print("0tax")
elif a<500000 and a>250000:
    print(a-a*5/100)
elif a<1000000 and a>500000:
    print(a-a*20/100)
elif a>1000000:
    print(a-a*30/100)











































