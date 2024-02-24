import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

#cost = 50843
#car='Acura '
#engine='"3.5L 6cyl Turbo 10A"'
year=2023
# reading saved html file
a = open('edmunds.html',encoding='utf8').read()
soup = BeautifulSoup(a, features="html.parser")

#counter
step=0
# pick table number
 # search for car prices
carprices=soup.find_all("div",{"class": "pricing-section"})
# loop through text to find cost of vehicle
for carprice in carprices:
    #  finding cost in correct table
    if step == location-1:
        # appeding car price and fixing text to contain only value
        cost=carprice.text
        cost=cost[-6:]
        cost=cost.replace(",","")
    #     print()
    #     print(cost)
    # print(carprice)
    step=step+1

# finding header containing vehicle model
tmodels=soup.find_all("h1")
#searching for vehicle mode
for tmodel in tmodels:
 #   print(tmodel)
    #storing model
    car=tmodel.text

# triming text to only display vechicle type
car=car[5:-11]
#print(car)

# counter
step=0
# finding engine specifications
tmodels=soup.find_all("h2")
# looping through tables to find correct model
for tmodel in tmodels:
    #print(tmodel)
    if step == location:
        model=tmodel.text
    step=step+1

# storing model year
model =model.replace("{year} ","")
model=model.split(' (')
#print(f"{model}\n")
car='"'+car+model[0]+'"'
engine = model[1]
engine='"'+engine[:-1]+'"'

#print(car)
# searching for itemized cost
tds = soup.find_all('td')
# creating empty list
csv_data = []
strings= []

# starting point of array location to loop through
if location == 1:
    i=-1
else:
    i=location-2
j=i+2
#print((j-1)*48-1)
#print(j*49)
# looping through table entries and storing values 
for td in tds:
    if i>(j-1)*49-2:
        if i<j*49:
            inner_text = td.text
#            print(inner_text)
            strings = inner_text.split("\n")
    i=i+1
    if i == 49*j-1: break
    csv_data.extend([string for string in strings if  string])
#    csv_data.extend([string for string in strings if  string])

#print(" ".join(csv_data))

# creating numpy data
num = np.array(csv_data)
#print(num.size)
# reshaping data
reshaped = num.reshape(8,6)
# creating dataframe
new_df=pd.DataFrame(reshaped)
# dropping last line containing summed values
new_df.drop(new_df.tail(1).index,inplace=True)
#print(new_df)
# defining index
index=['Insurance','Maintenance','Repairs','Taxes & Fees','Financing',
       'Depreciation','Fuel']
# making seven column  containing cost, model year, car model and engine specifications
cost_col = [cost,cost,cost,cost,cost,cost,cost]
year_col = [year,year,year,year,year,year,year]
car_col = [car,car,car,car,car,car,car]
engine_col = [engine,engine,engine,engine,engine,engine,engine]
# filling columns with values
new_df.insert(loc=0,column='index',value=index)
new_df.insert(loc=7,column='cost',value=cost_col)
new_df.insert(loc=7,column='engine',value=engine_col)
new_df.insert(loc=7,column='car',value=car_col)
new_df.insert(loc=7,column='year',value=year_col)

# dropping column containing 5 year sum of itemized cost
new_df = new_df.drop(5,axis=1)
# printing created table to terminal
print(new_df.to_string(index=False,header=False))