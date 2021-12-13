l1=[]
n=int(input("enter the limit of the list"))
print("enter  Numbers",n)
for i in range(0,n):
    t=int(input())
print("old list:",l1)
l2=[i for i in l1 if i>0]
print("new list:",l2)
