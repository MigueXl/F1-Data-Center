import pdfplumber
import PyPDF2 as p2
import re
import os

# path = "/Users/migue/Documents/F1 Data Center/"+'2022'+"/"+'Australia'+"_"+'2022'
# os.chdir(path)

#regex to find numbers
num = re.compile("\d")
#regex to find drivers surname
zho = 'ZHOU Guanyu'
dev = 'Nyck DE VRIES'
drivers_sn_time = re.compile("([A-Z][a-z]+\s[A-Z]+\s+\d+[.]+\d+|"+zho+"+\s+\d+[.]+\d+|"+dev+"+\s+\d+[.]+\d+)")
name = re.compile("("+dev+"+|[A-Z][a-z]+\s[A-Z]+|"+zho+"+)")
time = re.compile('\d+[.]+\d+')

class sectors:
    def __init__(self):
        self.data = self.get_lists()
        self.ntime = self.get_time(self.data[1], self.data[2], self.data[3])
        self.order = self.order_lists(self.data[0],self.ntime)
        self.names = self.order[0]
        self.times = self.order[1]
    
    def driverAllSect(self, drivers_name, rows):
        s1,s2,s3 = [],[],[]
        for r in rows:
            if len(r)==3:
                s1.append(re.search(name, r[0]).group())
                s2.append(re.search(name, r[1]).group())
                s3.append(re.search(name, r[2]).group())
            else:
                for i in range(len(r)):
                    if i==0: s1.append(re.search(name, r[i]).group())
                    else: s2.append(re.search(name, r[i]).group())
        
        allDrivers = [d for d in drivers_name if d in s1 and d in s2 and d in s3]
        
        return allDrivers
    
    def get_lists(self):
            """Obtain times lists and drivers names in each season"""
             
            #For each sesion, 20 drivers name
            drivers_name = []
            s1 = []
            s2 = []
            s3 = []
            
            rows = []
                
            invoice = open('sector.pdf', "rb")
            pdfread = p2.PdfFileReader(invoice)
            a = pdfread.getNumPages()
                    
            text = [] #Text of each season separated by pages

            #Extract text from each page
            for i in range(a):
                with pdfplumber.open(invoice) as pdf:
                    page = pdf.pages[i]
                    text.append(page.extract_text())
            
            

            # #Split text if enter occurs
            for i in range(a):
                for row in text[i].split('\n'):
                #Obtain driver and its time from each row 
                    if  drivers_sn_time.search(row) != None:
                        drivers_name.append(re.search(name, row).group())
                        rows.append(re.findall(drivers_sn_time, row))
            
            drivers_name = self.driverAllSect(drivers_name, rows)
            for n in drivers_name:
                for row in rows:
                    #! COULD BE BUGS IN THE CASE OF S1 DOES NOT EXIST FOR ONE DRIVER AND S2 SLOWEST SECTOR IS DONE BY ANOTHER DRIVER
                    #TODO IN CASE THAT HAPPENS, FIX IT IN THE FUTURE (BECAUSE S1 MOVES TO THE LEFT AND THAT DRIVER WILL FIND 2 DIFFERENT S1 WHILE THE SECOND IS S2)
                    if len(row) ==3:                             
                        if n in row[0]:
                            s1.append(re.search(time, row[0]).group())
                        if n in row[1]:
                            s2.append(re.search(time, row[1]).group())
                        if n in row[2]:
                            s3.append(re.search(time, row[2]).group())      
                     
            return drivers_name, s1,s2,s3
        
    def get_time(self,s1,s2,s3):
        
        time = []
        s1 = self.get_mil(s1)
        s2 = self.get_mil(s2)
        s3 = self.get_mil(s3)
        
        for i in range(len(s1)):
            total = s1[i] + s2[i] + s3[i]
            time.append(total)
        return time
        
    def get_mil(self,lista):
        nlist = []
        for i in lista:
            mil = 0
            sec = i[0:2]
            mil += int(sec) * 1000
            tre = i[3:]
            mil += int(tre)
            nlist.append(mil)
        return nlist
    
    def order_lists(self,drivers,time):
        n_driv = []
        n_time = []
        for i in range(len(drivers)):
            minim = min(time)
            index = time.index(minim)
            driv = drivers.pop(index)
            t = time.pop(index)
            n_driv.append(driv)
            n_time.append(t)
        return n_driv, n_time

class teams:
    def __init__(self,teams,times):
        self.data = self.get_avg(teams,times) 
        self.order = sectors().order_lists(self.data[0],self.data[1])
        self.teams = self.order[0]
        self.teams_t = self.order[1]
    
    def get_avg(self,teams,times):
        equipos = []
        tiempos = []
        for i in teams:
            if i not in equipos:
                equipos.append(i)
        
        for t in equipos:
            total = 0
            app = 0
            while t in teams and len(times) > 0:
                app += 1
                index = teams.index(t)
                teams.pop(index)
                time = times.pop(index)
                total += time
            tiempos.append(int(total/app))
        
        return equipos, tiempos
        
       
     

# ideal = sectors()
# names = ideal.names
# times = ideal.times

# eq = multidata.f1_teams(names,2022).equipos

# equipos = teams(eq,times.copy())

