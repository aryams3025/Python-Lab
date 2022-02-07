import csv 
dict_value = [
{'NAME':'AKHILA', 'MFC':50, 'DC':56, 'DS':59, 'ASE':55},
     {'NAME':'BINCY', 'MFC':51, 'DC':58, 'DS':55, 'ASE':59},
     {'NAME':'ANUSREE', 'MFC':60, 'DC':55, 'DS':57,'ASE':50},
     {'NAME':'ARYA', 'MFC':55, 'DC':53, 'DS':54, 'ASE':59},
     {'NAME':'VYSAKH', 'MFC':60, 'DC':60, 'DS':60, 'ASE':60},
     {'NAME':'ARUN', 'MFC':57, 'DC':59, 'DS':59, 'ASE':59},
     {'NAME':'ANU', 'MFC':50, 'DC':58, 'DS':50, 'ASE':58},
     {'NAME':'AMAL', 'MFC':59, 'DC':50, 'DS':57, 'ASE':50},
     {'NAME':'GOKUL', 'MFC':50, 'DC':58, 'DS':50, 'ASE':50},
     {'NAME':'MINNU', 'MFC':50, 'DC':51, 'DS':55, 'ASE':59},
    ]

fields = ["NAME","MFC","DC","DS","ASE"]

with open('student.csv','w') as c:
    writer = csv.DictWriter(c,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    c.close()
mfc=0
dc=0
ase=0
ds=0
with open('student.csv','r') as cfiles:
     reader = csv.DictReader(cfiles)
     for row in reader:
         print(row['NAME'],":",(int(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100)
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ase=ase+int(row['ASE'])
         ds=ds+int(row['DS'])
print("\n\nAverage of subjcts")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
