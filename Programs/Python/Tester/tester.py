import sys
import os
year = 2021

path = "/Users/migue/Documents/F1 Data Center/Datos/"
os.chdir(path)

if year == 2021:
    names = ['Daniel RICCIARDO', 'Lando NORRIS', 'Sebastian VETTEL', 'Nicholas LATIFI', 'Kimi RAIKKONEN', 'Nikita MAZEPIN', 'Pierre GASLY', 'Sergio PEREZ', 'Fernando ALONSO', 'Charles LECLERC', 'Lance STROLL', 'Yuki TSUNODA', 'Esteban OCON', 'Max VERSTAPPEN', 'Lewis HAMILTON', 'Mick SCHUMACHER', 'Carlos SAINZ', 'George RUSSELL', 'Valtteri BOTTAS', 'Antonio GIOVINAZZI','Robert KUBICA']


######################################################################################################
#Teams Colours
fer = '#9f121d'
rb = '#340db0'
mer = '#25b8a1'
am = '#185d5b'
at = '#2d3c4f'
ar = '#6b101b'
alp = '#2180c3'
wil = '#1e52b8'
mcl = '#ca923e'
haa = '#f0eff2'

colour_driver, colour_teams = [],[]

for i in range(len(names)):
        if names[i]== 'Daniel RICCIARDO' or names[i] == 'Lando NORRIS':
            colour_driver.append(mcl)
        elif names[i]== 'Sebastian VETTEL' or names[i] == 'Lance STROLL':
            colour_driver.append(am)
        elif names[i]== 'Nicholas LATIFI' or names[i] == 'George RUSSELL'or names[i] == 'Jack AITKEN'or names[i] == 'Roy NISSANY':
            colour_driver.append(wil)
        elif names[i]== 'Kimi RAIKKONEN' or names[i] == 'Antonio GIOVINAZZI'or names[i] == 'Robert KUBICA'or names[i] == 'Callum ILOTT':
            colour_driver.append(ar)
        elif names[i]== 'Nikita MAZEPIN' or names[i] == 'Mick SCHUMACHER':
            colour_driver.append(haa)
        elif names[i]== 'Pierre GASLY' or names[i] == 'Yuki TSUNODA':
            colour_driver.append(at)
        elif names[i]== 'Sergio PEREZ' or names[i] == 'Max VERSTAPPEN':
            colour_driver.append(rb)
        elif names[i]== 'Fernando ALONSO' or names[i] == 'Esteban OCON'or names[i] == 'Guanyu ZHOU':
            colour_driver.append(alp)
        elif names[i]== 'Charles LECLERC' or names[i] == 'Carlos SAINZ':
            colour_driver.append(fer)
        elif names[i]== 'Valtteri BOTTAS' or names[i] == 'Lewis HAMILTON':
            colour_driver.append(mer)

#print(colour_driver)

######################################################################################################
#Surname list

sur_list = []

for i in names:
    surname = i.split(' ')[1]
    sur = surname[0:3]
    sur_list.append(sur)

# print(sur_list)

