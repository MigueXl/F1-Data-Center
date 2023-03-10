import numpy as np
import os
import re
from result import raceResult

class f1_teams:
    '''Returns a `List` containing every F1 Team corresponding to each driver and it's color if necessary.
    - drivers: List containing every F1 Driver
    - year: Integer corresponding to season's year
    - gp: String corresponding to the Grand Prix Name
    - sesion (Optional): String corresponding to the F1 Session
    '''
    def __init__(self,drivers,year,gp,sesion = ''):
        self.equipos = self.get_teams(drivers,year,gp, sesion)
        self.color = self.get_teams(drivers,year,gp, sesion, color = True)
    
    def get_teams(self,names, year, gp, sesion, color = False):
        teams = []
        colorList = []
        ##################################################################################
        #2018Season
        ##################################################################################
        if year == 2018:
            for i in range(len(names)):
                if names[i]== 'Fernando ALONSO' or names[i] == 'Stoffel VANDOORNE' or names[i] == 'Lando NORRIS':
                    if color: colorList.append('#fe8000')
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Esteban OCON' or names[i] == 'Nicholas LATIFI':
                    if color: colorList.append('#ee99c5')
                    teams.append("Sahara Force India F1 Team")

                elif names[i]== 'Sergey SIROTKIN' or names[i] == 'Lance STROLL' or names[i] == 'Robert KUBICA':
                    if color: colorList.append('#FFFFFF')
                    teams.append("Williams Racing")

                elif names[i]== 'Marcus ERICSSON' or names[i] == 'Charles LECLERC' or names[i] == 'Antonio GIOVINAZZI':
                    if color: colorList.append('#6b101b')
                    teams.append("Alfa Romeo Sauber F1 Team")

                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN':
                    if color: colorList.append('#5a5b60')
                    teams.append("Haas F1 Team")

                elif names[i]== 'Pierre GASLY' or names[i] == 'Brendon HARTLEY' or names[i] == 'Sean GELAEL':
                    if color: colorList.append('#3364b5')
                    teams.append("Red Bull Toro Rosso Honda")

                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Max VERSTAPPEN':
                    if color: colorList.append('#340db0')
                    teams.append("Aston Martin Red Bull Racing")

                elif names[i]== 'Carlos SAINZ' or names[i] == 'Nico HULKENBERG' or names[i] == 'Artem MARKELOV':
                    if color: colorList.append('#f4f237')
                    teams.append("Renault Sport Formula One Team")

                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Kimi RAIKKONEN':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes AMG Petronas Motorsport")

                else:
                    if color: colorList.append('#000000')
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
                    if color: colorList.append('#fe8000')
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Lance STROLL':
                    if color: colorList.append('#ee99c5')
                    teams.append("SportPesa Racing Point F1 Team ")

                elif names[i]== 'Robert KUBICA' or names[i] == 'George RUSSELL' or names[i] == 'Nicholas LATIFI':
                    if color: colorList.append('#feffff')
                    teams.append(" ROKiT Williams Racing ")

                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI':
                    if color: colorList.append('#6b101b')
                    teams.append("Alfa Romeo Sauber F1 Team")

                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN':
                    if color: colorList.append('#eed899')
                    teams.append("Haas F1 Team")

                elif (names[i] == 'Alexander ALBON' and not albonRB) or names[i] == 'Daniil KVYAT' or (names[i]== 'Pierre GASLY' and  gaslyTR) or names[i] == 'Naoki YAMAMOTO':
                    if color: colorList.append('#3364b5')
                    teams.append("Red Bull Toro Rosso Honda")

                elif (names[i]== 'Pierre GASLY' and not gaslyTR) or names[i] == 'Max VERSTAPPEN' or (names[i] == 'Alexander ALBON' and albonRB):
                    if color: colorList.append('#340db0')
                    teams.append("Aston Martin Red Bull Racing")

                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Nico HULKENBERG':
                    if color: colorList.append('#f4f237')
                    teams.append("Renault F1 Team")

                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Charles LECLERC':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes AMG Petronas Motorsport")

                else:
                    if color: colorList.append('#000000')
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
                    if color: colorList.append('#fe8000')                   
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Lance STROLL' or names[i] == 'Nico HULKENBERG' or names[i] == 'Mick SCHUMACHER':
                    if color: colorList.append('#ee99c5')
                    teams.append("BWT Racing Point F1 Team")

                elif names[i]== 'Nicholas LATIFI' or (names[i] == 'George RUSSELL' and not rusMER) or names[i] == 'Jack AITKEN' or names[i] == 'Roy NISSANY':
                    if color: colorList.append('#1071d1')
                    teams.append("Williams Racing")

                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI' or names[i] == 'Robert KUBICA':
                    if color: colorList.append('#6b101b')
                    teams.append("Alfa Romeo Racing ORLEN")

                elif names[i]== 'Romain GROSJEAN' or names[i] == 'Kevin MAGNUSSEN' or names[i] == 'Callum ILOTT' or names[i] == 'Pietro FITTIPALDI':
                    if color: colorList.append('#000000')
                    teams.append("Haas F1 Team")

                elif names[i] == 'Daniil KVYAT' or names[i] == 'Pierre GASLY':
                    if color: colorList.append('#5b5b64')
                    teams.append("Scuderia AlphaTauri Honda")

                elif names[i] == 'Max VERSTAPPEN' or names[i] == 'Alexander ALBON':
                    if color: colorList.append('#340db0')
                    teams.append("Aston Martin Red Bull Racing")

                elif names[i]== 'Daniel RICCIARDO' or names[i] == 'Esteban OCON':
                    if color: colorList.append('#f4f237')
                    teams.append("Renault DP World F1 Team")

                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Charles LECLERC':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON' or (names[i] == 'George RUSSELL' and rusMER):
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes-AMG Petronas F1 Team")

                else:
                    if color: colorList.append('#000000')
                    teams.append("NO TEAM")
        ##################################################################################
        #2021Season
        ##################################################################################
        elif year == 2021:
            for i in range(len(names)):
                if names[i]== 'Daniel RICCIARDO' or names[i] == 'Lando NORRIS':
                    if color: colorList.append('#fe8000')
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Lance STROLL':
                    if color: colorList.append('#185d5b')
                    teams.append("Aston Martin Cognizant F1 Team")

                elif names[i]== 'Nicholas LATIFI' or names[i] == 'Jack AITKEN'or names[i] == 'Roy NISSANY' or names[i] == 'George RUSSELL':
                    if color: colorList.append('#1e52b8')
                    teams.append("Williams Racing")

                elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI'or names[i] == 'Robert KUBICA'or names[i] == 'Callum ILOTT':
                    if color: colorList.append('#6b101b')
                    teams.append("Alfa Romeo Racing ORLEN")

                elif names[i]== 'Nikita MAZEPIN' or names[i] == 'Mick SCHUMACHER':
                    if color: colorList.append('#FFFFFF')
                    teams.append("Uralkali Haas F1 Team")

                elif names[i]== 'Pierre GASLY' or names[i] == 'Yuki TSUNODA':
                    if color: colorList.append('#2d3c4f')
                    teams.append("Scuderia AlphaTauri Honda")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN':
                    if color: colorList.append('#340db0')
                    teams.append("Red Bull Racing Honda")

                elif names[i]== 'Fernando ALONSO' or names[i] == 'Esteban OCON'or names[i] == 'Guanyu ZHOU':
                    if color: colorList.append('#2180c3')
                    teams.append("Alpine F1 Team")

                elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari Mission Winnow")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes-AMG Petronas F1 Team")

                else:
                    if color: colorList.append('#000000')
                    teams.append("NO TEAM")
        ##################################################################################
        #2022Season
        ##################################################################################
        elif year == 2022 or year == 'TestYear':
            for i in range(len(names)):
                vries_m, vries_w, vries_am = False, False, False
                lawson_rb = False
                if gp == 'Francia' or  gp == 'Mexico':
                    vries_m = True
                elif gp == 'Italia' and sesion == 'fp1':
                    vries_am = True
                else:
                    vries_w = True
                    
                if gp == 'AbuDhabi':
                    lawson_rb = True
                
                if names[i]== 'Daniel RICCIARDO' or names[i] == 'Lando NORRIS' or names[i] == 'Alex PALOU' or names[i] == "Patricio O'WARD":
                    if color: colorList.append('#fe8000')
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Sebastian VETTEL' or names[i] == 'Lance STROLL' or names[i] == 'Nico HULKENBERG' or (names[i] == 'Nyck VRIES' and vries_am) or names[i] == 'Felipe DRUGOVICH':
                    if color: colorList.append('#185d5b')
                    teams.append("Aston Martin Cognizant F1 Team")

                elif names[i]== 'Nicholas LATIFI' or names[i] == 'Jack AITKEN' or names[i] == 'Roy NISSANY' or names[i] == 'Alexander ALBON' or (names[i] == 'Nyck VRIES' and vries_w) or names[i] == 'Logan SARGEANT':
                    if color: colorList.append('#041e42')
                    teams.append("Williams Racing")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Robert KUBICA'or names[i] == 'Callum ILOTT'or names[i] == 'ZHOU Guanyu' or names[i] == 'Guanyu ZHOU' or names[i] == 'Theo POURCHAIRE':
                    if color: colorList.append('#6b101b')
                    teams.append('Alfa Romeo F1 Team ORLEN')

                elif names[i]== 'Kevin MAGNUSSEN' or names[i] == 'Mick SCHUMACHER' or names[i] == 'Antonio GIOVINAZZI' or names[i] =='Pietro FITTIPALDI':
                    if color: colorList.append('#FFFFFF')
                    teams.append("Haas F1 Team")

                elif names[i]== 'Pierre GASLY' or names[i] == 'Yuki TSUNODA' or (names[i] == 'Liam LAWSON' and not lawson_rb):
                    if color: colorList.append('#022947')
                    teams.append("Scuderia AlphaTauri")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN' or names[i] == 'Juri VIPS' or (names[i] == 'Liam LAWSON' and lawson_rb):
                    if color: colorList.append('#340db0')
                    teams.append("Oracle Red Bull Racing")

                elif names[i]== 'Fernando ALONSO' or names[i] == 'Esteban OCON' or names[i] == 'Jack DOOHAN':
                    if color: colorList.append('#2180c3')
                    teams.append("BWT Alpine F1 Team")

                elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ' or names[i] == 'Robert SHWARTZMAN':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari")

                elif names[i]== 'George RUSSELL' or names[i] == 'Lewis HAMILTON' or (names[i] == 'Nyck VRIES' and vries_m):
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes-AMG Petronas F1 Team")

                else:
                    if color: colorList.append('#000000')
                    teams.append("NO TEAM")    
        ##################################################################################
        #2023Season
        ##################################################################################
        elif year == 2023:
            for i in range(len(names)):
                if names[i]== 'Oscar PIASTRI' or names[i] == 'Lando NORRIS' or names[i] == 'Alex PALOU' or names[i] == "Patricio O'WARD":
                    if color: colorList.append('#fe8000')
                    teams.append("McLaren F1 Team")

                elif names[i]== 'Fernando ALONSO' or names[i] == 'Lance STROLL' or names[i] == 'Felipe DRUGOVICH':
                    if color: colorList.append('#185d5b')
                    teams.append("Aston Martin Cognizant F1 Team")

                elif names[i] == 'Jack AITKEN' or names[i] == 'Roy NISSANY' or names[i] == 'Alexander ALBON' or names[i] == 'Logan SARGEANT':
                    if color: colorList.append('#041e42')
                    teams.append("Williams Racing")

                elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Robert KUBICA' or names[i] == 'Callum ILOTT' or names[i] == 'ZHOU Guanyu' or names[i] == 'Guanyu ZHOU' or names[i] == 'Theo POURCHAIRE':
                    if color: colorList.append('#6b101b')
                    teams.append('Alfa Romeo F1 Team Stake')

                elif names[i]== 'Kevin MAGNUSSEN' or names[i] == 'Antonio GIOVINAZZI' or names[i] =='Pietro FITTIPALDI' or names[i] == 'Nico HULKENBERG':
                    if color: colorList.append('#f0eff2')
                    teams.append("MoneyGram Haas F1 Team")

                elif names[i] == 'Yuki TSUNODA' or names[i] == 'Liam LAWSON' or names[i] == 'Nyck VRIES' or names[i] == 'Nyck DE VRIES':
                    if color: colorList.append('#022947')
                    teams.append("Scuderia AlphaTauri")

                elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN':
                    if color: colorList.append('#340db0')
                    teams.append("Oracle Red Bull Racing")

                elif names[i]== 'Pierre GASLY' or names[i] == 'Esteban OCON' or names[i] == 'Jack DOOHAN':
                    if color: colorList.append('#2180c3')
                    teams.append("BWT Alpine F1 Team")

                elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ' or names[i] == 'Robert SHWARTZMAN':
                    if color: colorList.append('#cc0000')
                    teams.append("Scuderia Ferrari")

                elif names[i]== 'George RUSSELL' or names[i] == 'Lewis HAMILTON':
                    if color: colorList.append('#25b8a1')
                    teams.append("Mercedes-AMG Petronas F1 Team")

                else:
                    if color: colorList.append('#000000')
                    teams.append("NO TEAM")
        else: 
            raise NameError('The year introduced is not correct')
        
        if color: return colorList
        else: return teams

