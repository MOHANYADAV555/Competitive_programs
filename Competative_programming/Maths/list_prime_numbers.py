number  = list(map(int,input()))

#print(number)
prime = []

composite  = []

prime_count = 0

composite_count = 0

add_prime = 0

add_composite = 0

for i in  number :

    count = 0

    for j in range (1,i+1):

        if i %j==0:

            count+=1

    if count==2:

        prime.append(i)

        prime_count+=1

        add_prime+=i


        #("prime number ")

    else:

        composite.append(i)

        composite_count+=1

        add_composite+=i


        #print("composite number ")

print("prime",prime)

print("count of prime numbers : ",prime_count)

print("add",add_prime)

print("composite ",composite)

print("count of composite : ",composite_count)

print("add",add_composite)
