import gp, multidata, gp_txt
import csv
import drivers
import os
import time
from tqdm import tqdm
from file_manager import updateALL
from multidata import getWEATHER as weather

inicio = time.time()


def remove_duplicates(lista):
    new_lista = []
    for i in range(len(lista)):
        if lista[i] not in new_lista:
            new_lista.append(lista[i])
    return new_lista

##################################################################################
#Incidents
##################################################################################

def incident(driver,year,circuit,sesion):
    #Posible outputs: Yes, No

##################################################################################
#2021Season
##################################################################################

    if year == 2021:
        ric,nor,vet,lat,rai,maz,gas,per,alo,lec,STR, tsu, oco,ver,ham,msc,sai,rus,bot,gio,kub = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
        driv_list = ['Fernando ALONSO', 'Charles LECLERC', 'Lance STROLL', 'Yuki TSUNODA', 'Esteban OCON', 'Max VERSTAPPEN', 'Lewis HAMILTON', 'Mick SCHUMACHER', 'Carlos SAINZ', 'George RUSSELL', 'Valtteri BOTTAS', 'Antonio GIOVINAZZI', 'Robert KUBICA']       
        if driver == 'Daniel RICCIARDO':
            ric = True
        elif driver == 'Lando NORRIS':
            nor = True
        elif driver == 'Sebastian VETTEL':
            vet = True
        elif driver == 'Nicholas LATIFI':
            lat = True
        elif driver == 'Kimi RAIKKONEN':
            rai = True
        elif driver == 'Nikita MAZEPIN':
            maz = True
        elif driver == 'Pierre GASLY':
            gas = True
        elif driver == 'Sergio PEREZ':
            per = True
        elif driver == driv_list[0]:
            alo = True
        elif driver == driv_list[1]:
            lec = True
        elif driver == driv_list[2]:
            STR = True
        elif driver == driv_list[3]:
            tsu = True
        elif driver == driv_list[4]:
            oco = True
        elif driver == driv_list[5]:
            ver = True
        elif driver == driv_list[6]:
            ham = True
        elif driver == driv_list[7]:
            msc = True
        elif driver == driv_list[8]:
            sai = True
        elif driver == driv_list[9]:
            rus = True
        elif driver == driv_list[10]:
            bot = True
        elif driver == driv_list[11]:
            gio = True
        elif driver == driv_list[12]:
            kub = True
            
        if circuit == 'Bahrein':
            if sesion == 'fp2':
                if rai:
                    return 'Yes'
            elif sesion == 'race':
                if gas or maz or vet or oco:
                    return 'Yes'
        elif circuit == 'Imola':
            if sesion == 'fp1':
                if oco or maz or per:
                    return 'Yes'
            elif sesion == 'fp2':
                if lec:
                    return 'Yes'
            elif sesion == 'quali':
                if tsu:
                    return 'Yes'
            elif sesion == 'race':
                if bot or rus or msc or lat:
                    return 'Yes'
        elif circuit == 'Portugal':
            if sesion == 'race':
                if rai:
                    return 'Yes'
        elif circuit == 'Monaco':
            if sesion == 'fp1':
                if alo:
                    return 'Yes'
            elif sesion == 'fp3':
                if lat:
                    return 'Yes'
            elif sesion == 'quali':
                if lec or msc:
                    return 'Yes'
        elif circuit == 'Azerbaiyan':
            if sesion == 'fp1':
                if maz or ver:
                    return 'Yes'
            elif sesion == 'quali':
                if STR or gio or ric or tsu or sai:
                    return 'Yes'
            elif sesion == 'race':
                if STR or ver:
                    return 'Yes'
        elif circuit == 'Belgica':
            if sesion == 'fp1':
                if rai:
                    return 'Yes'
            elif sesion == 'fp2':
                if lec or ver:
                    return 'Yes'
            elif sesion == 'quali':
                if nor:
                    return 'Yes'
        elif circuit == 'Hungria':
            if sesion == 'fp1':
                if tsu or msc:
                    return 'Yes'
            elif sesion == 'quali':
                if  sai:
                    return 'Yes'
            elif sesion == 'race':
                if bot or ver or per or ric or STR or nor or lec or maz:
                    return 'Yes'
        elif circuit == 'Holanda':
            if sesion == 'fp3':
                if sai:
                    return 'Yes'
            elif sesion == 'quali':
                if rus or lat:
                    return 'Yes'
        elif circuit == 'Francia':
            if sesion == 'fp1':
                if vet:
                    return 'Yes'
            elif sesion == 'quali':
                if msc or tsu:
                    return 'Yes'
        elif circuit == 'Austria1':
            if sesion == 'race':
                if lec or gas:
                    return 'Yes'
        elif circuit == 'Austria2':
            if sesion == 'race':
                if oco or rai or vet:
                    return 'Yes'
        elif circuit == 'Italia':
            if sesion == 'race':
                if ver or ham or gio:
                    return 'Yes'
        elif circuit == 'Mexico':
            if sesion == 'fp1':
                if lec or per:
                    return 'Yes'
            elif sesion == 'quali':
                if STR or gio:
                    return 'Yes'
            elif sesion == 'race':
                if ric or bot or msc or tsu:
                    return 'Yes'
        elif circuit == 'Saudi':
            if sesion == 'fp2':
                if lec:
                    return 'Yes'
            elif sesion == 'quali':
                if sai or ver:
                    return 'Yes'
            elif sesion == 'race':
                if msc or per or vet or rai or tsu or rus or maz:
                    return 'Yes'
        elif circuit == 'Rusia':
            if sesion == 'quali':
                if gio:
                    return 'Yes'
            elif sesion == 'race':
                if STR:
                    return 'Yes'
        elif circuit == 'AbuDhabi':
            if sesion == 'fp2':
                if rai or lat:
                    return 'Yes'
            elif sesion == 'quali':
                if rai or lat:
                    return 'Yes'
        elif circuit == 'EEUU':
            if sesion == 'race':
                if STR or lat:
                    return 'Yes'
        elif circuit == 'Turquia':
            if sesion == 'race':
                if alo or msc:
                    return 'Yes'
        elif circuit == 'Brasil':
            if sesion == 'race':
                if nor or msc or tsu or STR:
                    return 'Yes'