class numberToNames:
    """Tranforms Driver's Number into his corresponding Name.
    - year: Integer corresponding to season's year
    - number: String/Integer corresponding to Driver's Number
    """
    def __init__(self, year: int, number):
        self.name = self.get_names(year,number)

    def get_names(self, year: int, number):
        number = int(number)
        ##################################################################################
        #2020Season
        ##################################################################################
        if year == 2020:
            if number == 3: return 'Daniel RICCIARDO'              
            elif number == 4: return 'Lando NORRIS'             
            elif number == 5: return 'Sebastian VETTEL'             
            elif number == 6: return 'Nicholas LATIFI'               
            elif number == 7: return 'Kimi RAIKKONEN'               
            elif number == 8: return 'Romain GROSJEAN'               
            elif number == 10: return 'Pierre GASLY'               
            elif number == 11: return 'Sergio PEREZ'                
            elif number == 16: return 'Charles LECLERC'               
            elif number == 18: return 'Lance STROLL'                
            elif number == 20: return 'Kevin MAGNUSSEN'               
            elif number == 23: return 'Alexander ALBON'               
            elif number == 26: return 'Daniil KVYAT'               
            elif number == 31: return 'Esteban OCON'                
            elif number == 33: return 'Max VERSTAPPEN'               
            elif number == 40: return 'Roy NISSANY'                
            elif number == 44: return 'Lewis HAMILTON'               
            elif number == 55: return 'Carlos SAINZ'  
            elif number == 63: return 'George RUSSELL'             
            elif number == 77: return 'Valtteri BOTTAS'  
            elif number == 88: return 'Robert KUBICA'
            elif number == 99: return 'Antonio GIOVINAZZI'
            else:  raise NameError(f'Number {number} is not found for year {year}')
        ##################################################################################
        #2021Season
        ##################################################################################
        elif year == 2021:
            if number == 3: return 'Daniel RICCIARDO'              
            elif number == 4: return 'Lando NORRIS'             
            elif number == 5: return 'Sebastian VETTEL'             
            elif number == 6: return 'Nicholas LATIFI'               
            elif number == 7: return 'Kimi RAIKKONEN'               
            elif number == 8: return 'Romain GROSJEAN'  
            elif number == 9: return 'Nikita MAZEPIN'               
            elif number == 10: return 'Pierre GASLY'               
            elif number == 11: return 'Sergio PEREZ' 
            elif number == 14: return 'Fernando ALONSO'                               
            elif number == 16: return 'Charles LECLERC'               
            elif number == 18: return 'Lance STROLL'                
            elif number == 20: return 'Kevin MAGNUSSEN'   
            elif number == 22: return 'Yuki TSUNODA'                           
            elif number == 23: return 'Alexander ALBON'
            elif number == 24: return 'ZHOU Guanyu'                
            elif number == 26: return 'Daniil KVYAT'  
            elif number == 27: return 'Nico HULKENBERG'              
            elif number == 31: return 'Esteban OCON'                
            elif number == 33: return 'Max VERSTAPPEN'                              
            elif number == 44: return 'Lewis HAMILTON'   
            elif number == 45: return 'Roy NISSANY' 
            elif number == 47: return 'Mick SCHUMACHER'             
            elif number == 55: return 'Carlos SAINZ'   
            elif number == 63: return 'George RUSSELL'               
            elif number == 77: return 'Valtteri BOTTAS'  
            elif number == 88: return 'Robert KUBICA'
            elif number == 99: return 'Antonio GIOVINAZZI'
            else:  raise NameError(f'Number {number} is not found for year {year}')
        ##################################################################################
        #2022Season
        ##################################################################################
        elif year == 2022:
            if number == 1: return 'Max VERSTAPPEN'
            elif number == 3: return 'Daniel RICCIARDO'              
            elif number == 4: return 'Lando NORRIS'             
            elif number == 5: return 'Sebastian VETTEL'             
            elif number == 6: return 'Nicholas LATIFI'               
            elif number == 7: return 'Kimi RAIKKONEN'               
            elif number == 8: return 'Romain GROSJEAN'  
            elif number == 9: return 'Nikita MAZEPIN'               
            elif number == 10: return 'Pierre GASLY'               
            elif number == 11: return 'Sergio PEREZ' 
            elif number == 14: return 'Fernando ALONSO'                               
            elif number == 16: return 'Charles LECLERC'               
            elif number == 18: return 'Lance STROLL'                
            elif number == 20: return 'Kevin MAGNUSSEN'
            elif number == 21: return 'Nyck VRIES'    
            elif number == 22: return 'Yuki TSUNODA'                           
            elif number == 23: return 'Alexander ALBON'
            elif number == 24: return 'ZHOU Guanyu'                
            elif number == 26: return 'Daniil KVYAT'  
            elif number == 27: return 'Nico HULKENBERG'              
            elif number == 31: return 'Esteban OCON'                
            elif number == 33: return 'Max VERSTAPPEN'  
            elif number == 34: return 'Felipe DRUGOVICH'             
            elif number == 40: return 'Roy NISSANY'                
            elif number == 44: return 'Lewis HAMILTON'   
            elif number == 47: return 'Mick SCHUMACHER' 
            elif number == 51: return 'Pietro FITTIPALDI'            
            elif number == 55: return 'Carlos SAINZ'     
            elif number == 63: return 'George RUSSELL'             
            elif number == 77: return 'Valtteri BOTTAS'  
            elif number == 81: return 'Oscar PIASTRI'
            elif number == 88: return 'Robert KUBICA'
            elif number == 99: return 'Antonio GIOVINAZZI'
            else:  raise NameError(f'Number {number} is not found for year {year}')
        ##################################################################################
        #2023Season
        ##################################################################################
        elif year == 2023:
            if number == 1: return 'Max VERSTAPPEN'
            elif number == 2: return 'Logan SARGEANT'
            elif number == 3: return 'Daniel RICCIARDO'              
            elif number == 4: return 'Lando NORRIS'             
            elif number == 5: return 'Sebastian VETTEL'             
            elif number == 6: return 'Nicholas LATIFI'               
            elif number == 7: return 'Kimi RAIKKONEN'               
            elif number == 8: return 'Romain GROSJEAN'  
            elif number == 9: return 'Nikita MAZEPIN'               
            elif number == 10: return 'Pierre GASLY'               
            elif number == 11: return 'Sergio PEREZ' 
            elif number == 14: return 'Fernando ALONSO'                               
            elif number == 16: return 'Charles LECLERC'               
            elif number == 18: return 'Lance STROLL'                
            elif number == 20: return 'Kevin MAGNUSSEN' 
            elif number == 21: return 'Nyck VRIES'  
            elif number == 22: return 'Yuki TSUNODA'                           
            elif number == 23: return 'Alexander ALBON'
            elif number == 24: return 'ZHOU Guanyu'                
            elif number == 26: return 'Daniil KVYAT'  
            elif number == 27: return 'Nico HULKENBERG'              
            elif number == 31: return 'Esteban OCON'                
            elif number == 33: return 'Max VERSTAPPEN'  
            elif number == 34: return 'Felipe DRUGOVICH'             
            elif number == 40: return 'Roy NISSANY'                
            elif number == 44: return 'Lewis HAMILTON'   
            elif number == 47: return 'Mick SCHUMACHER'             
            elif number == 55: return 'Carlos SAINZ'   
            elif number == 63: return 'George RUSSELL'               
            elif number == 77: return 'Valtteri BOTTAS'  
            elif number == 81: return 'Oscar PIASTRI'
            elif number == 88: return 'Robert KUBICA'
            elif number == 99: return 'Antonio GIOVINAZZI'
            else:  raise NameError(f'Number {number} is not found for year {year}')
        else: raise NameError('The year introduced is not correct')
                

