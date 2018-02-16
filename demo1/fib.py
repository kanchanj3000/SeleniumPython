#WP for fibonacci
'''
0,1,1,2,3,5

first_num = 0
middle_num = 1

for i in range(0,50,1):
    next_num = first_num + middle_num
    print next_num
    first_num = middle_num
    middle_num = next_num

#WP for even and odd numbers
num = input("Enter the value of num :")
if num % 2 == 0:
    print "num is even"
else:
    print "num is odd"

    '''

even_num_list = []
odd_num_list = []

for i in range(1, 50, 1):
    if i % 2 == 0:
        even_num_list.append(i)
    else:
        odd_num_list.append(i)
print even_num_list
print odd_num_list