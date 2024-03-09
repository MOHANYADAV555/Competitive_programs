print("WELCOME TO THE CHADALAWADA RAMANAMMA ENGINEERING COLLEGE ")
Studet_record = { }

numbers = int(input("enter how many members are their : "))

for i in range(1,numbers+1):
    #print(i)
    Name = input("enter your student name : ")
    

    percentage = int(input("Enter % of marks of student : "))
    

    #print(Name)
    #print(percentage,"%")
    Studet_record[Name]=percentage
    print(Studet_record)
print("NAME OF THE STUDENT","\t","PERCENTAGE OF MARKS%")
for x in Studet_record:
    print("\t",x,"\t\t",Studet_record[x])  # here \t is using for white space 
    
