x=int(input("input:"))

if x<0:
    print("Enter  a positive number")

c=0
num=1
while c<x:
    print(num,end=" ")
    num=num+2
    c=c+1