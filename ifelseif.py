age=int(input("Enter Age : "))
if age==0 or age<0:
    print("you cannot watch")
elif(0<age<=3):
    print("Ticket Price : Free ")
elif 3<age<=10:
    print("Ticket Price : 150 ")
elif 11<age<=60:
    print("Ticket Price : 250 ")
else:
    print("Ticket Price : 200 ")