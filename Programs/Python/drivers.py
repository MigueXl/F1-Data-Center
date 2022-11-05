
class drivers:
    def __init__(self,name,team,age,gp,fp1,fp2,fp3,quali,race):
        self.name = name
        self.team = team
        self.age = age
        self.gp = gp
        self.fp1 = self.get_mean(fp1)
        self.fp2 = self.get_mean(fp2)
        self.fp3 = self.get_mean(fp3)
        self.quali = self.get_mean(quali)
        self.race = self.get_mean(race)
        if fp1[0] != 0:
            self.fp1_laps = len(fp1)
        else:
              self.fp1_laps = 0
             
        if fp2[0] != 0:
            self.fp2_laps = len(fp2)
        else:
              self.fp2_laps = 0
             
        if fp3[0] != 0:
            self.fp3_laps = len(fp3)
        else:
              self.fp3_laps = 0
             
        if quali[0] != 0:
            self.quali_laps = len(quali)
        else:
              self.quali_laps = 0
             
        if race[0] != 0:
            self.race_laps = len(race)
        else:
              self.race_laps = 0
        
        self.fp1_total = self.fp_quali_race(fp1)
        self.fp2_total = self.fp_quali_race(fp2)
        self.fp3_total = self.fp_quali_race(fp3)
        
        self.fp1_quali =  self.fp1_total[0]
        self.fp2_quali =  self.fp2_total[0]
        self.fp3_quali =  self.fp3_total[0]
 
        self.fp1_race = self.fp1_total[1]
        self.fp2_race = self.fp2_total[1]
        self.fp3_race = self.fp3_total[1]

        self.fp1_quali_mean =  self.fp1_total[2]
        self.fp2_quali_mean =  self.fp2_total[2]
        self.fp3_quali_mean =  self.fp3_total[2]
 
        self.fp1_race_mean = self.fp1_total[3]
        self.fp2_race_mean = self.fp2_total[3]
        self.fp3_race_mean = self.fp3_total[3]
        
        self.fp1_fastest = self.get_fastest(fp1)
        self.fp2_fastest = self.get_fastest(fp2)
        self.fp3_fastest = self.get_fastest(fp3)
        self.quali_fastest = self.get_fastest(quali)
        self.race_fastest = self.get_fastest(race)
        
        self.race_stops = 0
        
        
    def get_sec(self,lista):
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
    
    
    
    def get_mean(self,lista):
        lista = self.get_sec(lista)
        suma = 0
        if lista[0] != 0:
            for i in range(len(lista)):
                suma += lista[i]
            mean = int(suma/len(lista))
        else:
            mean = "NO TIME "
        return mean
    
    def get_time(self,milisec):
        mins, sec, mil = -1,-1,-1
        cond = False
        if milisec != "NO TIME ":
            mins = int(milisec/(60*1000))
            resto = milisec - mins*60*1000
            sec = int(resto/1000)
            mil = resto - sec*1000
            if sec < 10:
                sec = "0"+str(sec)
            if mil < 10:
                mil = "00"+str(mil)
                cond = True
            if not cond:
                if mil < 100:
                    mil = "0"+str(mil)
                    
            return str(mins)+":"+str(sec)+"."+str(mil)
        
        else:
            return "NO TIME "
    
    def get_fastest(self,lista):
        lista = self.get_sec(lista)
        fast = min(lista)
        return(fast)
        
        
    def fp_quali_race(self,lista):
        lista_sec = self.get_sec(lista)
        quali, race = [], []
        minim = min(lista_sec)
        if lista[0] != 0:
            for i in range(len(lista_sec)):
                x = int((lista_sec[i]*100)/minim)
                if x <= 102:
                    quali.append(lista[i])
                else:
                    race.append(lista[i])
                    
        quali_len = len(quali)
        race_len = len(race)
            
        if len(quali)== 0:
            quali.append(0)
        if len(race)== 0:
            race.append(0) 
        
        mean_quali = self.get_mean(quali)
        mean_race = self.get_mean(race)
            
        return quali_len, race_len, mean_quali, mean_race                

    
    def good_printing(self,text):
        l = len(text)
        for i in range(18-l):
            text += " "
        return text
    
    def printer(self,sesion):
        if sesion == "fp1":
                name = self.good_printing(self.name)
                if self.fp1_laps < 10:
                    text = name+ " "+self.get_time(self.fp1)+"       "+str(self.fp1_laps)+"            "+str(self.fp1_quali)+"           "+str(self.fp1_race)
                else:
                    text = name+ " "+self.get_time(self.fp1)+"       "+str(self.fp1_laps)+"           "+str(self.fp1_quali)+"           "+str(self.fp1_race)
        if sesion == "fp2":
                name = self.good_printing(self.name)
                if self.fp2_laps < 10:
                    text = name+ " "+self.get_time(self.fp2)+"       "+str(self.fp2_laps)+"            "+str(self.fp2_quali)+"           "+str(self.fp2_race)
                else:
                    text = name+ " "+self.get_time(self.fp2)+"       "+str(self.fp2_laps)+"           "+str(self.fp2_quali)+"           "+str(self.fp2_race)
        if sesion == "fp3":
                name = self.good_printing(self.name)
                if self.fp3_laps < 10:
                    text = name+ " "+self.get_time(self.fp3)+"       "+str(self.fp3_laps)+"            "+str(self.fp3_quali)+"           "+str(self.fp3_race)
                else:
                    text = name+ " "+self.get_time(self.fp3)+"       "+str(self.fp3_laps)+"           "+str(self.fp3_quali)+"           "+str(self.fp3_race)
        if sesion == "quali":
                name = self.good_printing(self.name)
                text = name+ " "+self.get_time(self.quali)+"       "+str(self.quali_laps)
        if sesion == "race":
                name = self.good_printing(self.name)
                text = name+ " "+self.get_time(self.race)+"       "+str(self.race_laps)

        return text
    
    def printer_detail(self,sesion):
        if sesion == "fp1":
                name = self.good_printing(self.name)
                if self.fp1_laps < 10:
                    text1 = name+ " "+self.get_time(self.fp1_quali_mean)+"       "+str(self.fp1_quali)
                else:
                    text1 = name+ " "+self.get_time(self.fp1_quali_mean)+"       "+str(self.fp1_quali)          
        if sesion == "fp2":
                name = self.good_printing(self.name)
                if self.fp2_laps < 10:
                    text1 = name+ " "+self.get_time(self.fp2_quali_mean)+"       "+str(self.fp2_quali)           
                else:
                    text1 = name+ " "+self.get_time(self.fp2_quali_mean)+"       "+str(self.fp2_quali)           
        if sesion == "fp3":
                name = self.good_printing(self.name)
                if self.fp3_laps < 10:
                    text1 = name+ " "+self.get_time(self.fp3_quali_mean)+"       "+str(self.fp3_quali)          
                else:
                    text1 = name+ " "+self.get_time(self.fp3_quali_mean)+"       "+str(self.fp3_quali)

        if sesion == "fp1":
                name = self.good_printing(self.name)
                if self.fp1_laps < 10:
                    text2 = name+ " "+self.get_time(self.fp1_race_mean)+"       "+str(self.fp1_race)
                else:
                    text2 = name+ " "+self.get_time(self.fp1_race_mean)+"       "+str(self.fp1_race)          
        if sesion == "fp2":
                name = self.good_printing(self.name)
                if self.fp2_laps < 10:
                    text2 = name+ " "+self.get_time(self.fp2_race_mean)+"       "+str(self.fp2_race)           
                else:
                    text2 = name+ " "+self.get_time(self.fp2_race_mean)+"       "+str(self.fp2_race)           
        if sesion == "fp3":
                name = self.good_printing(self.name)
                if self.fp3_laps < 10:
                    text2 = name+ " "+self.get_time(self.fp3_race_mean)+"       "+str(self.fp3_race)          
                else:
                    text2 = name+ " "+self.get_time(self.fp3_race_mean)+"       "+str(self.fp3_race)  
                    
        return text1, text2