class seasonResult:
    """Returns the final season results from the corresponding year and driver introduced.
    - year: Integer corresponding to season's year
    - driver: Stringcorresponding to Driver's Name
    """
    def __init__(self, year: int, driver: str):
        self.finalResult = self.get_result(year,driver)

    def get_result(self, year: int, driver):
        path = f'C:\\Users\\migue\\Documents\\F1 Data Center\\{year}'
        os.chdir(path)
        result = raceResult(driver, level = 'all').result[0]
        return result


class f1_calendar:
    """Returns a `List` containing the corresponding F1 Calendar containing the GPs Names.
    - year: Integer corresponding to season's year
    """

    def __init__(self,year):
        self.calendar = self.getCalendar(year)
    
    def getCalendar(self,year):
        '''Returns a `List` with all the gps calendar'''
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
        elif year == 2023:
            calendar = ['Bahrein', 'Saudi', 'Australia', 'Azerbaiyan', 'Miami', 'Imola', 'Monaco', 'España', 'Canada', 'Austria', 'GB', 'Hungria','Belgica','Holanda','Italia','Singapur','Japon','Qatar','EEUU','Mexico','Brasil','Vegas','AbuDhabi']
        else: 
            raise NameError('The year introduced is not correct')
        
        return calendar

class f1_Testing:
    """Returns a `List` containing the corresponding F1 Calendar containing the GPs Names.
    - year: Integer corresponding to season's year
    """
    def __init__(self,year):
        path =  f'C:\\Users\\migue\\Documents\\F1 Data Center\\Datos\\fastf1_Testing_Timing_Data\\{year}'
        os.chdir(path)

        self.testNumber, *self.yearSes = self.totalSes()
        if year == 2020:
            self.circuit = 'España'
        elif year in [2021,2022,2023]:
            self.circuit = 'Bahrein'
        else: raise NameError('The year introduced is not correct')
    
    def totalSes(self):
        testNumbers = []
        sesions = []
        path = os.getcwd()
        elems = os.listdir(path)
        for i in elems:
            num = re.findall('\d+', i)
            if int(num[0]) not in testNumbers:
                testNumbers.append(int(num[0]))
            if int(num[1]) not in sesions:
                sesions.append(int(num[1]))

        return max(testNumbers), testNumbers,sesions
            



