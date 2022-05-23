#%%import module
import csv

#%%loading data
csvfile = open('data\clean_data.csv', newline = '\n')
cfile = csv.reader(csvfile)
    
def fpd(aaa,bbb,ccc):
    if i > aaa and i < bbb:
        ccc.append(sum(row[1:13]) / 12)
    final = sum(ccc) / 10  
    return final

#%%analyze
i = 0
ar = []
br = []
cr = []
dr = []
er = []
fr = []
gr = []
hr = []
ir = []
jr = []
kr = []
lr = []
mr = []
nr = []

for roow in cfile:
    i += 1
    if i != 1:
        row = [float(p) for p in roow] 
    if i > 1 and i < 13:
        ar.append(sum(row[1:13]) / 12)
    b = fpd(12,23,br)
    c = fpd(22,33,cr)
    d = fpd(32,43,dr)
    e = fpd(42,53,er)
    f = fpd(52,63,fr)
    g = fpd(62,73,gr)
    h = fpd(72,83,hr)
    ii = fpd(82,93,ir)
    j = fpd(92,103,jr)
    k = fpd(102,113,kr)
    l = fpd(112,123,lr)
    m = fpd(122,133,mr)
    if i > 132:
        nr.append(sum(row[1:13]) / 12)

a = sum(ar) / 11
n = sum(nr) / 11  
   
def cf(q):
    return q / 100 * 1.8 
        
print('Average Temperature change for decade from 1880 to 1890: {:.1f}°F'.format(cf(a)))
print('Average Temperature change for decade from 1891 to 1900: {:.1f}°F'.format(cf(b)))
print('Average Temperature change for decade from 1891 to 1900: {:.1f}°F'.format(cf(b)))
print('Average Temperature change for decade from 1901 to 1910: {:.1f}°F'.format(cf(c)))
print('Average Temperature change for decade from 1911 to 1920: {:.1f}°F'.format(cf(d)))
print('Average Temperature change for decade from 1921 to 1930: {:.1f}°F'.format(cf(e)))
print('Average Temperature change for decade from 1931 to 1940: {:.1f}°F'.format(cf(f)))
print('Average Temperature change for decade from 1941 to 1950: {:.1f}°F'.format(cf(g)))
print('Average Temperature change for decade from 1951 to 1960: {:.1f}°F'.format(cf(h)))
print('Average Temperature change for decade from 1961 to 1970: {:.1f}°F'.format(cf(ii)))
print('Average Temperature change for decade from 1971 to 1980: {:.1f}°F'.format(cf(j)))
print('Average Temperature change for decade from 1981 to 1990: {:.1f}°F'.format(cf(k)))
print('Average Temperature change for decade from 1991 to 2000: {:.1f}°F'.format(cf(l)))
print('Average Temperature change for decade from 2001 to 2010: {:.1f}°F'.format(cf(m)))
print('Average Temperature change for decade from 2011 to 2021: {:.1f}°F'.format(cf(n)))
