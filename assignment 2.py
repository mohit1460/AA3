#question1

l=[]
name1= input("enter the input for the list")
l.append(name1)
name2= input("enter the input for the list")
l.append(name2)
print("the list is", l)



#question 2

c=['google','apple','facebook','microsoft','tesla']
print (c+l)

#question3

z=[1,2,3,1]
print(z.count(1))

#question4

m=[3,2,1]
m.sort()
print (m)

#question 5

a=[7,8,9]
b=[1,2,3]
a.sort()
b.sort()
c=a+b
c.sort()
print (c)

#question 6

a=[1,2,3,4,5]
a.pop()
print(a)
a.append(2)
print(a)

#question 7

even=[]
odd=[]
for num in range(1,11):
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print (even)
print(odd)
print(len(even))
print(len(odd))









