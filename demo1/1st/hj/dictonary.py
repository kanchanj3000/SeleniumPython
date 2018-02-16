from selenium import webdriver

#new_dict = {}
new_dict = dict()
new_dict.__setitem__("Ashok",56)
new_dict.__setitem__("Sunanda",45)
new_dict.__setitem__("Kanchan",25)
new_dict.__setitem__("Tinu",22)
new_dict.__setitem__("Priyanshu",12)
#print new_dict.pop("Tinu")
new_dict.popitem()
print new_dict


#k = new_dict.has_key("Tinu")
#print k
'''
v = new_dict.keys()
print v
s = v.__len__()
print s
for i in range(0,s,1):
    print new_dict.get(v[i])

'''
'''
dict_new = {"A":{"a":"apple","b":"banana","c":"papaya"},"B":{"k":"ball","d":"mat"},"C":{"n":"rat"},"D":["hh","jj"]}
print dict_new["D"][0]

'''
import json

with open('dict.json') as json_data:
    d = json.load(json_data)
    print(json.dumps(d))
    print d["alphabets"]["b"]
