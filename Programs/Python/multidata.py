class f1_teams:
    def __init__(self,drivers,year,gp,sesion = ''):
        self.equipos = self.get_teams(drivers,year,gp, sesion)
    
    def get_teams(self,names, year, gp, sesion):
        teams = []
        ##################################################################################
        #2018Season
        ##################################################################################
        if year == 2018:
            for i in range(len(names)):
                if names[i]== 'Fernando ALONSO' or names[i] == 'Stoffel VANDOORNE' or names[i] == 'Lando NORRIS':
                    teams.append("McLaren F1 Team")
                elif names[i]== 'Sergio PEREZ' or names[i] == 'Esteban OCON' or names[i] == 'Nicholas LATIFI':
                    teams.append("Sahara Force India F1 Team")
                elif names[i]== 'Sergey SIROTKIN' or names[i] == 'Lance STROLL' or names[i] == 'Robert KUBICA':
                    teams.append("Williams Racing")
                elif names[i]== 'Marcus ERICSSON' or names[i] == 'Charles LECLERC' or names[i] == 'Antonio GIOVINAZZI':
                    teams.append("Alfa Romeo Sauber F1 Team")
                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN':
                    teams.append("Haas F1 Team")
                elif names[i]== 'Pierre GASLY' or names[i] == 'Brendon HARTLEY' or names[i] == 'Sean GELAEL':
                    teams.append("Red Bull Toro Rosso Honda")
                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Max VERSTAPPEN':
                    teams.append("Aston Martin Red Bull Racing")
                elif names[i]== 'Carlos SAINZ' or names[i] == 'Nico HULKENBERG' or names[i] == 'Artem MARKELOV':
                    teams.append("Renault Sport Formula One Team")
                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Kimi RAIKKONEN':
                    teams.append("Scuderia Ferrari")
                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    teams.append("Mercedes AMG Petronas Motorsport")
                else:
                    teams.append("NO TEAM")
        ##################################################################################
        #2019Season
        ##################################################################################
        elif year == 2019:
            for i in range(len(names)):
                gaslyTR, albonRB = True, True
                if gp in ['Australia','Bahrein','China','Azerbaiyan','España','Monaco','Canada','Francia','Austria','GB','Alemania','Hungria']:
                    gaslyTR, albonRB = False, False

                if names[i]== 'Carlos SAINZ' or names[i] == 'Lando NORRIS':
                    teams.append("McLaren F1 Team")
                elif names[i]== 'Sergio PEREZ' or names[i] == 'Lance STROLL':
                    teams.append("SportPesa Racing Point F1 Team ")
                elif names[i]== 'Robert KUBICA' or names[i] == 'George RUSSELL' or names[i] == 'Nicholas LATIFI':
                    teams.append(" ROKiT Williams Racing ")
                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI':
                    teams.append("Alfa Romeo Sauber F1 Team")
                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN':
                    teams.append("Haas F1 Team")
                elif (names[i] == 'Alexander ALBON' and not albonRB) or names[i] == 'Daniil KVYAT' or (names[i]== 'Pierre GASLY' and  gaslyTR) or names[i] == 'Naoki YAMAMOTO':
                    teams.append("Red Bull Toro Rosso Honda")
                elif (names[i]== 'Pierre GASLY' and not gaslyTR) or names[i] == 'Max VERSTAPPEN' or (names[i] == 'Alexander ALBON' and albonRB):
                    teams.append("Aston Martin Red Bull Racing")
                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Nico HULKENBERG':
                    teams.append("Renault F1 Team")
                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Charles LECLERC':
                    teams.append("Scuderia Ferrari")
                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    teams.append("Mercedes AMG Petronas Motorsport")
                else:
                    teams.append("NO TEAM")
        ##################################################################################
        #2020Season
        ##################################################################################
        elif year == 2020:
            for i in range(len(names)):
                rusMER =  False
                if gp == 'Sahkir':
                    rusMER = True

                if names[i]== 'Carlos SAINZ' or names[i] == 'Lando NORRIS':
                    teams.append("McLaren F1 Team")
                elif names[i]== 'Sergio PEREZ' or names[i] == 'Lance STROLL' or names[i] == 'Nico HULKENBERG' or names[i] == 'Mick SCHUMACHER':
                    teams.append("BWT Racing Point F1 Team")
                elif names[i]== 'Nicholas LATIFI' or names[i] == 'George RUSSELL' or names[i] == 'Jack AITKEN' or names[i] == 'Roy NISSANY':
                    teams.append("Williams Racing")
                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI' or names[i] == 'Robert KUBICA':
                    teams.append("Alfa Romeo Racing ORLEN")
                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN' or names[i] == 'Callum ILOTT' or names[i] == 'Pietro FITTIPALDI':
                    teams.append("Haas F1 Team")
                elif names[i] == 'Daniil KVYAT' or names[i] == 'Pierre GASLY':
                    teams.append("Scuderia AlphaTauri Honda")
                elif names[i] == 'Max VERSTAPPEN' or names[i] == 'Alexander ALBON':
                    teams.append("Aston Martin Red Bull Racing")
                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Esteban OCON':
                    teams.append("Renault DP World F1 Team")
                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Charles LECLERC':
                    teams.append("Scuderia Ferrari")
                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON' or (names[i] == 'George RUSSELL' and rusMER):
                    teams.append("Mercedes-AMG Petronas F1 Team")
                else:
                    teams.append("NO TEAM")
        ##################################################################################
        #2021Season
        ##################################################################################
        elif year == 2021:
            for i in range(len(names)):
                if names[i]== 'Daniel RICCIARDO' or names[i] == 'Lando NORRIS':
                    teams.append("McLaren F1 Team")
                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Lance STROLL':
                    teams.append("Aston Martin Cognizant F1 Team")
                elif names[i]== 'Nicholas LATIFI' or names[i] == 'Jack AITKEN'or names[i] == 'Roy NISSANY' or names[i] == 'George RUSSELL':
                    teams.append("Williams Racing")
                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI'or names[i] == 'Robert KUBICA'or names[i] == 'Callum ILOTT':
                    teams.append("Alfa Romeo Racing ORLEN")
                elif names[i]== 'Nikita MAZEPIN' or names[i] == 'Mick SCHUMACHER':
                    teams.append("Uralkali Haas F1 Team")
                elif names[i]== 'Pierre GASLY' or names[i] == 'Yuki TSUNODA':
                    teams.append("Scuderia AlphaTauri Honda")
                elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN':
                    teams.append("Red Bull Racing Honda")
                elif names[i]== 'Fernando ALONSO' or names[i] == 'Esteban OCON'or names[i] == 'Guanyu ZHOU':
                    teams.append("Alpine F1 Team")
                elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ':
                    teams.append("Scuderia Ferrari Mission Winnow")
                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    teams.append("Mercedes-AMG Petronas F1 Team")
                else:
                    teams.append("NO TEAM")

        ##################################################################################
        #2022Season
        ##################################################################################

        elif year == 2022 or year == 'TestYear':
            for i in range(len(names)):
                vries_m, vries_w, vries_am = False, False, False
                if gp == 'Francia' or 'Mexico':
                    vries_m = True
                elif gp == 'Italia' and sesion == 'fp1':
                    vries_am = True
                else:
                    vries_w = True
                        
                if names[i]== 'Daniel RICCIARDO' or names[i] == 'Lando NORRIS' or names[i] == 'Alex PALOU':
                    teams.append("McLaren F1 Team")
                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Lance STROLL' or names[i] == 'Nico HULKENBERG' or (names[i] == 'Nyck VRIES' and vries_am):
                    teams.append("Aston Martin Cognizant F1 Team")
                elif names[i]== 'Nicholas LATIFI' or names[i] == 'Jack AITKEN'or names[i] == 'Roy NISSANY' or names[i] == 'Alexander ALBON' or (names[i] == 'Nyck VRIES' and vries_w) or names[i] == 'Logan SARGEANT':
                    teams.append("Williams Racing")
                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Robert KUBICA'or names[i] == 'Callum ILOTT'or names[i] == 'ZHOU Guanyu' or names[i] == 'Guanyu ZHOU' or names[i] == 'Theo POURCHAIRE':
                    teams.append('Alfa Romeo F1 Team ORLEN')
                elif names[i]== 'Kevin MAGNUSSEN' or names[i] == 'Mick SCHUMACHER' or names[i] == 'Antonio GIOVINAZZI' or names[i] =='Pietro FITTIPALDI':
                    teams.append("Haas F1 Team")
                elif names[i]== 'Pierre GASLY' or names[i] == 'Yuki TSUNODA' or names[i] == 'Liam LAWSON':
                    teams.append("Scuderia AlphaTauri")
                elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN' or names[i] == 'Juri VIPS':
                    teams.append("Oracle Red Bull Racing")
                elif names[i]== 'Fernando ALONSO' or names[i] == 'Esteban OCON' or names[i] == 'Jack DOOHAN':
                    teams.append("BWT Alpine F1 Team")
                elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ' or names[i] == 'Robert SHWARTZMAN':
                    teams.append("Scuderia Ferrari")
                elif names[i]== 'George RUSSELL' or names[i] == 'Lewis HAMILTON' or (names[i] == 'Nyck VRIES' and vries_m):
                    teams.append("Mercedes-AMG Petronas F1 Team")
                else:
                    teams.append("NO TEAM")
        
        else: 
            raise NameError('The year introduced is not correct')
        
        return teams