######################################################################################################
#Sort by time
if year == 2021: 

    bah = [89927,89974,92056,91936,91238,93273,89809,90659,90249,89678,90601,90607,91724,88997,89385,92449,90009,91316,89586,90708,0]
    imo= [74826,74454,75394,75593,75974,76797,74790,74446,75593,74740,75138,0,75117,74498,74411,76279,75199,75261,74672,76122,0]
    por= [79839,78481,78970,80285,79748,80912,79052,78845,79456,78769,79913,79463,78586,78209,77968,80452,78813,79109,78348,79216,0]
    esp= [77622,77696,78079,79219,78917,79807,77982,77669,77966,77510,77974,78556,77580,76777,76741,79117,77620,78445,76873,78356,0]
    mon= [71598,70620,71309,72366,71642,72958,70900,71019,72205,70346,71600,72096,71486,70576,71095,0,70611,71830,70601,71409,0]
    aze= [102304,101747,102224,103128,102587,104238,101565,101630,102195,101218,0,101654,102273,101563,101450,104158,101576,102728,102106,0,0]
    fra= [91382,91252,91767,93062,93354,93554,90868,90445,91340,90987,92122,166130,91736,89990,90248,92942,90840,92065,90376,91813,0]
    aut1= [64808,64120,64711,65175,65429,66192,64236,64168,64574,64472,64663,64514,65217,63841,64067,66041,64711,64671,64035,64913,0]
    aut2= [64719,63768,64493,65195,65009,65951,64107,63990,64472,64600,64547,64273,65051,63720,64014,65427,64559,64553,64049,64777,0]
    gb= [86899,86897,87103,88254,88062,89051,87273,86813,87245,86828,87665,88043,87340,86209,86023,88738,86848,86971,86328,87595,0]
    hun= [76871,76385,76750,78036,77553,78922,76394,76421,76541,76496,76893,77919,76653,75650,75419,0,76649,77944,75734,77583,0]
    bel= [117127,116025,116814,118056,124452,124939,116440,116886,118205,117721,118231,122413,117354,116559,116229,123973,118137,116950,116295,122306,0]
    hol= [69865,70406,70731,70093,0,71875,69478,70530,69956,69437,70367,70462,69919,68885,68923,71387,69537,70332,69222,69590,71301]
    ita= [79995,79989,80913,81925,0,82716,80260,80611,81069,80510,81020,81711,81103,79966,79651,82248,80462,81392,79555,80726,82530]
    rusia= [104156,101993,106573,108252,109586,113764,106641,105337,104204,108470,104956,106751,105865,119522,104050,109830,102510,102983,104710,111023,0]
    tur= [85881,83954,84795,86086,87525,88449,83326,83706,83477,83265,84305,84054,84842,83196,82868,85200,85177,85007,82998,86430,0]
    usa= [93808,93880,95281,95995,96311,96796,94118,93134,95756,93606,95983,94918,95377,92910,93119,96499,93792,95730,93475,95794,0]
    mex= [76763,77473,77502,78756,77606,79303,76456,76342,78452,76748,80873,76701,78126,76225,76020,78858,76761,77958,75875,77897,0]
    bra= [69039,68980,69399,69897,69503,70589,68777,68483,69113,68859,69663,69350,69189,68372,67934,69958,68826,69953,68426,69342,0]
    qat= [82597,81731,82146,83213,83156,85859,81640,82346,81670,82463,82460,81881,82012,81282,80827,83407,81840,82756,81478,83262,0]
    sau= [88216,88180,89198,89177,88856,90473,88125,87946,88920,88054,89368,88222,88574,87653,87511,89464,88237,88926,87622,88616,0]
    abu= [83409,82931,84225,84338,84779,85685,83489,82947,83460,83122,84061,83011,83389,82109,82480,84906,82992,84423,83036,84118,0]

    ric = 0
    nor = 0
    vet = 0
    lat = 0
    rai = 0
    maz = 0
    gas = 0
    per = 0
    alo = 0
    lec = 0
    strl = 0
    tsu = 0
    oco = 0
    ver = 0
    ham = 0
    sch = 0
    sai = 0
    rus = 0
    bot = 0
    gio = 0
    kub = 0

    circuits = [bah,imo,por,esp,mon,aze,fra,aut1,aut2,gb,hun,bel,hol,ita,rusia,tur,usa,mex,bra,qat,sau,abu]

    for c in range(len(circuits)):
        points = [25,18,15,12,10,8,6,4,2,1,0,0,0,0,0,0,0,0,0,0]
        p = -1
        circuit = circuits[c]
        if circuit.count(0) < 10:
            for i in range(len(circuit)):
                minim = min(circuit)
                if minim == 0:
                    zero = circuit.index(minim)
                    circuit[zero] = sys.maxsize
                else:
                    p += 1
                    index = circuit.index(minim)
                    circuit[index] = sys.maxsize
                    if index == 0: ric += points[p]     
                    elif index == 1:  nor += points[p]
                    elif index == 2:  vet += points[p]
                    elif index == 3:  lat += points[p]
                    elif index == 4:  rai += points[p]
                    elif index == 5:  maz += points[p]
                    elif index == 6:  gas += points[p]
                    elif index == 7:  per += points[p]
                    elif index == 8:  alo += points[p]
                    elif index == 9:  lec += points[p]
                    elif index == 10:  strl += points[p]
                    elif index == 11:  tsu += points[p]
                    elif index == 12:  oco += points[p]
                    elif index == 13:  ver += points[p]
                    elif index == 14:  ham += points[p]
                    elif index == 15:  sch += points[p]
                    elif index == 16:  sai += points[p]
                    elif index == 17:  rus += points[p]
                    elif index == 18:  bot += points[p]
                    elif index == 19:  gio += points[p]
                    elif index == 20:  kub += points[p]

points_list = [ric ,nor,vet,lat,rai,maz,gas,per,alo,lec,strl,tsu,oco,ver,ham,sch,sai,rus,bot,gio,kub]                  
#print(points_list)
                        
    
######################################################################################################
#Quali Performance

