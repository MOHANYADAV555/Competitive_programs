numbers =list (map(int,input("enter your numbers : ").split(",")))
#numbers
even = []
odd = []
even_count = 0
odd_count = 0
even_total = 0
odd_total = 0

for  z  in range(len(numbers)):

  if numbers[z]%2==0:

    even.append(numbers[z])
    even_count+=1
    even_total+=numbers[z]

    #print("even")

  else:

    odd.append(numbers[z])
    odd_count+=1
    odd_total+=numbers[z]


    #print('odd')
print(" even",even)
print(even_count)
print(even_total)

print("odd",odd)
print(odd_count)
print(odd_total)


