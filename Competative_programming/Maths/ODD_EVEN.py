number=input()
b=list(map(int,number))
even=0
Odd=0
for i in range(len(b)):
    if b[i]%2==0:
        print("even")
        even +=1
    else:
        print("odd")
        Odd+=1
print(even)
print(Odd)

              