class f1_calendar:

    def __init__(self,year):
        self.calendar = self.getCalendar(year)
    
    def getCalendar(self,year):
        '''Returns a list with all the gps calendar'''
        if year == 'TestYear':
            calendar = ['Austria1','Austria2','Japon', 'JaponTxt'] #'Austria1','Austria2',
        elif year == 2018:
            calendar = ['Australia','Bahrein','China','Azerbaiyan','España','Monaco','Canada','Francia','Austria','GB','Alemania','Hungria','Belgica','Italia','Singapur','Rusia','Japon','EEUU','Mexico','Brasil','AbuDhabi']
        elif year == 2019:
            calendar = ['Australia','Bahrein','China','Azerbaiyan','España','Monaco','Canada','Francia','Austria','GB','Alemania','Hungria','Belgica','Italia','Singapur','Rusia','Japon','Mexico','EEUU','Brasil','AbuDhabi']
        elif year == 2020:
            calendar = ['Austria1','Austria2','Hungria','GB1','GB2','España','Belgica','Italia','Mugello','Rusia','Alemania','Portugal','Imola','Turquia','Bahrein1','Sahkir','AbuDhabi']
        elif year == 2021:
            calendar = ['Bahrein', 'Imola', 'Portugal', 'España', 'Monaco', 'Azerbaiyan','Francia', 'Austria1', 'Austria2',  'GB', 'Hungria', 'Belgica', 'Holanda', 'Italia', 'Rusia', 'Turquia','EEUU', 'Mexico', 'Brasil', 'Qatar', 'Saudi',  'AbuDhabi']
        elif year == 2022:
            calendar = ['Bahrein', 'Saudi', 'Australia', 'Imola', 'Miami', 'España','Monaco','Azerbaiyan','Canada','GB','Austria','Francia','Hungria','Belgica','Holanda','Italia','Singapur','Japon','EEUU','Mexico','Brasil','AbuDhabi']
        else: 
            raise NameError('The year introduced is not correct')
        
        return calendar

