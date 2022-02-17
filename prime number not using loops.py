def prime(num,i):
    if(i<num and num%i==0):
        return" not a prime number"
    if(i==num):
        return "a prime number"
    else:
        return prime(num,i+1)
num = int(input("Enter a number :"))
i=2
result= prime(num,i)
print(result)