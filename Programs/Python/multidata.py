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
        #2019Season
        ##################################################################################
        elif year == 2019:
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
        #2020Season
        ##################################################################################
        elif year == 2020:
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
            calendar = ['Austria1','Austria2']
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

# a = f1_calendar(2018)
# print(a.calendar)