class driversAGE:
    def __init__(self,names,year):
        self.age = self.get_age(names,year)

    def get_age(self, names, year):
        if year == 'TestYear': year = 2022 #TESTYEAR
        age = []
        for i in range(len(names)):
            if names[i]== 'Kimi RAIKKONEN':
                born = 1979
                age.append(year - born)
            elif names[i]== 'Fernando ALONSO':
                born = 1981
                age.append(year - born)
            elif names[i]== 'Robert KUBICA':
                born = 1984
                age.append(year - born)
            elif names[i]== 'Lewis HAMILTON':
                born = 1985
                age.append(year - born)
            elif names[i]== 'Romain GROSJEAN':
                born = 1986
                age.append(year - born)
            elif names[i]== 'Sebastian VETTEL' or names[i] == 'Nico HULKENBERG':
                born = 1987
                age.append(year - born)
            elif names[i]== 'Naoki YAMAMOTO':
                born = 1988
                age.append(year - born)
            elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Daniel RICCIARDO' or names[i] == 'Brendon HARTLEY':
                born = 1989
                age.append(year - born)
            elif names[i]== 'Sergio PEREZ' or names[i]== 'Marcus ERICSSON':
                born = 1990
                age.append(year - born)
            elif names[i]== 'Kevin MAGNUSSEN' or names[i] == 'Stoffel VANDOORNE':  	
                born = 1992
                age.append(year - born)
            elif names[i]== 'Antonio GIOVINAZZI':
                born = 1993
                age.append(year - born)
            elif names[i] == 'Roy NISSANY' or names[i] == 'Carlos SAINZ' or names[i] == 'Daniil KVYAT' or names[i] == 'Artem MARKELOV':
                born = 1994
                age.append(year - born)
            elif names[i]== 'Nicholas LATIFI' or names[i] == 'Jack AITKEN' or names[i] == 'Nyck VRIES' or names[i]== 'Sergey SIROTKIN':
                born = 1995
                age.append(year - born)
            elif names[i]== 'Pierre GASLY' or names[i] == 'Esteban OCON' or names[i] == 'Alexander ALBON' or names[i] == 'Pietro FITTIPALDI' or names[i] == 'Sean GELAEL':
                born = 1996
                age.append(year - born)
            elif names[i]== 'Charles LECLERC' or names[i] == 'Max VERSTAPPEN' or names[i] == 'Alex PALOU':
                born = 1997
                age.append(year - born)
            elif names[i]== 'Lance STROLL' or names[i] == 'George RUSSELL' or names[i] == 'Callum ILOTT':
                born = 1998
                age.append(year - born)
            elif names[i]== 'Nikita MAZEPIN' or names[i] == 'Mick SCHUMACHER'or names[i] == 'Guanyu ZHOU' or names[i]== 'Lando NORRIS' or names[i] == 'ZHOU Guanyu' or names[i]== 'Robert SHWARTZMAN':
                born = 1999
                age.append(year - born)
            elif names[i] == 'Yuki TSUNODA' or names[i] == 'Juri VIPS' or names[i] == 'Logan SARGEANT':
                born = 2000
                age.append(year - born)
            elif names[i] == 'Liam LAWSON':
                born = 2003
                age.append(year - born)
            elif names[i] == 'Theo POURCHAIRE' or names[i] == 'Jack DOOHAN':
                born = 2003
                age.append(year - born)
            else:
                age.append("NO AGE")
        
        return age

