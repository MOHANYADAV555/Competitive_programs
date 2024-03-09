"""print(list(range(1,100)))
total=0
for i in range (1,100):
      if i%2==0:
          total +=i
print(total)"""

given_list=[7,5,4,4,3,1,-2,-3,-5,-7]
total2=0
j=len(given_list)-1
while given_list[j]<0:
    total2 +=given_list[j]
    j-=1
print(total2)

