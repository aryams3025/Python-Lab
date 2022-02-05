import csv
csv_columns = ['No','Name','Place']
dict_data = [
{'No': 1, 'Name': 'AKHILA', 'Place': 'Kochi'},
{'No': 2, 'Name': 'BINCY', 'Place': 'Trivandrum'},
{'No': 3, 'Name': 'ARYA', 'Place': 'Kollam'},
{'No': 4, 'Name': 'ANUSREE', 'Place': 'Kannur'},
{'No': 5, 'Name': 'ARUN', 'Place': 'Kozhikode'},
]
csv_file = "names.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)


with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0]+" "+row[1]+" "+row[2])

import csv
csv_columns=['no','name','place']
dict_data=[
    {'no':1,'name':2,'place':'ran'}
]        
f=open("names.csv",'w')
r=csv.DictWriter(f,fieldnames=csv_columns)
r.writeheader()
for data in dict_data:
    r.writerow(data)
f.close()
f=open("names.csv",'r')
r=csv.reader(f)
for row in r:
    print(row)    