class raceMONTH:
    def __init__(self, year: int, grand_prix: list):
        self.month = self.get_month(year,grand_prix)

    def get_month(self, year, grand_prix):
        month = []
        ##################################################################################
        #2018Season
        ##################################################################################
        if year == 2018:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Australia':
                    month.append("MAR")
                elif grand_prix[i]== 'Bahrein' or grand_prix[i]== 'China' or grand_prix[i]== 'Azerbaiyan':
                    month.append("APR")
                elif grand_prix[i]== 'Monaco' or grand_prix[i] == 'España':
                    month.append("MAY")
                elif grand_prix[i]== 'Canada' or grand_prix[i] == 'Francia':
                    month.append("JUN")
                elif grand_prix[i]== 'Austria' or grand_prix[i] == 'GB' or grand_prix[i]== 'Alemania' or grand_prix[i] == 'Hungria':
                    month.append("JUL")
                elif  grand_prix[i] == 'Belgica':
                    month.append("AUG")
                elif grand_prix[i]== 'Singapur' or grand_prix[i] == 'Italia' or grand_prix[i] == 'Rusia':
                    month.append("SEP")
                elif grand_prix[i]== 'Japon' or grand_prix[i] == 'EEUU' or grand_prix[i] == 'Mexico':
                    month.append("OCT")
                elif grand_prix[i] == 'Brasil' or grand_prix[i] == 'AbuDhabi':
                    month.append("NOV")
                else:
                    month.append('NO MONTH')

        ##################################################################################
        #2019Season
        ##################################################################################
        if year == 2019:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Australia' or grand_prix[i]== 'Bahrein':
                    month.append("MAR")
                elif  grand_prix[i]== 'China' or grand_prix[i]== 'Azerbaiyan':
                    month.append("APR")
                elif grand_prix[i]== 'Monaco' or grand_prix[i] == 'España':
                    month.append("MAY")
                elif grand_prix[i]== 'Canada' or grand_prix[i] == 'Francia' or grand_prix[i]== 'Austria':
                    month.append("JUN")
                elif  grand_prix[i] == 'GB' or grand_prix[i]== 'Alemania':
                    month.append("JUL")
                elif grand_prix[i] == 'Hungria':
                    month.append("AUG")
                elif grand_prix[i] == 'Belgica' or grand_prix[i]== 'Singapur' or grand_prix[i] == 'Italia' or grand_prix[i] == 'Rusia':
                    month.append("SEP")
                elif grand_prix[i]== 'Japon'  or grand_prix[i] == 'Mexico':
                    month.append("OCT")
                elif grand_prix[i] == 'Brasil'  or grand_prix[i] == 'EEUU':
                    month.append("NOV")
                elif grand_prix[i] == 'AbuDhabi':
                    month.append("DEC")
                else:
                    month.append('NO MONTH')

        ##################################################################################
        #2020Season
        ##################################################################################
        if year == 2020:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Austria1' or grand_prix[i]== 'Austria2' or grand_prix[i]== 'Hungria':
                    month.append("JUL")
                elif grand_prix[i] == 'GB1' or grand_prix[i] == 'GB2' or grand_prix[i] == 'Belgica' or grand_prix[i] == 'España':
                    month.append("AUG")
                elif grand_prix[i]== 'Mugello' or grand_prix[i] == 'Italia' or grand_prix[i] == 'Rusia':
                    month.append("SEP")
                elif grand_prix[i]== 'Alemania' or grand_prix[i] == 'Portugal':
                    month.append("OCT")
                elif grand_prix[i]== 'Imola' or grand_prix[i] == 'Turquia' or grand_prix[i] == 'Bahrein1':
                    month.append("NOV")
                elif grand_prix[i]== 'Sahkir' or grand_prix[i] == 'AbuDhabi':
                    month.append("DEC")
                else:
                    month.append('NO MONTH')

        ##################################################################################
        #2021Season
        ##################################################################################
        if year == 2021:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Bahrein':
                    month.append("MAR")
                elif grand_prix[i]== 'Imola':
                    month.append("APR")
                elif grand_prix[i]== 'Portugal' or grand_prix[i] == 'España' or grand_prix[i] == 'Monaco':
                    month.append("MAY")
                elif grand_prix[i]== 'Azerbaiyan' or grand_prix[i] == 'Francia' or grand_prix[i] == 'Austria1':
                    month.append("JUN")
                elif grand_prix[i]== 'Austria2' or grand_prix[i] == 'GB':
                    month.append("JUL")
                elif grand_prix[i]== 'Hungria' or grand_prix[i] == 'Belgica':
                    month.append("AUG")
                elif grand_prix[i]== 'Holanda' or grand_prix[i] == 'Italia' or grand_prix[i] == 'Rusia':
                    month.append("SEP")
                elif grand_prix[i]== 'Turquia' or grand_prix[i] == 'EEUU':
                    month.append("OCT")
                elif grand_prix[i]== 'Mexico' or grand_prix[i] == 'Brasil' or grand_prix[i] == 'Qatar':
                    month.append("NOV")
                elif grand_prix[i]== 'Saudi' or grand_prix[i] == 'AbuDhabi':
                    month.append("DEC")
                else:
                    month.append('NO MONTH')

        ##################################################################################
        #2022Season
        ##################################################################################

        if year == 2022:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Bahrein' or  grand_prix[i]== 'Saudi':
                    month.append("MAR")
                elif grand_prix[i]== 'Imola' or grand_prix[i]== 'Australia':
                    month.append("APR")
                elif grand_prix[i]== 'Miami' or grand_prix[i] == 'España' or grand_prix[i] == 'Monaco':
                    month.append("MAY")
                elif grand_prix[i]== 'Azerbaiyan' or grand_prix[i] == 'Canada':
                    month.append("JUN")
                elif grand_prix[i]== 'Austria' or grand_prix[i] == 'GB' or grand_prix[i] == 'Francia' or grand_prix[i]== 'Hungria':
                    month.append("JUL")
                elif grand_prix[i] == 'Belgica':
                    month.append("AUG")
                elif grand_prix[i]== 'Holanda' or grand_prix[i] == 'Italia':
                    month.append("SEP")
                elif grand_prix[i]== 'Singapur' or grand_prix[i] == 'EEUU' or grand_prix[i] == 'Japon' or grand_prix[i]== 'Mexico':
                    month.append("OCT")
                elif grand_prix[i] == 'Brasil' or grand_prix[i] == 'AbuDhabi':
                    month.append("NOV")
                else:
                    month.append("NO MONTH")
        
        return month


