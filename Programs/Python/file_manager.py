import os
import shutil
import multidata
import re
import pyautogui
import time
from tqdm import tqdm

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

class faseRename:
    '''Renames every provisional clasification file into result.pdf'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.oldName = []
    
    def findResult(self,dirFiles):
        all = os.listdir(dirFiles)
        for f in all:
            if 'provisional' in f:
                os.chdir(dirFiles)
                self.oldName.append(f[:10])
                os.rename(f, 'result.pdf')
                #CREATE THE CORRESPONDING result.txt to insert the data
                open('result.txt','w+')
    
    def printMessage(self):
        text = ''
        for i in self.oldName:
            text += str(i) + ' file has been renamed in its appropiate format\n'
        print(text)

    def renameFile(self):
        all = os.listdir(self.path)
        for f in all:
            dirFiles = os.path.join(self.path,f)
            if os.path.isdir(dirFiles):                
                self.findResult(dirFiles)
        
        self.printMessage()

class fase3:
    '''Create a copy of .txt if any information is readable regarding this folder'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.newFiles = []
        self.dir = []
    
    def whatFault(self,dirFiles):
        os.chdir(dirFiles)
        possible =  ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
        possiblePDF = ['_p1_','_p2_','_p3_','_q0_', '_r0_']
        new = []
        for f in os.listdir(dirFiles):
            #CHECK WHICH TEXT FILES ARE ALREADY INSIDE THE FILE
            for pos in possible:
                if pos in f:
                    index =  possible.index(pos)
                    possible.pop(index)
                    possiblePDF.pop(index)

        for f in os.listdir(dirFiles):
            for p in possiblePDF:
                if p in f: #EXISTS PDF CONTAINING THE CORRESPONDING SESSION
                    index = possiblePDF.index(p)

                    new.append(possible[index])
                    open(possible[index],'w+') #CREATES A TXT NAMED AS THE CORRESPONDING SESSION

                    possible.pop(index)
                    possiblePDF.pop(index)
        
        return new

    def printMessage(self):
        text = ''
        for f,dir in zip(self.newFiles,self.dir):
            text += str(f) + ' file has been created successuffly in '+str(dir)+'\n'
        print(text)

    def creatingFault(self):
        all = os.listdir(self.path)
        for f in all:
            dirFiles = os.path.join(self.path,f)
            if os.path.isdir(dirFiles):
                fault = self.whatFault(dirFiles)
                self.newFiles += fault
                for _ in range(len(fault)):
                    self.dir.append(dirFiles)
        
        self.printMessage()
        
class fase4:
    '''Copies the information from the pdf to the txt file '''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.newFiles = []
        self.dir = []
    
    def returnCorrectFiles(self, dirFiles: list, possible: list, possiblePDF: list, index: int):
        '''Returns the correct pdf regarding that document'''
        txt = possible[index]
        
        for f in os.listdir(dirFiles):
            if possiblePDF[index] in f:
                pdf = f
        
        return pdf, txt
    
    def returnPossPDF(self,posFixed):
        possible =  ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt",'result.txt']
        possiblePDF = ['_p1_','_p2_','_p3_','_q0_', '_r0_','result.pdf']

        PDFFixed = [possiblePDF[possible.index(i)] for i in posFixed if i in possible]
        
        return PDFFixed

    def whatFault(self,dirFiles):
        os.chdir(dirFiles)
        possible =  ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt",'result.txt']
        possiblePDF = ['_p1_','_p2_','_p3_','_q0_', '_r0_','result.pdf']
        new = []

        #AFTER THE CREATION OF EVERY TXT FILES; A DONE FILE WILL BE INCLUDED TO AVOID ENTERING AGAIN IN THE FOLDER
        if 'DONE.txt' in os.listdir(dirFiles):
            with open('DONE.txt', 'r') as check:
                result = check.readlines()    
                resCorrect = [ r.replace('\n','') for r in result]

            setA, setB = set(possible),  set(resCorrect)
            possible = list(setA-setB)
            possiblePDF = self.returnPossPDF(possible)

        for f in os.listdir(dirFiles):
            if f in possible:
                index = possible.index(f)
                new.append(possible[index])

                pdf, txt = self.returnCorrectFiles(dirFiles, possible, possiblePDF, index)

                #CHANGE THE WORKING DIRECTORY FOR BEING ABLE TO OPEN AND CLOSE FILES
                os.chdir(dirFiles)
                dir = os.getcwd()+ '\\'

                #OPEN THE PDF
                os.startfile(dir+pdf)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.hotkey('alt', 'f4')
                time.sleep(0.5)

                #OPEN THE TXT
                os.startfile(dir+txt)
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'e')
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('ctrl', 'g')
                pyautogui.hotkey('alt', 'f4')
                time.sleep(0.5)

                #APPEND NEW TO DONE.TXT 
                done = open('DONE.txt', 'a+')
                done.writelines(possible[index]+'\n')
                done.close()

                #REMOVE WHAT HAVE BEEN CREATED
                possible.pop(index)
                possiblePDF.pop(index)
        
        return new

    def printMessage(self):
        text = ''
        for f,dir in zip(self.newFiles,self.dir):
            text += str(f) + ' file has been updated successuffly in '+str(dir)+'\n'
        print(text)

    def generateFiles(self):
        all = os.listdir(self.path)
        for f in tqdm(all, desc =  str(self.year) + ' GPs PROGRESS BAR'):
            dirFiles = os.path.join(self.path,f)
            if os.path.isdir(dirFiles):
                fault = self.whatFault(dirFiles)
                self.newFiles += fault
                for _ in range(len(fault)):
                    self.dir.append(dirFiles)
        
        self.printMessage()
        
