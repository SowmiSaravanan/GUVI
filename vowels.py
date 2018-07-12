al=input()
if al=='a' or al=='e' or al=='o' or al=='i' or al=='u':
  print("Vowel")
elif al=='#' or al=='&' or al=='$'or al=='@':
  print("Invalid")
elif ord(al)>=97 and ord(al)<=122:
  print("Consonant")
