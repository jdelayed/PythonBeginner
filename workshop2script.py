# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:11:14 2021

@author: s2874394
"""


pressure = [0.27,0.456,0.3333,0.7,1.4]
print(len(pressure))
print(pressure[1])

#add single value to the end of my list
pressure.append(0.54333333)

#add another list
pressure.append([0.43,2.7,0.665])
print(pressure)

pressure1 = [0.27,0.456,0.3333,0.7,1.4]

#extend the list
pressure1.extend([0.43,2.7,0.665])

#delete
del pressure1[0]

empty = [1, "rrrrr", 1.2345]

##For loops

"I like cats"
"I like dogs"
"I like birds"
"I like coffee"

for number in (pressure1):
    print(number)

for kitten in [2,3,4,5]:
    print(kitten)

print(range(10))

total = 0
for number in range(10):
   total = total + (number + 1)
print(total)

primes = [2,3,5]
squared = []

for p in primes:
    sqr = p ** 2
    squared.append(sqr)
    print(squared)
    
total = 0
for char in "tin":
    total = total + 1
    print(total,char)


#if statements
mass = 1.7

if mass > 3.0 and mass <= 10.0:
    print(mass, "is large")
elif mass > 10.0:
        print(mass, "is super large")
else:
    print(mass, 'is not large')
    
    
masses = [2.4,7.4,1.1,52.3]

for i in masses:
    if i > 3.0 and i <= 10.0:
        print(i, "is large")
    elif i > 10.0:
            print(i, "is super large")
    else:
        print(i, 'is not large')
        
# can use and / or and = both conditions, or= either
for i in masses:
    if i > 3.0 or i <= 10.0:
        print(i, "is large")
    elif i > 10.0:
            print(i, "is super large")
    else:
        print(i, 'is not large')

velocity = [53.6,100.44,7.2,10000.2]

if masses[1] > 3.0 and masses[2] <= 10.0 or velocity[0] == 54:
    print('all good')
    
    
import glob
import pandas as pd
for filename in glob.glob('D:\Documents\Python_Training\data\*.csv'):
    contents = pd.read_csv(filename)
    if len(contents) < 50:
        print(filename, len(contents))
        
        
values = velocity
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)



#create functions, beyond built in functions

def print_greeting():
    print("hello!!")
    
def print_date(year, month, day):
    joined = str(year) + '-' + str(month)