class driversAGE:
    """Returns a `List` correspoinding to the Drivers's Age.
    - names: List containing every Driver name
    - year: Integer corresponding to season's year
    """
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
            elif names[i]== 'Nikita MAZEPIN' or names[i] == 'Mick SCHUMACHER'or names[i] == 'Guanyu ZHOU' or names[i]== 'Lando NORRIS' or names[i] == 'ZHOU Guanyu' or names[i]== 'Robert SHWARTZMAN' or names[i] == "Patricio O'WARD":
                born = 1999
                age.append(year - born)
            elif names[i] == 'Yuki TSUNODA' or names[i] == 'Juri VIPS' or names[i] == 'Logan SARGEANT' or names[i] == 'Felipe DRUGOVICH':
                born = 2000
                age.append(year - born)
            elif names[i] == 'Oscar PIASTRI':
                born = 2001
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
    """Returns a `List` correspoinding to the month when each GP was celebrated.
    - year: Integer corresponding to season's year
    - grand_prix: List containing every Grand Prix corresponding to that year
    """
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
        elif year == 2019:
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
        elif year == 2020:
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
        elif year == 2021:
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

        elif year == 2022:
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
        
        ##################################################################################
        #2023Season
        ##################################################################################

        elif year == 2023:
            for i in range(len(grand_prix)):
                if grand_prix[i]== 'Bahrein' or  grand_prix[i]== 'Saudi':
                    month.append("MAR")
                elif grand_prix[i]== 'Azerbaiyan' or grand_prix[i]== 'Australia':
                    month.append("APR")
                elif grand_prix[i]== 'Miami' or grand_prix[i] == 'Imola' or grand_prix[i] == 'Monaco':
                    month.append("MAY")
                elif grand_prix[i]== 'España' or grand_prix[i] == 'Canada':
                    month.append("JUN")
                elif grand_prix[i]== 'Austria' or grand_prix[i] == 'GB'  or grand_prix[i]== 'Hungria':
                    month.append("JUL")
                elif grand_prix[i] == 'Belgica' or grand_prix[i]== 'Holanda':
                    month.append("AUG")
                elif grand_prix[i] == 'Italia' or grand_prix[i]== 'Singapur' or grand_prix[i] == 'Japon':
                    month.append("SEP")
                elif grand_prix[i] == 'EEUU' or  grand_prix[i]== 'Mexico' or grand_prix[i]== 'Qatar':
                    month.append("OCT")
                elif grand_prix[i] == 'Brasil' or grand_prix[i] == 'AbuDhabi' or grand_prix[i] == 'Vegas':
                    month.append("NOV")
                else:
                    month.append("NO MONTH")
        
        else: 
            raise NameError('The year introduced is not correct')

        return month


