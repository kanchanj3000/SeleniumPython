'''

string1 = "Kanchan"
string2 = "Mayur"


print (string2+string1)
print (string2*3)
print (string2[2:-1])



print (string1.count('n',0,7))
print (string1.find('n'))
print string2.upper()
print string2.isalnum()
print string2.isupper()
print string2.isupper()
print string1.split()
print len(string1)


#Tuples


x = []
my_tup = ('kanchan','Mayur','Piyu','Pup')
print (my_tup+('Gabru','Zappu'))
print my_tup*2
print my_tup[1:5]
print my_tup.count('kanchan')



#List
my_list = ["kanchan","Mayur"]
my_list.append("Piyu")
print my_list
my_list.extend(["Rathod","Jadhav"])
print my_list.pop()

'''

from TestPkg import Constant

print Constant.firstname
print Constant.secondname
print Constant.thirdname
Constant.printname()
print Constant.getthirdname()