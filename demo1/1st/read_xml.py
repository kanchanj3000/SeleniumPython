from xml.etree.ElementTree import Element,SubElement,tostring
import xml.etree.cElementTree as ET
import untangle
import xmltodict
import lxml
import csv
'''
fp = open("C:\Users\Friends\Desktop\MK1.txt",'w+')
fp.writelines("have a nice day,\npython is good,\nnice to meet you,\nsee you soon")
fp.read()

############

#fp = open("C:\Users\Friends\Desktop\MK2.xml",'w+')

obj = untangle.parse(r'C:\Users\Friends\Desktop\MK2.xml')
print obj.root.child.cdata
#root = Element('root')
#child = SubElement(root, "child")
#child.text = "I am a child"

###########

with open(r"C:\Users\Friends\Desktop\MK2.xml") as fd:
    doc = xmltodict.parse(fd.read())
print doc['root']['child']

'''
###########################
#fp = open("C:\Users\Friends\Desktop\MK4.xml",'w+')

root = ET.Element("root")
doc = ET.SubElement(root,"doc")
child = ET.SubElement(doc,"child")

value1 = ET.SubElement(child,"field",name = 'kanchan').text
value2 = ET.SubElement(child,"filed2",name = 'mayur').text

tree = ET.ElementTree(root)
tree.write('C:\Users\Friends\Desktop\MK4.xml')

#############################