class getWEATHER:
    """Returns the Weather during that F1 Session. Posible outputs: `D`(Dry), `D/I`(Mixed conditions), `I`(Inter), `I/W`(Mixed wet conditions), `W`(Full Wet).
    - year: Integer corresponding to season's year
    - circuit: String corresponding to GP's Name
    - sesion: Sting corresponding to Session's Name
    """
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
            
        ##################################################################################
        #2023Season
        ##################################################################################    
        elif year == 2023:
            return 'D'
        
        else:
            return 'D'

class weekendFormat:
    """Returns the Weekend Format that Occurs during that GP. Posible outputs: `Normal` and `Sprint`.
    - year: Integer corresponding to season's year
    - circuit: String containing the Grand Prix Name
    """
    def __init__(self, year: int, circuit: str):
        self.f = self.format(year,circuit)

    def format(self, year, circuit):
        '''Posible outputs: Normal and Sprint'''
        ##################################################################################
        #2021Season
        ##################################################################################
        if year == 2021:
            if circuit == 'GB':
                return 'Sprint'
            elif circuit == 'Italia':
                return 'Sprint'
            elif circuit == 'Brasil':
                return 'Sprint'
            else:
                return 'Normal'
        ##################################################################################
        #2022Season
        ##################################################################################
        elif year == 2022:
            if circuit == 'Imola':
                return 'Sprint'
            elif circuit == 'Austria':
                return 'Sprint'
            elif circuit == 'Brasil':
                return 'Sprint'
            else:
                return 'Normal'
        ##################################################################################
        #2023Season
        ##################################################################################
        elif year == 2023:
            if circuit == 'Azerbaiyan':
                return 'Sprint'
            elif circuit == 'Austria':
                return 'Sprint'
            elif circuit == 'Belgica':
                return 'Sprint'
            elif circuit == 'Qatar':
                return 'Sprint'
            elif circuit == 'EEUU':
                return 'Sprint'
            elif circuit == 'Brasil':
                return 'Sprint'
            else:
                return 'Normal'
        else:
            return 'Normal'

