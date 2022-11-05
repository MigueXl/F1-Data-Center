import multidata
import pdfplumber
import PyPDF2 as p2
import re


#regex to find numbers
num = re.compile("\d")
#regex to find drivers surname
zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'
drivers_sn = re.compile("\d+\s("+dev+"|[A-Z][a-z]+\s[A-Z]+|"+zho+"+)")

class gp:
    ...