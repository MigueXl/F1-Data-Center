import re
import os
import multidata

#regex to find numbers
num = re.compile("\d")
#regex to find drivers surname
zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'

class raceResult:
    def __init__(self, orderedList:list):
        self.result = self.getResult(orderedList)
    
    def getResult(self, orderedList):
            """Obtain the results obtained in the corresponding GP"""

            zho = 'ZHOU Guanyu'
            dev = 'Nyck DE VRIES'
            resPatern = re.compile('\d+\s+\d+\s+('+dev+'|'+zho+'|[A-Z][a-z]+\s[A-Z]+)' )

            if os.path.exists('result.txt'):
                with open('result.txt', "r", encoding='utf-8') as invoice:
                    text = invoice.readlines()

                num = []
                driv = []

                result = []
                #Split text if enter occurs
                for row in text:
                    row = row.replace('\t', ' ')
                    if resPatern.search(row) != None:
                        todo = resPatern.search(row).group()
                        sp = todo.split()
                        num.append(int(sp[0]))
                        driv.append(sp[-1])
                
                for n in orderedList:
                    obj = False
                    for d in driv:
                        if d in n:
                            index = driv.index(d)
                            result.append(num[index])
                            obj = True

                    if not obj:
                        result.append('DNF')
                
                return result, orderedList

            else:
                return ['DNF' for _ in range(len(orderedList))], orderedList
                
        
       
     
