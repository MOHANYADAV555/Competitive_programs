# FIRST 3 MULTIPLES OF A GIVEN NUMBER
n = int(input("enter your number :  "))

b = int(input ("how many multiples you have :  "))
        

#c = []

for i in range (1,b+1):
    c = c + str(n*i)+" "
    #c.append(n*i)
    print(i)
#print(*c)
#print(type(c))
    
    
#print(c.strip())
