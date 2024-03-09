number = int(input("enter your number range : "))

li  = list(range(0,number+1))

#print(li)

even_list = []

even_count = 0

even_sum = 0

odd_list = []

odd_count = 0

odd_sum  = 0



for x in li:

    #print(x)

    if x%2==0:

        #print("EVEN NUMBER ")

        even_list.append(x)

        even_count +=1

        even_sum +=x

    else:

        #print("ODD NUMBER ")

        odd_list.append(x)

        odd_count+=1

        odd_sum +=x

print("even_numbers",even_list)

print("even_count",even_count)

print("even_sum",even_sum)

print("odd_numbers",odd_list)

print("odd_count",odd_count)

print("odd_sum",odd_sum)
        