class faseCorrect:
    '''Create the folders in the corresponding year and introduce a false name_gp.txt file inside each of them'''
    def __init__(self, gps: list, year: int or str):
        self.gps = gps
        self.year = year    
        self.mainPath = "/Users/migue/Documents/F1 Data Center/"
        self.path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"
        self.newDirs = []
    
    def modifyGP(self,dirFiles):
        os.chdir(dirFiles)
        interest = ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
        totFiles = os.listdir(dirFiles)
        #CHECK THAT NAME_GP.TXT HAS NOT BEEN RENAMED EARLIER
        if 'DONE.txt' in totFiles:
            with open('DONE.txt', 'r') as check:
                result = check.readlines()    
                resCorrect = [ r.replace('\n','') for r in result]
                if 'name_gp.txt' in resCorrect:
                    return #BREAK THIS MODULE

        for f in totFiles:
            if os.path.exists(f) and f in interest:
                txt = open(f,'r', encoding='utf-8')
                all = txt.readlines()
                correctName = all[-2] + ' -' #PENULTIMA LINEA 
                correctName = correctName.replace('\n','')
                txt.close() #CLOSE THE FILE, WE WILL NOT NEED IT ANY MORE

                with  open('name_gp.txt','w', encoding='utf-8') as nameGP:
                    nameGP.write(correctName)
                
                self.newDirs.append(dirFiles)

                #APPEND NEW TO DONE.TXT 
                with open('DONE.txt', 'a+') as done:
                    done.writelines('name_gp.txt'+'\n')
                break #WE DO NOT NEED TO ITERATE ANY MORE ON THE LOOP

    def printMessage(self):
        text = ''
        for i in self.newDirs:
            text += str(i) + ' directory has nameGP.txt fixed\n'
        print(text)
    
    def correctFile(self):
        totFiles = os.listdir(self.path)
        for f in totFiles:
            dirFiles = os.path.join(self.path,f)
            if os.path.isdir(dirFiles):                
                self.modifyGP(dirFiles)

        self.printMessage()


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
        possible = ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
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
        text = '\n\n\n'
        for f,dir in zip(self.fault,self.dir):
            text +=  str(f) + ' file is not in '+str(dir)+'\n'
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




class updateALL:
    '''Call this class and the F1 DATA CENTER will update until the last data version'''
    def __init__(self, years: list):
        #FASE 1: CREATION OF DIRECTORIES
        for y in years: 
            f1 = fase1(multidata.f1_calendar(y).calendar, y)
            f1.createFolder()
        
        #FASE CORRECT: CORRECT NAME_GP.TXT FILE
        for y in years: 
            fc = faseCorrect(multidata.f1_calendar(y).calendar, y)
            fc.correctFile()

        #FASE 2: APPEND FILES IN THE CORRESPONDING DIRECTORY
        for y in years: 
            f2 = fase2(multidata.f1_calendar(y).calendar, y)
            f2.addFile()

        #FASE 3: APPEND FILES IN THE CORRESPONDING DIRECTORY
        for y in years: 
            f3 = fase3(multidata.f1_calendar(y).calendar, y)
            f3.creatingFault()
        
        #FASE RENAME: RENAME INTO RESULT.PDF
        for y in years: 
            fr = faseRename(multidata.f1_calendar(y).calendar, y)
            fr.renameFile()

        #FASE 4: OBTAIN THE .TXT FILE WITH THE CORRECT INFORMATION INSIDE
        for y in tqdm(years, desc = 'Year Progress Bar'):
            f4 = fase4(multidata.f1_calendar(y).calendar, y)
            f4.generateFiles()

        #CHECK MISSING: WHICH FILES IS NOT IN EACH DIRECTORY
        for y in years: 
            chck = returnFault(multidata.f1_calendar(y).calendar, y)
            chck.lookingFault()



auto = False  #TO AVOID DOUBLE EXECUTION WHILE CSV GENERATES DATA 
#(USE BETTER CSV GENERATOR BECAUSE IT UPDATES THE CSV, BUT IF IT TAKES A LOT BECAUSE THE LECTURE OF THE .TXT, USE THIS FILE DIRECTLY)
if auto:
    def createListYear(inicio,final):
        return [y for y in range(inicio,final + 1)]

    upYears = createListYear(2018,2022)
    # upYears = ['TestYear']
    if upYears != ['TestYear']:
        correctYears = createListYear(2018,2021)
        for gY in correctYears:
            upYears.remove(gY)

    updateALL(upYears)