##################################################################################
#2022Season
##################################################################################
            
    if year == 2022:
        ric,nor,vet,lat,maz,gas,per,alo,lec,STR, tsu, oco,ver,ham,msc,sai,rus,bot,alb,zho,kmag, gio = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False, False, False
        driv_list = ['Fernando ALONSO', 'Charles LECLERC', 'Lance STROLL', 'Yuki TSUNODA', 'Esteban OCON', 'Max VERSTAPPEN', 'Lewis HAMILTON', 'Mick SCHUMACHER', 'Carlos SAINZ', 'George RUSSELL', 'Valtteri BOTTAS', 'Antonio GIOVINAZZI', 'Robert KUBICA']       
        if driver == 'Daniel RICCIARDO':
            ric = True
        elif driver == 'Lando NORRIS':
            nor = True
        elif driver == 'Sebastian VETTEL':
            vet = True
        elif driver == 'Nicholas LATIFI':
            lat = True
        elif driver == 'Pierre GASLY':
            gas = True
        elif driver == 'Sergio PEREZ':
            per = True
        elif driver == driv_list[0]:
            alo = True
        elif driver == driv_list[1]:
            lec = True
        elif driver == driv_list[2]:
            STR = True
        elif driver == driv_list[3]:
            tsu = True
        elif driver == driv_list[4]:
            oco = True
        elif driver == driv_list[5]:
            ver = True
        elif driver == driv_list[6]:
            ham = True
        elif driver == driv_list[7]:
            msc = True
        elif driver == driv_list[8]:
            sai = True
        elif driver == driv_list[9]:
            rus = True
        elif driver == driv_list[10]:
            bot = True
        elif driver == 'Guanyu ZHOU':
            zho = True
        elif driver == 'Alexander ALBON': 
            alb = True
        elif driver == 'Antonio GIOVINAZZI': 
            gio = True
        elif driver == 'Kevin MAGNUSSEN':
            kmag = True
        
        elif circuit == 'Bahrein':
            if sesion == 'race':
                if msc or oco:
                    return 'Yes'
        
        elif circuit == 'Saudi':
            if sesion == 'quali':
                if lat or msc:
                    return 'Yes'
            elif sesion == 'race':
                if lat or alb or STR:
                    return 'Yes'
        
        elif circuit == 'Australia':
            if sesion == 'fp3':
                if vet or STR:
                    return 'Yes'
            elif sesion == 'quali':
                if lat or STR or alo:
                    return 'Yes'
            elif sesion == 'race':
                if vet or sai:
                    return 'Yes'
        
        elif circuit == 'Imola':
            if sesion == 'quali':
                if sai:
                    return 'Yes'
            elif sesion == 'race':
                if alo or sai or msc or ric or lec:
                    return 'Yes'
        
        elif circuit == 'Miami':
            if sesion == 'fp1':
                if bot:
                    return 'Yes'
            elif sesion == 'fp2':
                if sai:
                    return 'Yes'
        
        elif circuit == 'España':
            if sesion == 'race':
                if ver or sai or STR or gas:
                    return 'Yes'
        
        elif circuit == 'Monaco':
            if sesion == 'fp2':
                if ric:
                    return 'Yes'
            if sesion == 'quali':
                if sai or per or tsu:
                    return 'Yes'
            if sesion == 'race':
                if msc or STR or lat:
                    return 'Yes'
        
        elif circuit == 'Azerbaiyan':
            if sesion == 'fp2':
                if alb:
                    return 'Yes'
            if sesion == 'quali':
                if STR:
                    return 'Yes'
        
        elif circuit == 'Canada':
            if sesion == 'quali':
                if alb or per:
                    return 'Yes'
            if sesion == 'race':
                if tsu:
                    return 'Yes'
        
        elif circuit == 'GB':
            if sesion == 'fp1':
                if STR:
                    return 'Yes'
            if sesion == 'race':
                if rus or alb or zho or oco or tsu or gas or vet:
                    return 'Yes'
        
        elif circuit == 'Austria':
            if sesion == 'quali':
                if ham or rus:
                    return 'Yes'
            if sesion == 'race':
                if rus or per or vet or gas:
                    return 'Yes'
        
        elif circuit == 'Francia':
            if sesion == 'race':
                if lec or tsu or kmag or lat:
                    return 'Yes'

        elif circuit == 'Hungria':
            if sesion == 'fp3':
                if vet:
                    return 'Yes'
            if sesion == 'race':
                if ric or STR or kmag:
                    return 'Yes'

        elif circuit == 'Belgica':
            if sesion == 'fp3':
                if lec:
                    return 'Yes'
            if sesion == 'race':
                if alo or ham or bot or lat:
                    return 'Yes'
        
        elif circuit == 'Holanda':
            if sesion == 'quali':
                if per:
                    return 'Yes'
            if sesion == 'race':
                if kmag or sai or ham:
                    return 'Yes'
        
        elif circuit == 'Singapur':
            if sesion == 'quali':
                if per:
                    return 'Yes'
            if sesion == 'race':
                if kmag or tsu or ham or rus or msc or ver or lat or zho:
                    return 'Yes'
        
        elif circuit == 'Japon':
            if sesion == 'fp1':
                if msc:
                    return 'Yes'
            if sesion == 'race':
                if sai or gas or vet:
                    return 'Yes'
        
        elif circuit == 'EEUU':
            if sesion == 'fp1':
                if gio:
                    return 'Yes'
            if sesion == 'race':
                if STR or alo or bot or sai or rus:
                    return 'Yes'
        
        elif circuit == 'Mexico':
            if sesion == 'fp2':
                if lec:
                    return 'Yes'
            if sesion == 'race':
                if tsu or ric:
                    return 'Yes'
        elif circuit == 'Brasil':
            if sesion == 'fp2':
                if oco or alo:
                    return 'Yes'
            if sesion == 'race':
                if lec or nor or kmag or ric or ver or ham:
                    return 'Yes'

