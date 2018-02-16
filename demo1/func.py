'''
def func(n):
    a = 0
    b = 1
    for x in range(n):
        a = b
        b = a + b
        print( a, '\n')
    return b
num = int(input("Enter the value of n:"))
print (func(num))


fp = open("C:\Users\Friends\Desktop\\kanchi\\python.txt",'w+')
fp.write("Python is fun")
fp.seek(0)
print fp.read()
fp.close()


def func(a,b):
    return a * b

print func(2,4)
print func("test",4)

def add(list):
    list.append("new")

list =["kanchan"]
print list
add(list)
print ("1st example")
print list


'''

def f(a=10,b=20,c=30):
    print (a,b,c)
    print f(c=10)