if year == 2021: 

    bah = [89927,89974,92056,91936,91238,93273,89809,90659,90249,89678,90601,90607,91724,88997,89385,92449,90009,91316,89586,90708,0]
    imo= [74826,74454,75394,75593,75974,76797,74790,74446,75593,74740,75138,0,75117,74498,74411,76279,75199,75261,74672,76122,0]
    por= [79839,78481,78970,80285,79748,80912,79052,78845,79456,78769,79913,79463,78586,78209,77968,80452,78813,79109,78348,79216,0]
    esp= [77622,77696,78079,79219,78917,79807,77982,77669,77966,77510,77974,78556,77580,76777,76741,79117,77620,78445,76873,78356,0]
    mon= [71598,70620,71309,72366,71642,72958,70900,71019,72205,70346,71600,72096,71486,70576,71095,0,70611,71830,70601,71409,0]
    aze= [102304,101747,102224,103128,102587,104238,101565,101630,102195,101218,0,101654,102273,101563,101450,104158,101576,102728,102106,0,0]
    fra= [91382,91252,91767,93062,93354,93554,90868,90445,91340,90987,92122,166130,91736,89990,90248,92942,90840,92065,90376,91813,0]
    aut1= [64808,64120,64711,65175,65429,66192,64236,64168,64574,64472,64663,64514,65217,63841,64067,66041,64711,64671,64035,64913,0]
    aut2= [64719,63768,64493,65195,65009,65951,64107,63990,64472,64600,64547,64273,65051,63720,64014,65427,64559,64553,64049,64777,0]
    gb= [86899,86897,87103,88254,88062,89051,87273,86813,87245,86828,87665,88043,87340,86209,86023,88738,86848,86971,86328,87595,0]
    hun= [76871,76385,76750,78036,77553,78922,76394,76421,76541,76496,76893,77919,76653,75650,75419,0,76649,77944,75734,77583,0]
    bel= [117127,116025,116814,118056,124452,124939,116440,116886,118205,117721,118231,122413,117354,116559,116229,123973,118137,116950,116295,122306,0]
    hol= [69865,70406,70731,70093,0,71875,69478,70530,69956,69437,70367,70462,69919,68885,68923,71387,69537,70332,69222,69590,71301]
    ita= [79995,79989,80913,81925,0,82716,80260,80611,81069,80510,81020,81711,81103,79966,79651,82248,80462,81392,79555,80726,82530]
    rusia= [104156,101993,106573,108252,109586,113764,106641,105337,104204,108470,104956,106751,105865,119522,104050,109830,102510,102983,104710,111023,0]
    tur= [85881,83954,84795,86086,87525,88449,83326,83706,83477,83265,84305,84054,84842,83196,82868,85200,85177,85007,82998,86430,0]
    usa= [93808,93880,95281,95995,96311,96796,94118,93134,95756,93606,95983,94918,95377,92910,93119,96499,93792,95730,93475,95794,0]
    mex= [76763,77473,77502,78756,77606,79303,76456,76342,78452,76748,80873,76701,78126,76225,76020,78858,76761,77958,75875,77897,0]
    bra= [69039,68980,69399,69897,69503,70589,68777,68483,69113,68859,69663,69350,69189,68372,67934,69958,68826,69953,68426,69342,0]
    qat= [82597,81731,82146,83213,83156,85859,81640,82346,81670,82463,82460,81881,82012,81282,80827,83407,81840,82756,81478,83262,0]
    sau= [88216,88180,89198,89177,88856,90473,88125,87946,88920,88054,89368,88222,88574,87653,87511,89464,88237,88926,87622,88616,0]
    abu= [83409,82931,84225,84338,84779,85685,83489,82947,83460,83122,84061,83011,83389,82109,82480,84906,82992,84423,83036,84118,0]

    circuits = [bah,imo,por,esp,mon,aze,fra,aut1,aut2,gb,hun,bel,hol,ita,rusia,tur,usa,mex,bra,qat,sau,abu]
    circuits_name = ['Bahrein', 'Imola', 'Portugal', 'España', 'Monaco', 'Azerbaiyan','Francia', 'Austria1', 'Austria2',  'GB', 'Hungria', 'Belgica', 'Holanda', 'Italia', 'Rusia', 'Turquia','EEUU', 'Mexico', 'Brasil', 'Qatar', 'Saudi',  'AbuDhabi']

    f = open("q_dist.csv", "w+")
    #header = 'GP_ID, GP_Name, Bahrein, Imola, Portugal, España, Monaco, Azerbaiyan,Francia,Austria1, Austria2,  GB, Hungria, Belgica, Holanda, Italia, Rusia, Turquia,EEUU, Mexico, Brasil, Qatar, Saudi,  AbuDhabi \n'
    header = 'GP_ID, GP_Name, Distance, Team \n'
    f.write(header)
    #Find minim inside each team:
    for c in range(len(circuits)):
        text = ''
        circuit = circuits[c]
        teams_best = []
        mcl, am, wil, ar, haa, at, rb, alp, fer, mer = [0,1], [2,10],[3,17],[4,19,20],[5,15],[6,11],[7,13],[8,12],[9,16],[14,18]
        teams = [mcl, am, wil, ar, haa, at, rb, alp, fer, mer]
        #Substitue index by lap time
        for t in range(len(teams)):
            for d in range(len(teams[t])):
                index =  teams[t][d]
                teams[t][d] = circuit[index]
        
        #Create list with the minimum lap time for each team
        for t in teams:
            count = t.count(0)
            if count > 0:
                for _ in range(count):
                    index = t.index(0)
                    t[index] = sys.maxsize
            minim = min(t)
            teams_best.append(minim)              

        #Creation of Data Frame
        minim = min(teams_best)
        for t in range(len(teams_best)):
            dist = teams_best[t] - minim
            teams_best[t] = dist

        for i in range(len(teams_best)):
            teams_name = ['Mclaren', 'Aston Martin', 'Williams', 'Alfa Romeo', 'Haas', 'AlphaTauri', 'Red Bull', 'Alpine', 'Ferrari', 'Mercedes']
            text += str(c+1)+','+str(circuits_name[c])+','+str(teams_best[i])+','+str(teams_name[i])+'\n'
        
        #Each Instance
        f.write(text)
        

