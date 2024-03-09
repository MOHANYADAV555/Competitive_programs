num = list(map(int,input()))
#print(num)


for i in num:
    #print(num[i])
    count  = 0
    for j in range(1,i+1):
        #print(j)
        if i%j==0:
            count=count+1
            #print(count)
    if count>2:
        
        print("composite number")
    else:
        print("not a composite number")
        
    
    
    

