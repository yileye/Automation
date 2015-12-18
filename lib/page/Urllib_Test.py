import urllib,re
url = r'http://10.66.11.225:8090/monitor/rhevh_build/7.2/vdsm7/20151210.1_36/'
fp_get = urllib.urlopen(url).read()
print fp_get
parame = r'(?<=href=\").+?(?=\")'
resault = re.findall(parame,fp_get)
for i in  resault:
    print i