import re
from tqdm import tqdm
# import time
import shutil, os, sys
import PyPDF2 as p2
# Importar módulo Aspose.Words for Python
import aspose.words as aw
import pdfplumber
import pyautogui
import subprocess
import numpy as np

path = "/Users/migue/Documents/F1 Data Center/F1-Data-Center/Programs/Python/"
os.chdir(path)

sys.path.append(path)
import gp, gp_txt

file = 'result.pdf'
file_txt = 'result.txt'

zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'
resPatern = re.compile('\d+\s\d+\s'+'([A-Z][a-z]+\s[A-Z]+ |'+zho+'|'+ dev + ')' )
# drivers_sn_time = re.compile("([A-Z][a-z]+\s[A-Z]+\s+\d+[.]+\d+|"+zho+"+\s+\d+[.]+\d+|"+dev+"+\s+\d+[.]+\d+)")
# name = re.compile("("+dev+"+|[A-Z][a-z]+\s[A-Z]+|"+zho+"+)")
result = []

# inicio = time.time()

def pdfInSesions(sesions):
    pdf = True
    for i in sesions:
        if '.txt' in i:
            pdf = False
    return pdf


def max_5_sesions(sesions):
    pdf = pdfInSesions(sesions)
    
    if pdf:
        sesions = sesions[0:5]
    else:
        sesions = sesions[5:]
    
    return sesions

year = 2022
grand_prix = 'Brasil'

path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"+grand_prix+"_"+str(year)
os.chdir(path)

sesiones = []
p_sesion = ["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf","fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
for i in range(len(p_sesion)):
    path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"+grand_prix+"_"+str(year)+"/"+p_sesion[i]
    if os.path.exists(path):
        sesiones.append(p_sesion[i])
    else:
        sesiones.append("")

#Generate all data availble from sesiones
sesiones = max_5_sesions(sesiones)
if pdfInSesions(sesiones):
    datos = gp.gp(sesiones, grand_prix)
else:
    datos = gp_txt.gp(sesiones, grand_prix)


print(datos.stops)
# print(datos.race_name)
# print(datos.race_result)
### PDF VERSION ###
# invoice = open('result.pdf', "rb")
# pdfread = p2.PdfFileReader(invoice)
# a = pdfread.getNumPages()
        
# text = [] #Text of each season separated by pages

# #Extract text from each page
# for i in range(a):
#     with pdfplumber.open(invoice) as pdf:
#         page = pdf.pages[i]
#         text.append(page.extract_text())

# # #Split text if enter occurs
# for i in range(a):
#     for row in text[i].split('\n'):
#     #Obtain driver and its time from each row 
#         if  resPatern.search(row) != None:
#             result.append(re.search(resPatern, row).group())


### TXT VERSION (FASTER) ###
# with open('result.txt', "r", encoding='utf-8') as invoice:
#     text = invoice.readlines()

# names = datos.race_name

# num = []
# driv = []

# result = []
# #Split text if enter occurs
# for row in text:
    
#     if resPatern.search(row) != None:
#         todo = resPatern.search(row).group()
#         sp = todo.split()
#         num.append(int(sp[0]))
#         driv.append(sp[-1])

# print(num, driv)

# for n in names:
#     obj = False
#     for d in driv:
#         if d in n:
#             index = driv.index(d)
#             result.append(num[index])
#             obj = True

#     if not obj:
#         result.append('DNF')

# print(names)
# print(result)
# print(time.time() - inicio)


resPatern = re.compile('\d+\s+\d+\s+'+'([A-Z][a-z]+\s[A-Z]+ |'+zho+'|'+ dev + ')' )

row = '1       44      Lewis HAMILTON  MERCEDES        61      1:51:11.611     25'

if resPatern.search(row) != None:
    todo = resPatern.search(row).group()
    sp = todo.split()



#regex to find numbers
num = re.compile("\d")
#regex to find drivers surname
zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'
drivers_sn = re.compile("\d+\s("+dev+"|[A-Z][a-z]+\s[A-Z]+|"+zho+")\n")


drivers_apellido = []
            
#For each sesion, 20 drivers name
drivers_name = []

#1 time for each season               
time = []

#For each sesion, 20 drivers time (Each time is a list containing each time available)
drivers = []

#Stops 
stops = np.zeros(20, dtype= np.int64)

def get_sec(elem):
    """Convert x:yy:zzz to seconds"""
    if ':' in elem[0:1] or ':' in elem[2:4] or ':' in elem[5:8]:
        return sys.maxsize  #NOT THE CORRECT FORMAT; NOT CONSIDER THIS TIME

    suma = 0
    mins = int(elem[0:1])*60*1000
    sec = int(elem[2:4])*1000
    mil = int(elem[5:8])
    suma = mins + sec + mil
        
    return(suma)

for _ in range(20):
    drivers.append([])

driv = -1
with open('race.txt', "r", encoding='utf-8') as invoice:
    text = invoice.readlines()

#Split text if enter occurs
print(text[-2])
    