class renameGP:
    """Rename a GP by its Circuit Name.
    - year: Integer corresponding to season's year
    - circuit: String containing the Grand Prix Name
    """
    def __init__(self, year: int, circuit: str):
        self.circuitName = self.rename(year,circuit)

    def rename(self, year, circuit):
        '''Rename it by "circuit" '''
        ##################################################################################
        #2020Season
        ##################################################################################
        if year == 2020:
            if circuit == 'Austria1' or circuit == 'Austria2':
                return 'Austria'
            elif circuit == 'GB1' or circuit == 'GB2':
                return 'GB'
            elif circuit == 'Alemania':
                return 'Nurburgring'
            else:
                raise NameError('GP Name Problem')
        ##################################################################################
        #2021Season
        ##################################################################################
        if year == 2021:
            if circuit == 'GB1' or circuit == 'GB2':
                return 'GB'
            else:
                raise NameError('GP Name Problem')

        else:
            raise NameError('The year introduced is not correct')

class lastTeamName:
    """Return a `List` containing a shorter version of the name and regarding the final team is in the grid. 
    For example Renault became Alpine because in the grid they are called Alpine in the last year of the dataset
    - teams: List containing the original F1 Team Name
    """
    def __init__(self, teams: list):
        self.correct = self.getShortNames(teams)
    
    def getShortNames(self,teams):
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

# class plotColors:
#     def __init__(self, year: int):
#         self.color = self.getColors(year)
    
#     def getColors(self, year):
#         if year == 2018:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         elif year == 2019:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         elif year == 2020:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         elif year == 2021:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         elif year == 2022:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         elif year == 2023:
#             back, lgnd = '#DFF0FF', '#DFF0FF'
#         else:
#             raise NameError('The year introduced is not correct')
#         return back, lgnd

