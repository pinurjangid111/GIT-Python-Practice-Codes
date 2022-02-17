#n=int(input("Enter a number : "))
#total=0
#for i in range(1,n+1):
#    total+=i
#print(f"Sum is : {total}")

total=0
num=input("Enter a 4 digit number : ")
for i in range(0,len(num)):
    total+=int(num[i])

print(f"Sum of digits are : {total}")
