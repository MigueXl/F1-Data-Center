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
    def __init__(self, lista_sesiones,gp,laps=None):
        self.gp = gp
        self.laps = laps
        self.lista = self.get_lists(lista_sesiones)
        if laps == [None,None] or laps == None:
            self.interval = self.lista[0:5]
        else:
            self.interval = self.get_int(list(self.lista[0:5]),self.laps)
        self.correcto = self.out_format(self.interval)
        self.definitivo = self.out_of_time(self.correcto)
        self.fp1 = self.definitivo[0]                                                                   
        self.fp2 = self.definitivo[1]                                                                        
        self.fp3 = self.definitivo[2]
        self.quali = self.definitivo[3]
        self.race = self.definitivo[4]
        self.fp1_name = self.lista[5]                                                                   
        self.fp2_name = self.lista[6]                                                                        
        self.fp3_name = self.lista[7]
        self.quali_name = self.lista[8]
        self.race_name = self.lista[9]
        
    def get_lists(self, lista_sesiones):
            """Obtain times lists and drivers names in each season"""
            drivers_apellido = []
            
            #For each sesion, 20 drivers name
            drivers_name = []
            for _ in range(len(lista_sesiones)):
                drivers_name.append([])
            
            #1 time for each season               
            time = []
            for _ in range(len(lista_sesiones)):
                time.append([])
            
            #For each sesion, 20 drivers time (Each time is a list containing each time available)
            drivers = []
            for _ in range(len(lista_sesiones)):
                drivers.append([])
            
            for i in range(len(drivers)):
                for _ in range(20):
                    drivers[i].append([])
                
            for sesion in range(len(lista_sesiones)):
                #Important later this driv = -1
                driv = -1
                if lista_sesiones[sesion] != "":
                    invoice = open(lista_sesiones[sesion], "rb")
                    pdfread = p2.PdfFileReader(invoice)
                    a = pdfread.getNumPages()
                    
                    text = [] #Text of each season separated by pages

                    #Extract text from each page
                    for i in range(a):
                        with pdfplumber.open(invoice) as pdf:
                            page = pdf.pages[i]
                            text.append(page.extract_text())

                    #Split text if enter occurs
                    for i in range(a):
                        for row in text[i].split('\n'):
                            
                            if drivers_sn.search(row) != None:
                                todo = drivers_sn.search(row).group()
                                sp = todo.split()
                                if sp[-1] not in drivers_apellido:
                                    drivers_apellido.append(sp[-1])
                            
                            #Get numbers from each row 
                            if num.search(row) != None:
                                n = num.search(row).group()
                            else:
                                n = "0"
                            #If row starts with number, we split row if " " occurs but sentences stays in the same list. 
                            if row.startswith(n):
                                time[sesion].append(row.split())
                    
                    for j in range(len(time[sesion])):
                        #If the last element in the list(surname) is in drivers_apellido list, we append his name to drivers_name of each season
                        if time[sesion][j][-1] in drivers_apellido:
                            drivers_name[sesion].append(time[sesion][j][1]+" "+time[sesion][j][-1])
                            driv += 1  #We have find a driver, then we can to the next one
                        else:
                            #Here we add times to each driver
                            for z in range(len(time[sesion][j])):
                                if ":" in time[sesion][j][z]:
                                    if 'P' not in time[sesion][j]: 
                                        drivers[sesion][driv].append(time[sesion][j][z])
                                    else:
                                        pit_time = time[sesion][j][-1]
                                        drivers[sesion][driv].append(pit_time)

                
                #If lista_sesiones = "" (Does not exist)                    
                else:
                    drivers_name[sesion] = drivers_name[sesion-1].copy()
                    for i in range(len(drivers[sesion])):
                        drivers[sesion][i].append(0)
                    
                
            fp1 = drivers[0]
            fp1.append([0]) #Ghost driver
            fp2 = drivers[1]
            fp2.append([0]) #Ghost driver
            fp3 = drivers[2]
            fp3.append([0]) #Ghost driver
            quali = drivers[3]
            quali.append([0]) #Ghost driver
            race = drivers[4]
            race.append([0]) #Ghost driver
            
            fp1_name = drivers_name[0]
            fp1_name.append("NO DRIVER") #Ghost driver
            fp2_name = drivers_name[1]
            fp2_name.append("NO DRIVER") #Ghost driver
            fp3_name = drivers_name[2] 
            fp3_name.append("NO DRIVER") #Ghost driver
            quali_name = drivers_name[3] 
            quali_name.append("NO DRIVER") #Ghost driver
            race_name = drivers_name[4] 
            race_name.append("NO DRIVER") #Ghost driver
                        
            return(fp1,fp2,fp3,quali,race,fp1_name,fp2_name,fp3_name,quali_name,race_name)
        
    def get_sec(self,lista):
        """Convert x:yy:zzz to seconds"""
        sec_list = []
        if len(lista) > 0:
            if lista[0] != 0:
                for i in range(len(lista)):
                    suma = 0
                    mins = int(lista[i][0:1])*60*1000
                    sec = int(lista[i][2:4])*1000
                    mil = int(lista[i][5:8])
                    suma = mins + sec + mil
                    sec_list.append(suma)
            else:
                sec_list.append(0)
        else:
            sec_list.append(0)
            
        return(sec_list)

    def out_format(self,lista):
        """Remove those times that are out of format. Correct format: 'x:yy:zzz'"""
        new_lista=[]
        #We create 5x20 empty lists (sesionsxdrivers)
        for _ in range(len(lista)):
            new_lista.append([])
        for i in range(len(lista)):
            for _ in range(len(lista[i])):
                new_lista[i].append([])
        
        
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                for z in range(len(lista[i][j])):
                    #[i][j][z] represents each time
                    if lista[i][j][z] != 0:
                        #Remove those that are above 10 minutes because are out of format
                        if ":" in lista[i][j][z][0:2]:
                            new_lista[i][j].append(lista[i][j][z])
                    else:
                        new_lista[i][j].append(lista[i][j][z])
        return(new_lista)

    def get_int(self,lists,interval):
        '''Return the race list with the interval of laps selected'''
        race = lists.pop(4)
        new_race = []
        for i in range(len(race)):
            new_race.append([])
        for d in range(len(race)):
            begin,end = interval[0], interval[1]
            if end == None or end > len(race[d]):
                end = len(race[d])
            for l in range(begin-1,end):
                new_race[d].append(race[d][l])
        lists.append(new_race)
        return lists
                
                
            
    
    def out_of_time(self,lista):
        """Remove those values that are out of time. 102% in case of quali and 110% for the rest"""
        new_lista = []
        lista_time = []
        
        #We create 5x20 empty lists (sesionsxdrivers)
        for _ in range(len(lista)):
            new_lista.append([])
            lista_time.append([])
        for i in range(len(lista)):
            for _ in range(21):
                new_lista[i].append([])
                lista_time[i].append([]) 
    
        for i in range(len(lista)):
            for j in range(len(lista[i])):
                lista_time[i][j] = self.get_sec(lista[i][j])
        
        for sesion in range(len(lista_time)):  
                
                #When sesion is quali
                if sesion == 3:
                    for i in range(len(lista_time[sesion])):
                        if lista_time[sesion][i][0] != 0:
                            minim = min(lista_time[sesion][i])
                            maximo = int((102*minim)/100)
                            for j in range(len(lista_time[sesion][i])):
                                if lista_time[sesion][i][j] < maximo:
                                    new_lista[sesion][i].append(lista[sesion][i][j])
                        else:
                            new_lista[sesion][i].append(0)
                            
                else:
                    for i in range(len(lista_time[sesion])):
                        if lista_time[sesion][i][0] != 0:
                            minim = min(lista_time[sesion][i])
                            maximo = int((110*minim)/100)
                            for j in range(len(lista_time[sesion][i])):
                                if lista_time[sesion][i][j] < maximo:
                                    new_lista[sesion][i].append(lista[sesion][i][j])
                        else:
                            new_lista[sesion][i].append(0)
            
        return new_lista
        