def getLongest(sesiones:list):
    lengths = []
    for l in sesiones:
        lengths.append(len(l))
    return  max(lengths)  

            
def getShortNames(teams):
    '''Return a shorter version of the name and regarding the final team is in the grid. 
    For example Renault became Alpine because in the grid they are called Alpine in the last year of the dataset
    '''
    for i,t in enumerate(teams):
        if 'McLaren' in t:
            teams[i] = 'McLaren'
        elif 'Force India' in t or 'Racing Point' in t or ('Aston Martin' in t and not 'Red Bull' in t):
            teams[i] = 'Aston Martin'
        elif 'Williams' in  t:
            teams[i] = 'Williams'
        elif 'Alfa Romeo' in  t:
            teams[i] = 'Alfa Romeo'
        elif 'Haas' in  t:
            teams[i] = 'Haas'
        elif 'Toro Rosso' in t or 'AlphaTauri' in t:
            teams[i] = 'AlphaTauri'
        elif 'Red Bull' in  t and not 'Toro Rosso' in t:
            teams[i] = 'Red Bull'
        elif 'Renault' in  t  or 'Alpine' in t:
            teams[i] = 'Alpine'
        elif 'Ferrari' in  t:
            teams[i] = 'Ferrari'
        elif 'Mercedes' in  t:
            teams[i] = 'Mercedes'
    
    return teams
        























