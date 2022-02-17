ob = [1,5,4,2,3]
sum=0
for i in range(len(ob)):
    sum+=ob[i]
mean= sum/len(ob)
sum_of_squared_deviation = 0
for i in range(len(ob)):
    sum_of_squared_deviation+=(ob[i]-mean)**2
sd = ((sum_of_squared_deviation)/len(ob))**0.5
print("Standard Deviation of sample is ",sd)