class getWEATHER:
    def __init__(self, year: int, circuit: str, sesion: str):
        self.w = self.weather(year,circuit, sesion)

    def weather(self, year,circuit,sesion):
        '''Posible outputs: D(Dry), D/I(Mixed conditions), I(Inter), I/W(Mixed wet conditions), W(Full Wet)'''
        ##################################################################################
        #2018Season
        ##################################################################################
        if year == 2018:
            if circuit == 'Francia' and sesion == 'fp3':
                return 'D/I'
            elif circuit == 'Alemania' and sesion == 'fp3':
                    return 'W'
            elif circuit == 'Hungria' and  sesion == 'quali': 
                    return 'D/I'
            elif circuit == 'Belgica' and  sesion == 'quali': 
                    return 'D/I'
            elif circuit == 'EEUU' and (sesion == 'fp1' or sesion == 'fp2'): 
                    return 'I'    
            else:
                return 'D'
        ##################################################################################
        #2019Season
        ##################################################################################
        elif year == 2019:
            if circuit == 'Alemania' and sesion == 'race':
                return 'D/I'
            elif circuit == 'Brasil' and sesion == 'fp1':
                    return 'I/W'
            else:
                return 'D'
        ##################################################################################
        #2020Season
        ##################################################################################
        elif year == 2020:
            if circuit == 'Austria2' and sesion == 'quali':
                return 'W'
            elif circuit == 'Hungria' and (sesion == 'fp2' or sesion == 'race'):
                if sesion == 'fp2':
                    return 'W'
                elif sesion =='race':
                    return 'D/I'
            elif circuit == 'Turquia' and (sesion == 'fp1' or sesion == 'fp3' or sesion == 'quali' or sesion == 'race'): 
                if sesion == 'fp1':
                    return 'D/I'    
                elif sesion == 'fp3' or sesion == 'quali' or sesion == 'race':
                    return 'I/W'
            else:
                return 'D'
        ##################################################################################
        #2021Season
        ##################################################################################
        elif year == 2021:
            if circuit == 'Imola' and sesion == 'race':
                return 'D/I'
            elif circuit == 'Belgica' and (sesion == 'fp3' or sesion == 'quali'):
                if sesion == 'fp3':
                    return 'I'
                elif sesion =='quali':
                    return 'I/W'
            elif circuit == 'Rusia' and (sesion == 'race' or sesion == 'quali'): 
                    return 'D/I'
            elif circuit == 'Turquia' and (sesion == 'fp3' or sesion == 'race'): 
                    return 'I'    
            else:
                return 'D'
        
        ##################################################################################
        #2022Season
        ##################################################################################    
        elif year == 2022:
            if circuit == 'Imola' and (sesion == 'fp1' or sesion == 'quali' or sesion == 'race'):
                if sesion == 'fp1':
                    return 'I/W'
                elif sesion =='quali' or 'race':
                    return 'D/I'
            if circuit == 'Monaco' and sesion == 'race':
                return 'D/I'
            if circuit == 'Canada' and (sesion == 'fp3' or sesion == 'quali'):
                return 'I/W'
            if circuit == 'GB' and (sesion == 'fp1' or sesion == 'quali'):
                return 'I'
            if circuit == 'Hungria' and (sesion == 'fp3' or sesion == 'quali'):
                if sesion == 'fp3':
                    return 'I/W'
                elif sesion == 'quali':
                    return 'D/I'
            if circuit == 'Singapur' and (sesion == 'fp3' or sesion == 'quali'):
                if sesion == 'fp3':
                    return 'I'
                elif sesion == 'quali':
                    return 'D/I'
            if circuit == 'Japon' and (sesion == 'fp1' or sesion == 'fp2' or sesion == 'race'):
                if sesion == 'fp2':
                    return 'I'
                elif sesion == 'fp1' or sesion == 'race':
                    return 'I/W'
            if circuit == 'Brasil' and sesion == 'quali':
                return 'D/I'
            else:
                return 'D'
        
        else:
            return 'D'