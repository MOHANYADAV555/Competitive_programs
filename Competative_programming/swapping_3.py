data = input("enter your input")
my_list =  list(data)
size = len(my_list)
temp = my_list[0]
my_list[0] = my_list[size-1]
my_list[size-1] = temp
print(my_list)

