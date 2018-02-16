#Dictonaries

my_dicto = {1:"Green",2:"Blue",3:"red"}
print (my_dicto[1])
print len(my_dicto)
print my_dicto.keys()
print my_dicto.values()
print my_dicto.items()
print my_dicto.get(2)
my_dicto.update({4:'White'})
print my_dicto

'''

#Sets

my_set = {1,2,3,4,3,1,2,9,0}
my_set1 = {2,6,5,7,0,9}
print my_set
print "intersection=", my_set & my_set1
print "difference=", my_set - my_set1
print "Union=",my_set1 | my_set

#flow control

marks = 50
if (marks >=80):
    print "grade A"
elif (marks>=60) and (marks<=80):
    print "Grade B"
elif (marks>=40) and (marks<=60):
    print "Grade C"
else:
    print("fail")



for quant in range(99,0,-1):
    if quant>1:
        print (quant,"bottles of beer on the wall",quant,"bottles of beer")
        if quant>2:
            suffix=str(quant)+"bottles of beer on the wall"
        else:
            suffix="1 bottle of beer on the wall"

    elif quant ==1:
                print("1 bottle of beer on the wall ,1 bottle of beer")
                suffix= "No more beer on the wall"

    print("Take one down pass it around", suffix)
    print ("---")
'''
count = 0
while(True):
    print count
    count+=1
    if count>10:
        break



for x in range(20):
    if(x%2)==0:
        continue
    print x



