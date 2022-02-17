print("1 : ADDITION \n2 :SUBSTRACTION \n3 :MULTIPICATION \n4 :DIVISION")
print("Enter your choice :")
op=int(input())
print("Enter first number")
a=int(input())
print("Enter second number")
b=int(input())
if(op==1):
 print("The sum is ",a+b)
elif(op==2):
 print("The difference is ",a-b)
elif(op==3):
 print("The product is ",a*b)
else:
 print("The quotient is ",a/b)
