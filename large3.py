x=input()
x=x.split()
num1=int(x[0])
num2=int(x[1])
num3=int(x[2])
if num1>=num2 and num1>=num3:
  print(num1)
elif num2>=num1 and num2>=num3:
  print(num2)
else:
  print(num3)