#ONLY FOR TESTING

import os
path = "/Users/migue/Documents/F1 Data Center/2022/Francia_2022/"
os.chdir(path)

sesiones = []
p_sesion = ["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf"]
for i in range(len(p_sesion)):
    path = "/Users/migue/Documents/F1 Data Center/2022/Francia_2022/"+p_sesion[i]
    if os.path.exists(path):
        sesiones.append(p_sesion[i])
    else:
        sesiones.append("")
        
inicio = 60
final = None
laps = [inicio,final]

year,grand_prix = 2022,'Francia'
#Generate all data availble from sesiones
datos = gp(sesiones, grand_prix,laps)


names = []
teams = []
teams_lista = []
drivers_lista = []

#names contains name and surname for every driver that at least has participate at least in one season.
for i in range(len(datos.fp1_name)):
        if datos.fp1_name[i] not in drivers_lista and datos.fp1_name[i] != "NO DRIVER":
            names.append(datos.fp1_name[i])
        if i < len(datos.fp2_name):
            if datos.fp2_name[i] not in drivers_lista and datos.fp2_name[i] != "NO DRIVER":
                names.append(datos.fp2_name[i])
        if i < len(datos.fp3_name):
            if datos.fp3_name[i] not in drivers_lista and datos.fp3_name[i] != "NO DRIVER":
                names.append(datos.fp3_name[i])
        if i < len(datos.quali_name):
            if datos.quali_name[i] not in drivers_lista and datos.quali_name[i] != "NO DRIVER":
                names.append(datos.quali_name[i])
        if i < len(datos.race_name):
            if datos.race_name[i] not in drivers_lista and datos.race_name[i] != "NO DRIVER": 
                names.append(datos.race_name[i])

def remove_duplicates(lista):
        new_lista = []
        for i in range(len(lista)):
            if lista[i] not in new_lista:
                new_lista.append(lista[i])
        return new_lista

names = remove_duplicates(names)


#Depending on names list, add their team to another list ordered in the same way names list is

teams = multidata.f1_teams(names,year,grand_prix).equipos