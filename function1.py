def add_two(a,b):
    return a+b

def min_two(a,b):
    return a-b

def mul_two(a,b):
    return a*b

a=int(input("Enter a : "))
b=int(input("Enter b :"))

total=add_two(a,b)
total2=min_two(a,b)
total3=mul_two(a,b)

print(total)
print(total2)
print(total3)