'''
num = input("Enter the num")
if num % 2==0:
    k = num/2
else:
    k = (num+1)/2

for i in range(2,k+1,1):
    if num % i == 0:
        print("num is not prime")
        break
    else:
        if i == k:
            print ("num is prime")

if num ==1:
    print "The num is 1 and always prime"

lower = 2
upper = 50

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            if i == num-1:
                print (num)


num = input("enter num")
for i in range(2,num,1):
    if num % i == 0:
        print "not prime"
        break
    else:
        if i == num -1:
            print "prime"


'''

12121

num = "12121"
k = num.__len__()
res = ""
for i in range(k-1,-1,-1):
    print num[i]
    res = res + num[i]
print res



