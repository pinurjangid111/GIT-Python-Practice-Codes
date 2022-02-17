sum=0
x=[2,3,4,6,2,6,5,6,7,7]
for i in x:
    sum=sum+i
    mean=sum/len(x)
print(f"Mean is: {mean}")
n=len(x)
x.sort()
if(n%2==0):
    med1=n//2
    med2=(n//2)+1
    final_median=(x[med1-1]+x[med2-1])/2
else:final_median=x[n//2]
print(f"Final median is :{final_median}")
import statistics
mode2=statistics.mode(x)
print(f"Mode is : {mode2}")

