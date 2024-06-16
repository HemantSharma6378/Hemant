a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
oprator=input("Enter oprator +,-,*,/,%,**,// :")

if oprator == '+':
    print(f"addition of a and b is  {a+b}")
elif oprator == '-':
    print(f"subtraction of a and b is  {a-b}")
elif oprator == '/':
    print(f"division of a and b is  {a/b}")
elif oprator == '**':
    print(f"Exponentiation of a and b is  {a**b}")
elif oprator == '//':
    print(f"Floor Division of a and b is  {a//b}")    
elif oprator == '*':
    print(f"multiplication of a and b is  {a*b}")
elif oprator == '%':
    print(f"Modulus of a and b is  {a%b}")
else:
    print(f"invalid sentance")