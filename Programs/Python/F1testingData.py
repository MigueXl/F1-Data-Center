#LIBRARIES
import fastf1 as ff1
import numpy as np
import pandas as pd
import pickle
import os
import multidata

class Extractor:
    '''Returns a `np.ndarray` containing the most interesting features from the corresponding testing season.
    - year: Integer corresponding to season's year
    - testNumber: Integer Containing the Test Number
    - sesion: Integer Containing the Season Number
    '''
    def __init__(self, year: int, testNumber: int, sesion: int):
        self.year = year
        self.data = self.returnData(year,testNumber,sesion)
    
    # Transform Driver Number into Drivers Name
    def transformNum(self, row):
        numb = row['Driver'] 
        return multidata.numberToNames(self.year, numb).name
    
    def toMins(self,row):
        try: 
            return row['Time'].total_seconds() / 60
        except:
            return np.nan

    def toMiliscs(self,elem):
        try: 
            return elem.total_seconds() *1000
        except:
            return np.nan

    def returnQualy_RaceLaps(self, times: np.array, mode: str = 'tt'):
        qualyLaps = []
        qualyIndeces = []
        raceLaps = []
        raceIndices = []
        minTime = np.nanmin(times)
        qualyTop = (minTime * 103)/100
        raceTop = (minTime * 110)/100
        for t,time in enumerate(times):
            if time != np.nan:
                if time <= qualyTop:
                    qualyLaps.append(time)
                    qualyIndeces.append(t)
                elif time <= raceTop:
                    raceLaps.append(time)
                    raceIndices.append(t)

        if mode == 'tt':
            if len(qualyLaps) == 0 and len(raceLaps) == 0:
                return [0], [0], [0], [0]
            elif len(raceLaps) == 0:
                return np.array(qualyLaps), qualyIndeces, [0], [0]
            else:
                return np.array(qualyLaps), qualyIndeces, np.array(raceLaps), raceIndices
        else: 
            if len(qualyLaps) == 0 and len(raceLaps) == 0:
                return [0], [0]
            elif len(raceLaps) == 0:
                return np.array(qualyLaps), [0]
            else:
                return np.array(qualyLaps), np.array(raceLaps)

    def returnData(self,year,testNumber,sesion):
        try: 
            circuit = multidata.f1_Testing(year).circuit
            path =  f'C:\\Users\\migue\\Documents\\F1 Data Center\\Datos\\fastf1_Testing_Timing_Data\\{year}'
            os.chdir(path)
            with open(f'timing_data_t{testNumber}_s{sesion}.ff1pkl', 'rb') as f:
                data = pickle.load(f)
            dataTuple = data['data'][0]
            df = pd.DataFrame(dataTuple)

            #REMOVE EMPTY ROWS
            nanDF = df.isna()
            df['TotalNan'] = nanDF.sum(axis=1) 
            df = df.loc[(df['TotalNan'] <= 2), :]
            df = df.drop(['TotalNan'], axis=1)
            df = df.reset_index(drop=True)

            df = df.loc[df['Driver'].astype(int) < 100, :] #bug

            #DROP UNNECESSARY COLUMNS
            df = df.drop(['PitOutTime', 'PitInTime', 'Sector1SessionTime','Sector2SessionTime','Sector3SessionTime','IsPersonalBest'], axis=1)

            df['Driver'] = df.apply(self.transformNum, axis=1)
            df['Time'] = df.apply(self.toMins, axis=1)
            df['LapTime'] = df['LapTime'].apply(self.toMiliscs)
            df['Sector1Time'] = df['Sector1Time'].apply(self.toMiliscs)
            df['Sector2Time'] = df['Sector2Time'].apply(self.toMiliscs)
            df['Sector3Time'] = df['Sector3Time'].apply(self.toMiliscs)

            colsName = ['Driver', 'Team', 'Year', 'Circuit', 'Test_number', 'Session', 'Total_PitStops', 'Total_Laps', 'Fastest_Lap', 'Fastest_S1', 'Fastest_S2', 'Fastest_S3', 'Ideal_FLap', 
            'Qualy_Times', 'Total_Qualy_Laps', 'Avg_Qualy_Track_Time','Avg_Qualy_Speed1', 'Avg_Qualy_Speed2', 'Avg_Qualy_SpeedFL', 'Avg_Qualy_SpeedST', 'Sector1_Qualy', 'Total_S1Q_Laps', 'Sector2_Qualy', 'Total_S2Q_Laps', 'Sector3_Qualy', 'Total_S3Q_Laps', 
            'Race_Times', 'Total_Race_Laps', 'Avg_Race_Track_Time', 'Avg_Race_Speed1', 'Avg_Race_Speed2', 'Avg_Race_SpeedFL', 'Avg_Race_SpeedST', 'Sector1_Race', 'Total_S1R_Laps', 'Sector2_Race', 'Total_S2R_Laps',
            'Sector3_Race','Total_S3R_Laps', 'FinalSeasonResult']

            drivers = df['Driver'].unique()
            rows = len(drivers)
            data = np.empty((rows, len(colsName)),  dtype='object')

            teams = multidata.f1_teams(drivers, year, 'Default', 'Default').equipos
            teams = multidata.lastTeamName(teams).correct
            for d,driv in enumerate(drivers):
                data[d,colsName.index('Driver')] = driv
                data[d,colsName.index('Team')] = teams[d]
                data[d,colsName.index('Year')] = year
                data[d,colsName.index('Circuit')] = circuit
                data[d,colsName.index('Test_number')] = testNumber
                data[d,colsName.index('Session')] = sesion

                dfDriv = df.loc[(df['Driver'] == driv), :] 
                data[d,colsName.index('Total_PitStops')] = dfDriv['NumberOfPitStops'].max()
                data[d,colsName.index('Total_Laps')] = dfDriv['NumberOfLaps'].max()

                allTimes = dfDriv['LapTime'].to_numpy()
                qualyLaps, qualyIndeces, raceLaps, raceIndices = self.returnQualy_RaceLaps(allTimes)

                data[d,colsName.index('Fastest_Lap')] = np.amin(qualyLaps)
                data[d,colsName.index('Qualy_Times')] = int(np.nanmean(qualyLaps, dtype=np.float64))
                data[d,colsName.index('Total_Qualy_Laps')] = len(qualyLaps)
                dfDrivQuali = dfDriv.iloc[qualyIndeces, :]
                data[d,colsName.index('Avg_Qualy_Track_Time')] = int(np.nanmean(dfDrivQuali['Time'].to_numpy()))
                data[d,colsName.index('Avg_Qualy_Speed1')] = int(np.nanmean(dfDrivQuali['SpeedI1'].to_numpy()))
                data[d,colsName.index('Avg_Qualy_Speed2')] = int(np.nanmean(dfDrivQuali['SpeedI2'].to_numpy()))
                data[d,colsName.index('Avg_Qualy_SpeedFL')] = int(np.nanmean(dfDrivQuali['SpeedFL'].to_numpy()))
                data[d,colsName.index('Avg_Qualy_SpeedST')] = int(np.nanmean(dfDrivQuali['SpeedST'].to_numpy()))

                data[d,colsName.index('Race_Times')] = int(np.mean(raceLaps, dtype=np.float64))
                data[d,colsName.index('Total_Race_Laps')] = len(raceLaps)
                dfDrivrace = dfDriv.iloc[raceIndices, :]
                data[d,colsName.index('Avg_Race_Track_Time')] = int(np.nanmean(dfDrivrace['Time'].to_numpy()))
                data[d,colsName.index('Avg_Race_Speed1')] = int(np.nanmean(dfDrivrace['SpeedI1'].to_numpy()))
                data[d,colsName.index('Avg_Race_Speed2')] = int(np.nanmean(dfDrivrace['SpeedI2'].to_numpy()))
                data[d,colsName.index('Avg_Race_SpeedFL')] = int(np.nanmean(dfDrivQuali['SpeedFL'].to_numpy()))
                data[d,colsName.index('Avg_Race_SpeedST')] = int(np.nanmean(dfDrivrace['SpeedST'].to_numpy()))

                s = dfDriv['Sector1Time'].to_numpy()
                qualyLaps, raceLaps = self.returnQualy_RaceLaps(s, mode='s')
                
                s1 = np.amin(qualyLaps)
                data[d,colsName.index('Fastest_S1')] = s1
                data[d,colsName.index('Sector1_Qualy')] = int(np.mean(qualyLaps))
                data[d,colsName.index('Total_S1Q_Laps')] = len(qualyLaps)
                data[d,colsName.index('Sector1_Race')] = int(np.mean(raceLaps))
                data[d,colsName.index('Total_S1R_Laps')] = len(raceLaps)

                s = dfDriv['Sector2Time'].to_numpy()
                qualyLaps, raceLaps = self.returnQualy_RaceLaps(s, mode='s')

                s2 = np.amin(qualyLaps)
                data[d,colsName.index('Fastest_S2')] = s2
                data[d,colsName.index('Sector2_Qualy')] = int(np.mean(qualyLaps))
                data[d,colsName.index('Total_S2Q_Laps')] = len(qualyLaps)
                data[d,colsName.index('Sector2_Race')] = int(np.mean(raceLaps))
                data[d,colsName.index('Total_S2R_Laps')] = len(raceLaps)

                s = dfDriv['Sector3Time'].to_numpy()
                qualyLaps, raceLaps = self.returnQualy_RaceLaps(s, mode='s')

                s3 = np.amin(qualyLaps)
                data[d,colsName.index('Fastest_S3')] = s3
                data[d,colsName.index('Sector3_Qualy')] = int(np.mean(qualyLaps))
                data[d,colsName.index('Total_S3Q_Laps')] = len(qualyLaps)
                data[d,colsName.index('Sector3_Race')] = int(np.mean(raceLaps))
                data[d,colsName.index('Total_S3R_Laps')] = len(raceLaps)

                data[d,colsName.index('Ideal_FLap')] = s1 + s2 + s3
                data[d,colsName.index('FinalSeasonResult')] = multidata.seasonResult(year,[driv]).finalResult[0]
                
            return data
        
        except:
            raise NameError(f'Problems Extracting Data from year = {year}, Test Number = {testNumber} and Session = {sesion}')