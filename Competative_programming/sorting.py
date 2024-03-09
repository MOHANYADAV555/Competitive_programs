array = [9,3,2,4,5,6]
for i in range(0,len(array)):
    print(i)
    for j in range(i+1,len(array)):
        print(j)
        if array[i]>array[j]:
            temp=array[i]
            array[i]=array[j]
            array[i]=temp
print(array)
