'''
num = input("Enter the num")
for i in range(2, num, 1):
    if num % i == 0:
        print ("num is not prime")
        break
    else:
        if i == num -1:
            print ("num is prime")

upper_number = 50
lower_number = 2
for num in range(lower_number, upper_number + 1, 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
            if i == num - 1:
                print num


positive_num = []
negative_num = []
for i in range(-10,10,1):
    if i >= 0:
        positive_num.append(i)
    else:
        negative_num.append(i)
print positive_num
print negative_num



odd_num_list = []
even_num_list = []
for i in range(0,50,1):
    if i % 2 == 0:
        even_num_list.append(i)
    else:
        odd_num_list.append(i)
print odd_num_list
print even_num_list


#0,1,1,2,3,5,8,12

first_num = 0
middle_num = 1
for i in range(0,50,1):
    last_number = first_num + middle_num
    print last_number
    first_num = middle_num
    middle_num = last_number


string = "KANCHAN"
k = string.__len__()
res = ""
for i in range(k-1,-1,-1):
    print string[i]


str_name = " I got a Job"
k = str_name.split()
v = k.__len__()
res = ""
for i in range(v-1,-1,-1):
    res = res + k[i]
print res


list = [10,20,30,40,50]
k = list.__len__()
for i in range(k-1,-1,-1):
    print list[i]


num_array = [6, 1, 9, 90, 34, 20, 10, 36, 89]
k = num_array.__len__()
for j in range(0,k-1,1):
    for i in range(j+1,k,1):
        if num_array[j] > num_array[i]:
            temp = num_array[j]
            num_array[j] = num_array[i]
            num_array[i] = temp
print num_array
print num_array[0]
print num_array[k-1]


num = input("Enter the number")1*2*3
res = 1
for i in range(1,num,1):
    res = res * i
print res



12121

num = input("enter the number")
temp = num
rev = 0
while num > 0:
    dig = num % 10
    print dig
    rev = rev * 10 + dig
    print rev
    num = num // 10
    print num
if temp == rev:
    print ("Number is palindrome")
else:
    print ("Number is not palindrome")


num = input("Enter the number")
temp = num
sum = 0
while num > 0:
    dig = num % 10
    sum = sum + dig ** 3
    num = num // 10
if temp == sum:
    print ("Num is amstrong")
else:
    print ("Num is not amstrong")



lower = 100
upper = 1000


for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        dig = temp % 10
        sum = sum + dig ** order
        temp = temp // 10
    if num == sum:
        print num
'''

lower = 100
upper = 10000
for num in range(lower, upper):
    temp = num
    sum = 0
    while temp > 0:
        dig = num % 10
        sum = sum * 10 + dig
        temp = temp // 10
    if num == sum:
        print num
