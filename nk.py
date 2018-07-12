n=int(input())
k=int(input())
lis=[]
sum=0
for i in range(n):
  num=int(input())
  lis.append(num)
for i in range(k):
  sum=sum+lis[i]
print (sum)
