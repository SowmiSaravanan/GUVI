x=input()
x=x.split()
num=int(x[0])
pow=int(x[1])
pro=1
for i in range(pow):
  pro=pro*num
print(pro)
