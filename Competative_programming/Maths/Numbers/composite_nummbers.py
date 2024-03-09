number = int(input("enter your number" ))
count=0
for i in range(2,number+1):
    if (number%i)==0:
        count= count+1
if (count>2):
    print("composite number")

else:

    print(" not a composite number")
    
