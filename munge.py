#%%import module
import re

#%%loading
df = open('data/nasa.txt', "r")

data = []

def rdr():
    lines = df.readline()
    lines = re.sub("\s+", ",", lines.strip())
    data.append(lines.strip())

for a in range(7):
    lines = df.readline()
  
cols = df.readline()
headings = re.sub("\s+", ",", cols.strip())

for b in range(21):
    rdr()

random = df.readline()
random = df.readline()

for c in range(20):
    rdr()

random = df.readline()
random = df.readline()

for d in range(20):
    rdr()

random = df.readline()
random = df.readline()

for e in range(20):
    rdr()

random = df.readline()
random = df.readline()

for f in range(20):
    rdr()

random = df.readline()
random = df.readline()

for g in range(20):
    rdr()

random = df.readline()
random = df.readline()

for h in range(20):
    rdr()

random = df.readline()
random = df.readline()

rdr()
    
df.close()

#print(data)
#print(headings)

#%%list to csv
f = open("data/clean_data.csv", "w")

f.write(headings + "\n")

cn = 0

for zzz in data:
    cn += 1
    if cn == 1:
        zzz = '1880,-17,-24,-8,-15,-9,-20,-17,-9,-14,-23,-21,-17,-16,-22.4,-21,-11,-16,-19,1880'
    f.write(zzz + "\n")

f.close()
