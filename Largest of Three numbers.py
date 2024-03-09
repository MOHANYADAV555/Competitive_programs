# Largest of Three Numbers

a = eval(input("Enter First Number : "))
b = eval(input("Enter Second Number : "))
c = eval(input("Enter Third Number :"))

if a>b:
    if a>c:
        largest = a
    else:
        largest = c
else:
    if(b>c):
        largest=b
    else:
        largest=c
print("Largest of three numbers is : ",largest)