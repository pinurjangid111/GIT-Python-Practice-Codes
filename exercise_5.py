n=input("Enter a number more than one digit (Ex: 1234)  :  ")
total=0
i=0
while i < len(n):
    total +=int(n[i])
    i +=1
print(f"Sum of digits : {total}")