################################## MAIN FUNCTION #################################

#DATA UPDATE

def createListYear(inicio,final):
    return [y for y in range(inicio,final + 1)]

upYears = createListYear(2018,2022)
# years = ['TestYear']
correctYears = createListYear(2018,2021)
for gY in correctYears:
    upYears.remove(gY)

updateALL(upYears)

time.sleep(0.5)


#### LISTAS ####
data = [['Driver', 'Team', 'Age', 'Year', 'Month', 'GP', 'GP_ID','fp1_quali_Pace', 'fp1_quali_Laps', 'fp1_race_Pace', 'fp1_race_Laps', 'fp1_fastest_lap', 'fp1_Weather', 'fp1_Incident', 'fp2_quali_Pace', 'fp2_quali_Laps', 'fp2_race_Pace', 'fp2_race_Laps', 'fp2_fastest_lap', 'fp2_Weather', 'fp2_Incident', 'fp3_quali_Pace', 'fp3_quali_Laps', 'fp3_race_Pace', 'fp3_race_Laps', 'fp3_fastest_lap', 'fp3_Weather', 'fp3_Incident', 'quali_Pace', 'quali_Laps', 'quali_fastest_lap', 'quali_Weather', 'quali_Incident', 'race_Pace', 'race_Laps', 'race_fastest_lap', 'race_Stops', 'race_Weather', 'race_Incident','race_Result']]
w_list = []

############ INPUT YEARS #############
year = createListYear(2018,2022)     #
######################################

##################################################################################
#Loops and .csv preparation
##################################################################################
def correctNames(orderedList:list, num_ord: list, previous_name: list, form: str):
    correctResult = []
    for n in orderedList:
        obj = False
        for d in previous_name:
            if d == n:
                index = previous_name.index(d)
                correctResult.append(num_ord[index])
                obj = True

        if not obj:
            if form == 'res':
                correctResult.append('DNF')
            else:
                correctResult.append(0)
    
    return correctResult


