import openpyxl
import xlwt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from xlrd import open_workbook

#book = open_workbook('C:\Users\Friends\Desktop\dummy.xlxs')
'''
fp = open("C:\Users\Friends\Desktop\dummy.xlxs",'r')
wb = openpyxl.load_workbook("dummy.xlxs")
wb.get_sheet_names()
sheet = wb.get_sheet_by_name("Sheet1")
'''
file = open("C:\Users\Friends\Desktop\dummy.xlxs",'r')
x1 = pd.ExcelFile(file)
print (x1.sheet_names)