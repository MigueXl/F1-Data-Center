class teams:
        def __init__(self,name,fp1,fp2,fp3,quali,race,fp1_laps,fp2_laps,fp3_laps,quali_laps,race_laps):
            self.name = name
            self.fp1 = self.get_mean(fp1)
            self.fp2 = self.get_mean(fp2)
            self.fp3 = self.get_mean(fp3)
            self.quali = self.get_mean(quali)
            self.race = self.get_mean(race)
            self.fp1_laps = self.get_laps(fp1_laps)
            self.fp2_laps = self.get_laps(fp2_laps)
            self.fp3_laps = self.get_laps(fp3_laps)
            self.quali_laps = self.get_laps(quali_laps)
            self.race_laps = self.get_laps(race_laps)
            
        def get_mean(self,lista):
            suma = 0
            counter = 0
            for i in range(len(lista)):      
                if lista[i] != "NO TIME ":
                    suma += lista[i]
                    counter += 1
            if counter != 0:
                mean = int(suma/counter)
            else:
                mean = "NO TIME "
            return mean

        def get_laps(self,lista):
            suma = 0
            for i in range(len(lista)):
                suma += lista[i]
            return suma
        
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
        
        
        def good_printing(self,text, item_name: list):
            r = len(max(item_name, key = len))
            l = len(text)
            for i in range(r + 1 -l):
                text += " "
            return text
                        
        
        def printer(self,sesion, item_name: list):
            if sesion == "fp1":
                    name = self.good_printing(self.name, item_name)
                    text = name+ " "+self.get_time(self.fp1)+"       "+str(self.fp1_laps)
            if sesion == "fp2":
                    name = self.good_printing(self.name, item_name)
                    text = name+ " "+self.get_time(self.fp2)+"       "+str(self.fp2_laps)
            if sesion == "fp3":
                    name = self.good_printing(self.name, item_name)
                    text = name+ " "+self.get_time(self.fp3)+"       "+str(self.fp3_laps)
            if sesion == "quali":
                    name = self.good_printing(self.name, item_name)
                    text = name+ " "+self.get_time(self.quali)+"       "+str(self.quali_laps)
            if sesion == "race":
                    name = self.good_printing(self.name, item_name)
                    text = name+ " "+self.get_time(self.race)+"       "+str(self.race_laps)
        
            return text

