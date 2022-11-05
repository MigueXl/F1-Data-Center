import os
import shutil
import multidata
import re

class fase1:
    '''Create the folders in the corresponding year and introduce a false namegp.txt file inside each of them'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.mainPath = "/Users/migue/Documents/F1 Data Center/"
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.newDirs = []
    
    def getDirPath(self,gp):
        return self.path+"/"+gp+"_"+str(self.year)
    
    def printMessage(self):
        text = ''
        for i in self.newDirs:
            text += str(i) + ' directory has been created\n'
        print(text)
    
    def createFolder(self):
        for i in self.gps:
            os.chdir(self.path) #This is the directory where we have to update the files and folders
            if not os.path.exists(self.getDirPath(i)):
                nPath = str(i)+'_'+str(self.year)
                os.mkdir(self.path + nPath) #Create the new directory
                self.newDirs.append(nPath)

                #Append name_gp to each new directory
                src = os.path.join(self.mainPath, 'name_gp.txt') # origen
                dst = os.path.join(self.path + nPath, 'name_gp.txt') # destino
                shutil.copy(src, dst)

        self.printMessage()


class fase2:
    '''Introduce each file in its respective directory'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.fileAdd = []
    
    def findDir(self,file_name):
        patern = re.compile('_\d+_')
        number_rare = patern.findall(file_name)[0]
        #Remove '_'
        number = int(re.sub('_','',number_rare))
        return self.path + str(self.gps[number-1]) +'_'+str(self.year)
    
    def printMessage(self):
        text = ''
        for i in self.fileAdd:
            text += str(i) + ' file has been appended propertly\n'
        print(text)

    def addFile(self):
        totFiles = os.listdir(self.path)
        for f in totFiles:
            if os.path.isfile(os.path.join(self.path, f)) and f != 'name_gp.txt':
                righdir = self.findDir(f)
                #Append the file to the corresponding directory
                src = os.path.join(self.path, f) # origen
                dst = os.path.join(righdir, f) # destino
                shutil.move(src, dst)
                self.fileAdd.append(f[:10])
        
        self.printMessage()

class fase3:
    '''Obtain a readable file by main_program'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.fileAdd = []

class returnFault:
    '''Will return every file which fault in each directory'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.fault = []
        self.dir = []
    
    def removeBad(self,format: str, l: list):
        goodList = l.copy()
        for f in l:
            if format in f:
                goodList.remove(f)

        return goodList
    
    def whatFault(self,dirFiles):
        pdf = False
        possible = ["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf","fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
        sesionFiles = os.listdir(dirFiles)
        for f in sesionFiles:
            if f in possible:
                possible.remove(f)
                if '.pdf' in f:
                    pdf = True

        if pdf:
            return self.removeBad('.txt',possible)
        else:
            return self.removeBad('.pdf',possible)

    
    def printMessage(self):
        text = ''
        for f,dir in zip(self.fault,self.dir):
            text += str(f) + ' file is not in '+str(dir)+'\n'
        print(text)

    def lookingFault(self):
        all = os.listdir(self.path)
        for f in all:
            dirFiles = os.path.join(self.path,f)
            if os.path.isdir(dirFiles):
                fault = self.whatFault(dirFiles)
                self.fault += fault
                for _ in range(len(fault)):
                    self.dir.append(dirFiles)
        
        self.printMessage()





def createListYear(inicio,final):
    return [y for y in range(inicio,final + 1)]

years = createListYear(2018,2022)
# years = ['TestYear']
correctYears = [2021]
for gY in correctYears:
    years.remove(gY)

#FASE 1: CREATION OF DIRECTORIES
for y in years: 
    f1 = fase1(multidata.f1_calendar(y).calendar, y)
    f1.createFolder()

#FASE 2: APPEND FILES IN THE CORRESPONDING DIRECTORY
for y in years: 
    f2 = fase2(multidata.f1_calendar(y).calendar, y)
    f2.addFile()

#FASE 3: APPEND FILES IN THE CORRESPONDING DIRECTORY
for y in years: 
    f3 = fase3(multidata.f1_calendar(y).calendar, y)

#CHECK MISSING: WHICH FILES IS NOT IN EACH DIRECTORY
for y in years: 
    chck = returnFault(multidata.f1_calendar(y).calendar, y)
    chck.lookingFault()