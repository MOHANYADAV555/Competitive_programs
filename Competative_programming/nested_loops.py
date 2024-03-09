data=[1,2,4,2,6,4]
for i in range(0,len(data)):
    for m in range(i+1,len(data)):
         print(data[i], "and the data of m is",data[m])
         if data[i] == data[m]:
             print("duplicate is",data[m],"at index ",i)
      
