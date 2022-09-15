import pandas as pd
import glob
import xlrd
import openpyxl

lst=[]
for i in glob.glob('*.xls'):
    print(i)
    lst.append(i)
print(lst)

for i in glob.glob('*.xlsx'):
    print(i)
    lst.append(i)
print(lst)

bddlist = []
for i in lst:
 bdd = pd.read_excel(i)
 bddlist.append(bdd)
print(bddlist)
df=pd.concat(bddlist,axis=1)




