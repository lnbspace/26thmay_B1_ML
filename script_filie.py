##Data Types
##Built-in Functions
##Python Scripting
##    if-else, while, for
##User defined Functions
##Module/Libraries
##    file handling
##        csv, json, xls
##    os
##    webbrowser
##
##Application - GUI

##def hello():
##    print('Hello this is Python')
##
##def abc(x,y,z):
##    print(x+y-z)
##
##def abc1(x=1,y=0,z=2):
##    return (x+y-z)/z
##
##def abc2(*b):
##    return 1+(sum(b)/(len(b)+1))
##
##def abc3(**k):
##    return k

# One liner functions - Lambda Expressions (Annonymous Functions)

##def func1(n):
##    return n%2
##
##func2 = lambda n:n%2


##x = [4,5,6,87,34,4,99,65]
##print(x)

##def operate(a):
##    c = []
##    for i in a:
##        c.append(i*2)
##    return c
##
##def operate1(a):
##    c = []
##    for i in a:
##        c.append(i/10)
##    return c

##y = operate(x)
##print(y)
##
##y1 = operate1(x)
##print(y1)

##def operate(f,a):
##    c = []
##    for i in a:
##        c.append(f(i))
##    return c
##
##y = operate(lambda n:n*2, x)
##print(y)
##
##y1 = operate(lambda n:n/10, x)
##print(y1)
##
##y2 = operate(lambda n:'Even' if not n%2 else 'Odd', x)
##print(y2)

##y3 = list(map(lambda n:n%3, x))
##print(y3)
##
##y4 = 
##print(y4)


##import mymodule
##
##print(mymodule.message)
##print(mymodule.doubler(65))

#################################################################
# Working with Data/Files

# Bare File Handling
##f = open('mytext.txt','w')
##f.write('One line only')
##f.close()

##f = open('newfile.txt','w') # writing fresh data
##f.write('One more line only')
##f.close()

##f = open('newfile.txt','a') # appending data to it
##f.write('\nthis is more content\nin the same file')
##f.close()

##f = open('newfile.txt','r')
##r = f.read()
##print(r)
##f.close()
##
##r1 = r.split('\n')
##r1.insert(1,'Inserted through file handling')
##content = '\n'.join(r1)
##f = open('newfile.txt','w')
##f.write(content)
##f.close()

##import csv
##import json

##f = open('supermarkets.csv','r')
##r = f.read()
##f.close()
##print(r)
##
##r1 = r.split('\n')[:-1]
##cols = r1[0].split(',')
##r2 = list(map(lambda x:x.split(','), r1[1:]))
##d = dict(zip(cols,zip(*r2)))
##print(d)

##f = open('supermarkets.csv','r')
##data = csv.reader(f)
##for r in data:
##    print(r)

##f = open('supermarkets.json','r')
##r = json.load(f)
##print(r)

# json.dump()
# json.loads()
# json.dumps()





























        
