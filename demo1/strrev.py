str_name = "KANCHAN" # NAHCNAK
k = str_name.__len__()
res = ""
for i in range(k-1,-1,-1):
    res +=str_name[i]
print res


str_name1 = "MERRYXMAS"
k = str_name1.__len__()

for i in range(k-1,-1,-1):
   print str_name1[i]


str_name1 = "MERRYXMAS"
k = str_name1.__len__()
res1 =""
for i in range(k-1,-1,-1):
   res1+=str_name1[i]
print res1



str_name = "I m the best"
k = str_name.split()
v = k.__len__()
res = ""
for i in range(v-1,-1,-1):
    print k[i]
    res += k[i]
print res