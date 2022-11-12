import re
from tqdm import tqdm
import time
import shutil, os, sys
import PyPDF2 as p2
# Importar módulo Aspose.Words for Python
import aspose.words as aw
import pdfplumber


file = '2019_01_aus_f1_p1_timing_firstpracticesessionlaptimes_v01.pdf'

# patern = re.compile('_\d+_')
# number = patern.findall(file)[0]
# number = int(re.sub('_','',number))

patern = re.compile('_\d+_')
number_rare = patern.findall(file)[0]
#Remove '_'
number = int(re.sub('_','',number_rare))

# print(type(number))
# print(number)

l =["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf","fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]

# print(l[5:])

if '.pdf' in ['', '', 'fp3.pdf', '', '']:
    ...
    # print('Su')

path = "/Users/migue/Documents/F1 Data Center/"+"TestYear/"
os.chdir(path)

 
# # create file object variable
# # opening method will be rb
# pdffileobj=open('fp2.pdf','rb')
 
# #create reader variable that will read the pdffileobj
# pdfreader=p2.PdfFileReader(pdffileobj)
 
# #This will store the number of pages of this pdf file
# x=pdfreader.numPages
 
# #create a variable that will select the selected number of pages
# text = ''
# for i in range(x):
#     page = pdfreader.getPage(i)
#     text += page.extractText()

# file1=open(path+"fp1.txt","a+")
# file1.writelines(text)

# file1=open(path+"fp1.txt","rb+")
# print(file1.read())

# def getPDFFileContentToTXT(pdfFile):
#     myPDF= p2.PdfFileReader(pdfFile)

#     with open(path+"fp1.txt", 'w+') as pdf_output:
#         for page in range(myPDF.getNumPages()):
#             data = myPDF.getPage(page).extractText()
#             pdf_output.write(data)
    
#     with open(path+"fp1.txt", 'r') as myPDFContent:
#         return myPDFContent.read().replace('\n', ' ')


# getPDFFileContentToTXT('fp2.pdf')
# file1=open(path+"fp1.txt","r")
# print(file1.read())

import pyautogui
import subprocess

import os
import pyautogui
import time
from tqdm import tqdm


l = ['a','b','c','d']
text = ''
for y in tqdm(l, desc = 'Year Progress Bar'):
    text += y
    time.sleep(1)

print(text)

dir = os.getcwd()+ '\\'
path = 'C:\\Users\\migue\\Documents\\F1 Data Center\\TestYear\\'
pdf = 'fp2.pdf'
txt = 'fp1.txt'
# print(dir)

# possible =  ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
# done = open('DONE.txt', 'a+')
# for i in possible:
#     done.writelines(i+'\n')
# done.close()

# with open('DONE.txt', 'r') as check:
#     result = check.readlines()    
#     resCorrect = [ r.replace('\n','') for r in result]

# print(resCorrect)
# setA = set(possible)
# setB = set(resCorrect)
# print(list(setA-setB))


# os.startfile(dir+pdf)
# time.sleep(0.5)
# pyautogui.hotkey('ctrl', 'a')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.hotkey('alt', 'f4')
# time.sleep(0.5)
# os.startfile(dir+txt)
# time.sleep(0.5)
# pyautogui.hotkey('ctrl', 'e')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.hotkey('ctrl', 'g')
# pyautogui.hotkey('alt', 'f4')
# time.sleep(0.5)