# for y in range(len(year)):
for y in tqdm(range(len(year)), desc = 'Year Progress Bar'):
    grand_prix = multidata.f1_calendar(year[y]).calendar

    # for j in range(len(grand_prix)): 
    for j in tqdm(range(len(grand_prix)), desc = 'GP ' + str(year[y]) +' Progress Bar'):
        print(grand_prix[j])
        path = "/Users/migue/Documents/F1 Data Center/"+str(year[y])+"/"+grand_prix[j]+"_"+str(year[y])
        os.chdir(path)
        
        sesiones = []
        p_sesion = ["fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
        
        for s in range(len(p_sesion)):
            path = "/Users/migue/Documents/F1 Data Center/"+str(year[y])+"/"+grand_prix[j]+"_"+str(year[y])+"/"+p_sesion[s]
            if os.path.exists(path):
                sesiones.append(p_sesion[s])
            else:
                sesiones.append("")

        datos = gp_txt.gp(sesiones, grand_prix)       

        names = []
        drivers_lista = []
        
        ses_Nlist = [datos.fp1_name,datos.fp2_name,datos.fp3_name,datos.quali_name,datos.race_name]
        r = getLongest(ses_Nlist)
        for i in range(r):
            if i < len(datos.fp1_name) and datos.fp1_name[i] not in drivers_lista and datos.fp1_name[i] != "NO DRIVER":
                names.append(datos.fp1_name[i])
            if i < len(datos.fp2_name) and  datos.fp2_name[i] not in drivers_lista and datos.fp2_name[i] != "NO DRIVER":
                names.append(datos.fp2_name[i])
            if i < len(datos.fp3_name) and datos.fp3_name[i] not in drivers_lista and datos.fp3_name[i] != "NO DRIVER":
                names.append(datos.fp3_name[i])
            if i < len(datos.quali_name) and datos.quali_name[i] not in drivers_lista and datos.quali_name[i] != "NO DRIVER":
                names.append(datos.quali_name[i])
            if i < len(datos.race_name) and datos.race_name[i] not in drivers_lista and datos.race_name[i] != "NO DRIVER": 
                names.append(datos.race_name[i])
            
            names = remove_duplicates(names)

        num_ord, previous_name = datos.race_result
        race_result = correctNames(names, num_ord, previous_name, 'res')
        stops, previous_name = datos.stops
        pitStops = correctNames(names, stops, previous_name, 'stops')

        #### FULL DNF RACE (OBIOUSLY BECAUSE IT IS WRONG) ####
        w = True
        for i in race_result:
            if i != 'DNF':
                w = False
        if w:
            w_list.append(grand_prix[j]+ '_' + str(year[y])+ '\n')
        
        ##################################################################################
        #DATA GENERATION
        ##################################################################################

        teams = multidata.f1_teams(names,year[y],grand_prix[j]).equipos
        teams = getShortNames(teams)
        age = multidata.driversAGE(names,year[y]).age
        month = multidata.raceMONTH(year[y], grand_prix).month

        ##################################################################################
        #DATA GENERATION
        ##################################################################################

                    
        for i in range(len(names)):
            if names[i] not in  datos.fp1_name:
                index_fp1 = 20
            else:
                index_fp1 = datos.fp1_name.index(names[i])
                    
            if names[i] not in  datos.fp2_name:
                index_fp2 = 20
            else:
                index_fp2 = datos.fp2_name.index(names[i])
                    
            if names[i] not in  datos.fp3_name:
                index_fp3 = 20
            else:
                index_fp3 = datos.fp3_name.index(names[i])
                    
            if names[i] not in  datos.quali_name:
                index_quali = 20
            else:
                index_quali = datos.quali_name.index(names[i])
                    
            if names[i] not in  datos.race_name:
                index_race = 20
            else:
                index_race = datos.race_name.index(names[i])
    
            drivers_lista.append(drivers.drivers(names[i], teams[i], age[i], grand_prix[j], datos.fp1[index_fp1],datos.fp2[index_fp2],datos.fp3[index_fp3],datos.quali[index_quali],datos.race[index_race],race_result[i],pitStops[i]))


        for i in range(len(drivers_lista)):
            fp1_inc = incident(drivers_lista[i].name,year[y],grand_prix[j],'fp1')
            if fp1_inc == None:
                fp1_inc = 'No'
            fp2_inc = incident(drivers_lista[i].name,year[y],grand_prix[j],'fp2')
            if fp2_inc == None:
                fp2_inc = 'No'
            fp3_inc = incident(drivers_lista[i].name,year[y],grand_prix[j],'fp3')
            if fp3_inc == None:
                fp3_inc = 'No'
            quali_inc = incident(drivers_lista[i].name,year[y],grand_prix[j],'quali')
            if quali_inc == None:
                quali_inc = 'No'
            race_inc = incident(drivers_lista[i].name,year[y],grand_prix[j],'race')
            if race_inc == None:
                race_inc = 'No'

            #DEBUGGING
            # os.chdir("/Users/migue/Documents/F1 Data Center/"+str(year[y])+"/")
            # with open('debug'+ grand_prix[j] + str(year[y])+'.csv','w+') as debug:
            #     debug.write(str(i) +'\n')
            #     # l = [drivers_lista[i].name,drivers_lista[i].team,drivers_lista[i].age,year[y],month[j],grand_prix[j],j,drivers_lista[i].fp1_quali_mean,drivers_lista[i].fp1_quali,drivers_lista[i].fp1_race_mean,drivers_lista[i].fp1_race,drivers_lista[i].fp1_fastest,weather(year[y],grand_prix[j],'fp1'),fp1_inc,drivers_lista[i].fp2_quali_mean,drivers_lista[i].fp2_quali,drivers_lista[i].fp2_race_mean,drivers_lista[i].fp2_race,drivers_lista[i].fp2_fastest,weather(year[y],grand_prix[j],'fp2'),fp2_inc,drivers_lista[i].fp3_quali_mean,drivers_lista[i].fp3_quali,drivers_lista[i].fp3_race_mean,drivers_lista[i].fp3_race,drivers_lista[i].fp3_fastest,weather(year[y],grand_prix[j],'fp3'),fp3_inc,drivers_lista[i].quali,drivers_lista[i].quali_laps,drivers_lista[i].quali_fastest,weather(year[y],grand_prix[j],'quali'),quali_inc,drivers_lista[i].race,drivers_lista[i].race_laps,drivers_lista[i].race_fastest,drivers_lista[i].race_stops,weather(year[y],grand_prix[j],'race'),race_inc]
            #     lred = [drivers_lista[i].age,year[y],month[j]]
            #     for i in lred:
            #         debug.write(str(i)+'\n')

            data.append([drivers_lista[i].name,drivers_lista[i].team,drivers_lista[i].age,year[y],month[j],grand_prix[j],j,drivers_lista[i].fp1_quali_mean,drivers_lista[i].fp1_quali,drivers_lista[i].fp1_race_mean,drivers_lista[i].fp1_race,drivers_lista[i].fp1_fastest,weather(year[y],grand_prix[j],'fp1').w,fp1_inc,drivers_lista[i].fp2_quali_mean,drivers_lista[i].fp2_quali,drivers_lista[i].fp2_race_mean,drivers_lista[i].fp2_race,drivers_lista[i].fp2_fastest,weather(year[y],grand_prix[j],'fp2').w,fp2_inc,drivers_lista[i].fp3_quali_mean,drivers_lista[i].fp3_quali,drivers_lista[i].fp3_race_mean,drivers_lista[i].fp3_race,drivers_lista[i].fp3_fastest,weather(year[y],grand_prix[j],'fp3').w,fp3_inc,drivers_lista[i].quali,drivers_lista[i].quali_laps,drivers_lista[i].quali_fastest,weather(year[y],grand_prix[j],'quali').w,quali_inc,drivers_lista[i].race,drivers_lista[i].race_laps,drivers_lista[i].race_fastest,drivers_lista[i].race_stops,weather(year[y],grand_prix[j],'race').w,race_inc,drivers_lista[i].raceResult])



### GENERATE THE WARNING FILE ###
warning = open('/Users/migue/Documents/F1 Data Center/'+'WARNING.txt','w+')
for w in w_list:
    warning.write(w)

#Generate all data availble from sesiones
#rows format: [['a','b'], ['c','d']]
#Return to directory where data.csv is:
path = "/Users/migue/Documents/F1 Data Center/Datos/"
os.chdir(path)

with open('data.csv','w+', newline= '') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(data)


