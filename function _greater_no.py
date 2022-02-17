#Which number is greatest ?
def greater(a,b):
    if a>b:
        return a
    return b

#def greatest(a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    return c

def new_greatest(a,b,c):
    #bigger=greater(a,b)
    return greater(greater(a,b),c)

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))

big=new_greatest(a,b,c)

print(f"{big} is greater")