import re
from tqdm import tqdm
import time

file = '2019_01_aus_f1_p1_timing_firstpracticesessionlaptimes_v01.pdf'

# patern = re.compile('_\d+_')
# number = patern.findall(file)[0]
# number = int(re.sub('_','',number))

patern = re.compile('_\d+_')
number_rare = patern.findall(file)[0]
#Remove '_'
number = int(re.sub('_','',number_rare))

print(type(number))
print(number)

l =["fp1.pdf","fp2.pdf","fp3.pdf","quali.pdf","race.pdf","fp1.txt","fp2.txt","fp3.txt","quali.txt","race.txt"]

print(l[5:])

for i in tqdm(range(20), desc = 'tqdm() Progress Bar'):
    time.sleep(0.5)
