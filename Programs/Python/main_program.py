import gp, gp_txt
import drivers
import teams as equipo
import re
import os
import sectors
import multidata

grand_prix = "Japon"
year = 2022

path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"+grand_prix+"_"+str(year)
os.chdir(path)

sesion = "race"
inicio = 1
final = None
laps = [inicio,final]

#n/s
mode = 'n'

#TO PRINT 
ngp = open("name_gp.txt", "r")
name_gp  = ngp.read()

#ESPAÑA
name_gp = re.sub("Ã‘","Ñ",name_gp)

def max_5_sesions(sesions):
    pdf = False
    for i in sesions:
        if '.pdf' in i:
            pdf = True
    
    if pdf:
        sesions = sesions[0:5]
    else:
        sesions = sesions[5:]
    return sesions

if mode == 'n':
    sesiones = []
    p_sesion = ["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf","fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]
    for i in range(len(p_sesion)):
        path = "/Users/migue/Documents/F1 Data Center/"+str(year)+"/"+grand_prix+"_"+str(year)+"/"+p_sesion[i]
        if os.path.exists(path):
            sesiones.append(p_sesion[i])
        else:
            sesiones.append("")

    #Generate all data availble from sesiones
    sesiones = max_5_sesions(sesiones)
    if '.pdf' in sesiones[0]:
        datos = gp.gp(sesiones, grand_prix,laps)
    else:
        datos = gp_txt.gp(sesiones, grand_prix,laps)
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

    teams = multidata.f1_teams(names,year,grand_prix,sesion).equipos

    #Age needed but not relevant here
    age = []
    for i in range(len(names)):
        age.append(i)

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
            
        drivers_lista.append(drivers.drivers(names[i], teams[i], age[i], grand_prix, datos.fp1[index_fp1],datos.fp2[index_fp2],datos.fp3[index_fp3],datos.quali[index_quali],datos.race[index_race]))
        
        
    unique_teams = remove_duplicates(teams)

    for i in range(len(unique_teams)):
        fp1, fp2, fp3, quali, race = [], [], [], [], []
        fp1_laps, fp2_laps, fp3_laps, quali_laps, race_laps = [], [], [], [], []
        for j in range(len(drivers_lista)):
            if drivers_lista[j].team == unique_teams[i]:
                fp1.append(drivers_lista[j].fp1)
                fp2.append(drivers_lista[j].fp2)
                fp3.append(drivers_lista[j].fp3)
                quali.append(drivers_lista[j].quali)
                race.append(drivers_lista[j].race)
                fp1_laps.append(drivers_lista[j].fp1_laps)
                fp2_laps.append(drivers_lista[j].fp2_laps)
                fp3_laps.append(drivers_lista[j].fp3_laps)
                quali_laps.append(drivers_lista[j].quali_laps)
                race_laps.append(drivers_lista[j].race_laps)
        
                
        teams_lista.append(equipo.teams(unique_teams[i], fp1, fp2, fp3, quali, race, fp1_laps,fp2_laps,fp3_laps,quali_laps,race_laps))


    def order_grid(lista):
        posible, no_posible = [], []
        for i in range(5):
            posible.append([])
            no_posible.append([])
            
        for i in range(len(lista)):
            
            if lista[i].fp1 != 'NO TIME ':
                posible[0].append(lista[i])
            else: 
                no_posible[0].append(lista[i])
                
            if lista[i].fp2 != 'NO TIME ':
                posible[1].append(lista[i])
            else: 
                no_posible[1].append(lista[i])
                
            if lista[i].fp3 != 'NO TIME ':
                posible[2].append(lista[i])
            else: 
                no_posible[2].append(lista[i])
                
            if lista[i].quali != 'NO TIME ':
                posible[3].append(lista[i])
            else: 
                no_posible[3].append(lista[i])
                
            if lista[i].race != 'NO TIME ':
                posible[4].append(lista[i])
            else: 
                no_posible[4].append(lista[i])
        
        fp1 = order_list(posible[0],"fp1")
        fp2 = order_list(posible[1],"fp2")
        fp3 = order_list(posible[2],"fp3")
        quali = order_list(posible[3],"quali")
        race = order_list(posible[4],"race")
        
        fp1 += no_posible[0]
        fp2 += no_posible[1]
        fp3 += no_posible[2]
        quali += no_posible[3]
        race += no_posible[4]
        
        return fp1, fp2, fp3, quali, race
            
    def order_list(lista, sesion):
        order_lista = []
        new_lista = []
        final_list = []
        for i in range(len(lista)):
            if sesion == "fp1":
                order_lista.append(lista[i].fp1)
            if sesion == "fp2":
                order_lista.append(lista[i].fp2)
            if sesion == "fp3":
                order_lista.append(lista[i].fp3)
            if sesion == "quali":
                order_lista.append(lista[i].quali)
            if sesion == "race":
                order_lista.append(lista[i].race)
            
        while(len(order_lista)) != 0:
            minim = min(order_lista)
            index = order_lista.index(minim)
            order_lista.pop(index)
            new_lista.append(minim)
            
            
        while len(new_lista) != 0:
            j = -1
            while len(lista) != 0:
                j += 1
                if sesion == "fp1":
                    if new_lista[0] == lista[j].fp1:
                        final_list.append(lista[j])
                        new_lista.pop(0)
                        lista.pop(j)
                        break
                            
                if sesion == "fp2":
                    if new_lista[0] == lista[j].fp2:
                        final_list.append(lista[j])
                        new_lista.pop(0)
                        lista.pop(j)
                        break
                        
                if sesion == "fp3":
                    if new_lista[0] == lista[j].fp3:
                        final_list.append(lista[j])
                        new_lista.pop(0)
                        lista.pop(j)
                        break
                            
                if sesion == "quali":
                    if new_lista[0] == lista[j].quali:
                        final_list.append(lista[j])
                        new_lista.pop(0)
                        lista.pop(j)
                        break
                            
                if sesion == "race":
                    if new_lista[0] == lista[j].race:
                        final_list.append(lista[j])
                        new_lista.pop(0)
                        lista.pop(j)
                        break
            
        return final_list
                    

    orden_drivers = order_grid(drivers_lista)
    orden_teams = order_grid(teams_lista)

    def order_grid_detail(lista):
        posible, no_posible = [], []
        for i in range(6):
            posible.append([])
            no_posible.append([])
            
        for i in range(len(lista)):
            
            if lista[i].fp1_quali_mean != 'NO TIME ':
                posible[0].append(lista[i])
            else: 
                no_posible[0].append(lista[i])
                
            if lista[i].fp1_race_mean != 'NO TIME ':
                posible[1].append(lista[i])
            else: 
                no_posible[1].append(lista[i])
                
            if lista[i].fp2_quali_mean != 'NO TIME ':
                posible[2].append(lista[i])
            else: 
                no_posible[2].append(lista[i])
                
            if lista[i].fp2_race_mean != 'NO TIME ':
                posible[3].append(lista[i])
            else: 
                no_posible[3].append(lista[i])
                
            if lista[i].fp3_quali_mean != 'NO TIME ':
                posible[4].append(lista[i])
            else: 
                no_posible[4].append(lista[i])
            
            if lista[i].fp3_race_mean != 'NO TIME ':
                posible[5].append(lista[i])
            else: 
                no_posible[5].append(lista[i])
        
        fp1_quali = order_list_detail(posible[0],"fp1","quali")
        fp1_race = order_list_detail(posible[1],"fp1", "race")
        fp2_quali = order_list_detail(posible[2],"fp2", "quali")
        fp2_race = order_list_detail(posible[3],"fp2", "race")
        fp3_quali = order_list_detail(posible[4],"fp3", "quali")
        fp3_race = order_list_detail(posible[5],"fp3", "race")
        
        fp1_quali += no_posible[0]
        fp1_race += no_posible[1]
        fp2_quali += no_posible[2]
        fp2_race += no_posible[3]
        fp3_quali += no_posible[4]
        fp3_race += no_posible[5]
        
        return fp1_quali, fp1_race, fp2_quali, fp2_race, fp3_quali, fp3_race
            
    def order_list_detail(lista, sesion, detail):
        order_lista = []
        new_lista = []
        final_list = []
        if detail == "quali":
            for i in range(len(lista)):
                if sesion == "fp1":
                    order_lista.append(lista[i].fp1_quali_mean)
                if sesion == "fp2":
                    order_lista.append(lista[i].fp2_quali_mean)
                if sesion == "fp3":
                    order_lista.append(lista[i].fp3_quali_mean)
        else:
            for i in range(len(lista)):
                if sesion == "fp1":
                    order_lista.append(lista[i].fp1_race_mean)
                if sesion == "fp2":
                    order_lista.append(lista[i].fp2_race_mean)
                if sesion == "fp3":
                    order_lista.append(lista[i].fp3_race_mean)

            
        while(len(order_lista)) != 0:
            minim = min(order_lista)
            index = order_lista.index(minim)
            order_lista.pop(index)
            new_lista.append(minim)
            
        if detail == "quali":    
            while len(new_lista) != 0:
                j = -1
                while len(lista) != 0:
                    j += 1
                    if sesion == "fp1":
                        if new_lista[0] == lista[j].fp1_quali_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                                    
                    if sesion == "fp2":
                        if new_lista[0] == lista[j].fp2_quali_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                                
                    if sesion == "fp3":
                        if new_lista[0] == lista[j].fp3_quali_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                        
        else:     
            while len(new_lista) != 0:
                j = -1
                while len(lista) != 0:
                    j += 1
                    if sesion == "fp1":
                        if new_lista[0] == lista[j].fp1_race_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                                
                    if sesion == "fp2":
                        if new_lista[0] == lista[j].fp2_race_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                            
                    if sesion == "fp3":
                        if new_lista[0] == lista[j].fp3_race_mean:
                            final_list.append(lista[j])
                            new_lista.pop(0)
                            lista.pop(j)
                            break
                            
        return final_list

    orden_drivers_detail = order_grid_detail(drivers_lista)


    def print_out(name_gp,orden_drivers,orden_teams,sesion):
        header_d = "POS      DRIVER          TIME    TOTAL LAPS   QUALI LAPS   RACE LAPS"
        header_t = "POS             TEAM                  TIME    TOTAL LAPS"
        text = ""
        if sesion == "fp1":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_d + "\n"
            for i in range(len(orden_drivers[0])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[0][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[0][i].printer(sesion)+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_t + "\n"
            for i in range(len(orden_teams[0])):
                if i < 9:
                    text += str(i+1)+".  "+orden_teams[0][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_teams[0][i].printer(sesion)+ "\n"
        if sesion == "fp2":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_d + "\n"
            for i in range(len(orden_drivers[1])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[1][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[1][i].printer(sesion)+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_t + "\n"
            for i in range(len(orden_teams[1])):
                if i < 9:
                    text += str(i+1)+".  "+orden_teams[1][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_teams[1][i].printer(sesion)+ "\n"
        if sesion == "fp3":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_d + "\n"
            for i in range(len(orden_drivers[2])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[2][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[2][i].printer(sesion)+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_t + "\n"
            for i in range(len(orden_teams[2])):
                if i < 9:
                    text += str(i+1)+".  "+orden_teams[2][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_teams[2][i].printer(sesion)+ "\n"
        if sesion == "quali":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_d + "\n"
            for i in range(len(orden_drivers[3])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[3][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[3][i].printer(sesion)+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_t + "\n"
            for i in range(len(orden_teams[3])):
                if i < 9:
                    text += str(i+1)+".  "+orden_teams[3][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_teams[3][i].printer(sesion)+ "\n"
        if sesion == "race":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_d + "\n"
            for i in range(len(orden_drivers[4])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[4][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[4][i].printer(sesion)+ "\n"
            text += "------------------------------------------------------------------------"+"\n"
            text += header_t + "\n"
            for i in range(len(orden_teams[4])):
                if i < 9:
                    text += str(i+1)+".  "+orden_teams[4][i].printer(sesion)+ "\n"
                else:
                    text += str(i+1)+". "+orden_teams[4][i].printer(sesion)+ "\n"
            
        return text

    def printer_details(name_gp,orden_drivers,sesion):
        header_q = "POS      DRIVER          TIME    QUALI LAPS" 
        header_r = "POS      DRIVER          TIME    RACE LAPS"  
        text = ""
        if sesion == "fp1":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_q + "\n"
            for i in range(len(orden_drivers[0])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[0][i].printer_detail(sesion)[0]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[0][i].printer_detail(sesion)[0]+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_r + "\n"
            for i in range(len(orden_drivers[1])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[1][i].printer_detail(sesion)[1]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[1][i].printer_detail(sesion)[1]+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"

        if sesion == "fp2":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_q + "\n"
            for i in range(len(orden_drivers[2])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[2][i].printer_detail(sesion)[0]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[2][i].printer_detail(sesion)[0]+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_r + "\n"
            for i in range(len(orden_drivers[3])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[3][i].printer_detail(sesion)[1]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[3][i].printer_detail(sesion)[1]+ "\n"

        if sesion == "fp3":
            text += name_gp+" "+sesion.upper()+"\n"
            text += header_q + "\n"
            for i in range(len(orden_drivers[4])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[4][i].printer_detail(sesion)[0]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[4][i].printer_detail(sesion)[0]+ "\n"
            text += "--------------------------------------------------------------------------"+"\n"
            text += header_r + "\n"
            for i in range(len(orden_drivers[5])):
                if i < 9:
                    text += str(i+1)+".  "+orden_drivers[5][i].printer_detail(sesion)[1]+ "\n"
                else:
                    text += str(i+1)+". "+orden_drivers[5][i].printer_detail(sesion)[1]+ "\n"
            
        return text



    print(print_out(name_gp,orden_drivers,orden_teams,sesion))

    if sesion == "fp1" or sesion == "fp2" or sesion == "fp3":
        print(printer_details(name_gp,orden_drivers_detail,sesion))
        

    #PARA SACAR NOMBRE DE LOS PILOTOS
    # chuleta = []
    # for i in range(len(drivers_lista)):
    #     chuleta.append(drivers_lista[i].name)
    # print(chuleta)

elif mode == 's':

    ideal = sectors.sectors()
    names = ideal.names
    times = ideal.times

    teams = multidata.f1_teams(names,year,grand_prix,sesion).equipos

    equipos = sectors.teams(teams,times.copy())
    eq = equipos.teams
    eq_times = equipos.teams_t

    def good_printing(text,type):
        l = len(text)
        if type == 'd':
            for i in range(18-l):
                text += " "
        else:
            for i in range(31-l):
                text += " "
        return text
    
    def get_time(milisec):
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

    def printer_sect(names,times,eq,eq_times,sesion = 'Best Sectors'):
        header_d = "POS      DRIVER          TIME"
        header_t = "POS             TEAM                  TIME"
        text = name_gp+" "+sesion.upper()+"\n"
        text += header_d + "\n"
        for i in range(len(names)):
            name =  good_printing(names[i],'d')
            time = get_time(times[i])
            if i < 9:
                text += str(i+1)+".  "+name+ " "+str(time)+"\n"
            else:
                text += str(i+1)+". "+name+ " "+str(time)+"\n"
        text += "--------------------------------------------------------------------------"+"\n"
        text += header_t + "\n"
        for i in range(len(eq)):
            equipo =  good_printing(eq[i],'t')
            eq_time = get_time(eq_times[i])
            if i < 9:
                text += str(i+1)+".  "+equipo+ " "+str(eq_time)+"\n"
            else:
                text += str(i+1)+". "+equipo+ " "+str(eq_time)+"\n"
        
        return text
        
    print(printer_sect(names,times,eq,eq_times))