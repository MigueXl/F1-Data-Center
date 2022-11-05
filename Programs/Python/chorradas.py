
import os
import re
path = "/Users/migue/Documents/F1 Data Center/"+'2022'+"/"+'Australia'+"_"+'2022'
os.chdir(path)


drivers_sn_time = re.compile("[A-Z][a-z]+\s[A-Z]+\s+\d+[.]+\d+")
zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'
name = re.compile("("+dev+"+|[A-Z][a-z]+\s[A-Z]+|"+zho+"+)")
drivers_sn_time = re.compile("([A-Z][a-z]+\s[A-Z]+\s+\d+[.]+\d+|"+zho+"+\s+\d+[.]+\d+|"+dev+"+\s+\d+[.]+\d+)")
s_cond =  re.compile("\s+\d+\s+")
frase = '1 16 ZHOU Guanyu 26.740 14 Fernando ALONSO 17.753 16 Nyck DE VRIES 33.342'
b = 'paco'


if  s_cond.search(frase) != None :
    splited = re.split(s_cond,frase)

l = re.search(name, frase).group()
print(l)
x = re.findall(drivers_sn_time, frase)
print(x)

a = 'Hola'

t = '28.123'
print(t[3:])

def suma(n1,n2,n3=0,n4=2):
    s = n1 + n2 + n3+n4
    return s

print(suma(1,1,3))