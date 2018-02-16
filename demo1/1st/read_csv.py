import csv
import codecs

'''
csv_file = codecs.open("C:\Users\Friends\Desktop\demo.csv", encoding="utf-8-sig")
csv_reader = csv.reader(csv_file)
csv_lst = list(csv_reader)
print csv_lst
for row in csv_lst:
    print(row)
    print(row[0])

try:
    f = open("C:\Users\Friends\Desktop\demo.csv","rb")
    reader = csv.reader(f)
    for column in reader:
        print column[0], column[1], column[2]
except:
    print "IndexError: list index out of range"



k = open("C:\Users\Friends\Desktop\\new_data.csv","rb")
reader = csv.reader(k,delimiter=',')
dates = []
colors = []
for row in reader:
    date = row[0]
    color = row[1]
    dates.append(date)
    colors.append(color)
print dates
print colors
'''
# file writing

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]

k = open("C:\Users\Friends\Desktop\\new_data1.csv","w+")
writer = csv.writer(k,delimiter=',')
k.writelines("('first_name', 'second_name', 'Grade'),\n('Alex', 'Brian', 'A'),\n('Tom', 'Smith', 'B')")
print k