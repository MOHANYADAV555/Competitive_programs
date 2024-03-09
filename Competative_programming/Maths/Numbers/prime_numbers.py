lower = int(input())

for i in range (2,lower+1):

  if i >1:

    for j in range(2,i):

      if (i%j)==0:

        break

    else:

      print(i)
        #i = str(i)    # 35
        #print(i)
        #if int(i[-1]) ==  3:
            #print("satisfied prime with end 3")


