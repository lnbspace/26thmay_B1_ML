Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> hello()
Hello this is Python
>>> abc(4,6,8)
0.25
>>> k = abc(4,6,8)
>>> k
0.25
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> abc(4,6,8)
2
>>> k = abc(4,6,8)
2
>>> k
>>> print(k)
None
>>> k1 = abc1(4,6,8)
>>> k1
0.25
>>> k1 = abc1(4,6)
>>> k1
4.0
>>> abc1(y=30,x=50)
39.0
>>> abc2(4,6,8,9,4,7,8,56,7,9,0)
11.727272727272727
>>> abc2()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    abc2()
  File "E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py", line 24, in abc2
    return 1+(sum(b)/len(b))
ZeroDivisionError: division by zero
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> abc2()
1.0
>>> abc2(4,6,8,9,4,7,8,56,7,9,0)
10.833333333333334
>>> abc3(name='someone',val = 30)
{'name': 'someone', 'val': 30}
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> func1(65)
1
>>> func1(66)
0
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> func2(34)
0
>>> func2(39)
1
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
Traceback (most recent call last):
  File "E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py", line 47, in <module>
    y = operate(a)
NameError: name 'a' is not defined
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
[8, 10, 12, 174, 68, 8, 198, 130]
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
[8, 10, 12, 174, 68, 8, 198, 130]
[0.4, 0.5, 0.6, 8.7, 3.4, 0.4, 9.9, 6.5]
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
[8, 10, 12, 174, 68, 8, 198, 130]
[0.4, 0.5, 0.6, 8.7, 3.4, 0.4, 9.9, 6.5]
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Even', 'Odd', 'Odd']
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
[1, 2, 0, 0, 1, 1, 0, 2]
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[4, 5, 6, 87, 34, 4, 99, 65]
[1, 2, 0, 0, 1, 1, 0, 2]
[4, 6, 34, 4]
>>> import keyword
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
hello
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
hello
130
>>> import os
>>> import math
>>> import datetime
>>> import sys
>>> import calendar
>>> import time
>>> import mymodule as mm # creating alias
>>> mm.message
'hello'
>>> from mymodule import message
>>> message
'hello'
>>> doubler
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    doubler
NameError: name 'doubler' is not defined
>>> from mymodule import message, doubler
>>> doubler(3)
6
>>> from mymodule import *
>>> val
30
>>> from mymodule import message as m
>>> m
'hello'
>>> from mymodule import message as m, val as v
>>> v
30
>>> m
'hello'
>>> import numpy
>>> import requests
>>> import bs4
>>> import keras
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    import keras
ModuleNotFoundError: No module named 'keras'
>>> import cv2
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'
>>> import pyautogui
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    import pyautogui
ModuleNotFoundError: No module named 'pyautogui'
>>> import openpyxl
>>> import pyautogui
>>> import cv2
>>> import webbrowser as wb
>>> wb.open_new('www.google.com/search?q=latest music')
True
>>> wb.open('www.google.com/search?q=latest music')
True
>>> wb.open('www.flipkart.com/search?q=latest phone')
True
>>> os.startfile(r'd:/banner.mp4')
>>> os.startfile(r'd:/banner.mp4')
>>> os.system('taskkill /im vlc.exe')
0
>>> print(calendar.calendar(2021))
                                  2021

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
One more line only
this is more content
in the same file
>>> r
'One more line only\nthis is more content\nin the same file'
>>> r1 = r.split('\n')
>>> r1
['One more line only', 'this is more content', 'in the same file']
>>> r1.insert(1,'Inserted through file handling')
>>> r1
['One more line only', 'Inserted through file handling', 'this is more content', 'in the same file']
>>> content = '\n'.join(r1)
>>> content
'One more line only\nInserted through file handling\nthis is more content\nin the same file'
>>> f = open('newfile.txt','w')
>>> f.write(content)
87
>>> f.close()
>>> content
'One more line only\nInserted through file handling\nthis is more content\nin the same file'
>>> type(content)
<class 'str'>
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
ID,Address,City,State,Country,Name,Employees
1,3666 21st St,San Francisco,CA 94114,USA,Madeira,8
2,735 Dolores St,San Francisco,CA 94119,USA,Bready Shop,15
3,332 Hill St,San Francisco,California 94114,USA,Super River,25
4,3995 23rd St,San Francisco,CA 94114,USA,Ben's Shop,10
5,1056 Sanchez St,San Francisco,California,USA,Sanchez,12
6,551 Alvarado St,San Francisco,CA 94114,USA,Richvalley,20

>>> r
"ID,Address,City,State,Country,Name,Employees\n1,3666 21st St,San Francisco,CA 94114,USA,Madeira,8\n2,735 Dolores St,San Francisco,CA 94119,USA,Bready Shop,15\n3,332 Hill St,San Francisco,California 94114,USA,Super River,25\n4,3995 23rd St,San Francisco,CA 94114,USA,Ben's Shop,10\n5,1056 Sanchez St,San Francisco,California,USA,Sanchez,12\n6,551 Alvarado St,San Francisco,CA 94114,USA,Richvalley,20\n"
>>> r.index("Ben's Shop")
262
>>> r1 = r.split('\n')
>>> r1
['ID,Address,City,State,Country,Name,Employees', '1,3666 21st St,San Francisco,CA 94114,USA,Madeira,8', '2,735 Dolores St,San Francisco,CA 94119,USA,Bready Shop,15', '3,332 Hill St,San Francisco,California 94114,USA,Super River,25', "4,3995 23rd St,San Francisco,CA 94114,USA,Ben's Shop,10", '5,1056 Sanchez St,San Francisco,California,USA,Sanchez,12', '6,551 Alvarado St,San Francisco,CA 94114,USA,Richvalley,20', '']
>>> r1 = r1[:-1]
>>> r1
['ID,Address,City,State,Country,Name,Employees', '1,3666 21st St,San Francisco,CA 94114,USA,Madeira,8', '2,735 Dolores St,San Francisco,CA 94119,USA,Bready Shop,15', '3,332 Hill St,San Francisco,California 94114,USA,Super River,25', "4,3995 23rd St,San Francisco,CA 94114,USA,Ben's Shop,10", '5,1056 Sanchez St,San Francisco,California,USA,Sanchez,12', '6,551 Alvarado St,San Francisco,CA 94114,USA,Richvalley,20']
>>> cols = r1[0].split(',')
>>> cols
['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']
>>> r2 = list(map(lambda x:x.split(','), r1[1:]))
>>> r2
[['1', '3666 21st St', 'San Francisco', 'CA 94114', 'USA', 'Madeira', '8'], ['2', '735 Dolores St', 'San Francisco', 'CA 94119', 'USA', 'Bready Shop', '15'], ['3', '332 Hill St', 'San Francisco', 'California 94114', 'USA', 'Super River', '25'], ['4', '3995 23rd St', 'San Francisco', 'CA 94114', 'USA', "Ben's Shop", '10'], ['5', '1056 Sanchez St', 'San Francisco', 'California', 'USA', 'Sanchez', '12'], ['6', '551 Alvarado St', 'San Francisco', 'CA 94114', 'USA', 'Richvalley', '20']]
>>> d = dict(zip(cols,zip(*r2)))
>>> d
{'ID': ('1', '2', '3', '4', '5', '6'), 'Address': ('3666 21st St', '735 Dolores St', '332 Hill St', '3995 23rd St', '1056 Sanchez St', '551 Alvarado St'), 'City': ('San Francisco', 'San Francisco', 'San Francisco', 'San Francisco', 'San Francisco', 'San Francisco'), 'State': ('CA 94114', 'CA 94119', 'California 94114', 'CA 94114', 'California', 'CA 94114'), 'Country': ('USA', 'USA', 'USA', 'USA', 'USA', 'USA'), 'Name': ('Madeira', 'Bready Shop', 'Super River', "Ben's Shop", 'Sanchez', 'Richvalley'), 'Employees': ('8', '15', '25', '10', '12', '20')}
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
ID,Address,City,State,Country,Name,Employees
1,3666 21st St,San Francisco,CA 94114,USA,Madeira,8
2,735 Dolores St,San Francisco,CA 94119,USA,Bready Shop,15
3,332 Hill St,San Francisco,California 94114,USA,Super River,25
4,3995 23rd St,San Francisco,CA 94114,USA,Ben's Shop,10
5,1056 Sanchez St,San Francisco,California,USA,Sanchez,12
6,551 Alvarado St,San Francisco,CA 94114,USA,Richvalley,20

{'ID': ('1', '2', '3', '4', '5', '6'), 'Address': ('3666 21st St', '735 Dolores St', '332 Hill St', '3995 23rd St', '1056 Sanchez St', '551 Alvarado St'), 'City': ('San Francisco', 'San Francisco', 'San Francisco', 'San Francisco', 'San Francisco', 'San Francisco'), 'State': ('CA 94114', 'CA 94119', 'California 94114', 'CA 94114', 'California', 'CA 94114'), 'Country': ('USA', 'USA', 'USA', 'USA', 'USA', 'USA'), 'Name': ('Madeira', 'Bready Shop', 'Super River', "Ben's Shop", 'Sanchez', 'Richvalley'), 'Employees': ('8', '15', '25', '10', '12', '20')}
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']
['1', '3666 21st St', 'San Francisco', 'CA 94114', 'USA', 'Madeira', '8']
['2', '735 Dolores St', 'San Francisco', 'CA 94119', 'USA', 'Bready Shop', '15']
['3', '332 Hill St', 'San Francisco', 'California 94114', 'USA', 'Super River', '25']
['4', '3995 23rd St', 'San Francisco', 'CA 94114', 'USA', "Ben's Shop", '10']
['5', '1056 Sanchez St', 'San Francisco', 'California', 'USA', 'Sanchez', '12']
['6', '551 Alvarado St', 'San Francisco', 'CA 94114', 'USA', 'Richvalley', '20']
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
Traceback (most recent call last):
  File "E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py", line 132, in <module>
    r = json.load('supermarkets.json')
  File "C:\Users\hp\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day5/script_filie.py ===========
[{'ID': 1, 'Address': '3666 21st St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': 'Madeira', 'Employees': 8}, {'ID': 2, 'Address': '735 Dolores St', 'City': 'San Francisco', 'State': 'CA 94119', 'Country': 'USA', 'Name': 'Bready Shop', 'Employees': 15}, {'ID': 3, 'Address': '332 Hill St', 'City': 'San Francisco', 'State': 'California 94114', 'Country': 'USA', 'Name': 'Super River', 'Employees': 25}, {'ID': 4, 'Address': '3995 23rd St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': "Ben's Shop", 'Employees': 10}, {'ID': 5, 'Address': '1056 Sanchez St', 'City': 'San Francisco', 'State': 'California', 'Country': 'USA', 'Name': 'Sanchez', 'Employees': 12}, {'ID': 6, 'Address': '551 Alvarado St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': 'Richvalley', 'Employees': 20}]
>>> f1 = open('supermarkets.json','r');
>>> r1 = f1.read()
>>> print(r1)
[
  {
    "ID": 1,
    "Address": "3666 21st St",
    "City": "San Francisco",
    "State": "CA 94114",
    "Country": "USA",
    "Name": "Madeira",
    "Employees": 8
  },
  {
    "ID": 2,
    "Address": "735 Dolores St",
    "City": "San Francisco",
    "State": "CA 94119",
    "Country": "USA",
    "Name": "Bready Shop",
    "Employees": 15
  },
  {
    "ID": 3,
    "Address": "332 Hill St",
    "City": "San Francisco",
    "State": "California 94114",
    "Country": "USA",
    "Name": "Super River",
    "Employees": 25
  },
  {
    "ID": 4,
    "Address": "3995 23rd St",
    "City": "San Francisco",
    "State": "CA 94114",
    "Country": "USA",
    "Name": "Ben's Shop",
    "Employees": 10
  },
  {
    "ID": 5,
    "Address": "1056 Sanchez St",
    "City": "San Francisco",
    "State": "California",
    "Country": "USA",
    "Name": "Sanchez",
    "Employees": 12
  },
  {
    "ID": 6,
    "Address": "551 Alvarado St",
    "City": "San Francisco",
    "State": "CA 94114",
    "Country": "USA",
    "Name": "Richvalley",
    "Employees": 20
  }
]
>>> type(r1)
<class 'str'>
>>> type(r)
<class 'list'>
>>> r[0]
{'ID': 1, 'Address': '3666 21st St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': 'Madeira', 'Employees': 8}
>>> r[0]['Address']
'3666 21st St'
>>> r1
'[\n  {\n    "ID": 1,\n    "Address": "3666 21st St",\n    "City": "San Francisco",\n    "State": "CA 94114",\n    "Country": "USA",\n    "Name": "Madeira",\n    "Employees": 8\n  },\n  {\n    "ID": 2,\n    "Address": "735 Dolores St",\n    "City": "San Francisco",\n    "State": "CA 94119",\n    "Country": "USA",\n    "Name": "Bready Shop",\n    "Employees": 15\n  },\n  {\n    "ID": 3,\n    "Address": "332 Hill St",\n    "City": "San Francisco",\n    "State": "California 94114",\n    "Country": "USA",\n    "Name": "Super River",\n    "Employees": 25\n  },\n  {\n    "ID": 4,\n    "Address": "3995 23rd St",\n    "City": "San Francisco",\n    "State": "CA 94114",\n    "Country": "USA",\n    "Name": "Ben\'s Shop",\n    "Employees": 10\n  },\n  {\n    "ID": 5,\n    "Address": "1056 Sanchez St",\n    "City": "San Francisco",\n    "State": "California",\n    "Country": "USA",\n    "Name": "Sanchez",\n    "Employees": 12\n  },\n  {\n    "ID": 6,\n    "Address": "551 Alvarado St",\n    "City": "San Francisco",\n    "State": "CA 94114",\n    "Country": "USA",\n    "Name": "Richvalley",\n    "Employees": 20\n  }\n]'
>>> json.loads(r1)
[{'ID': 1, 'Address': '3666 21st St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': 'Madeira', 'Employees': 8}, {'ID': 2, 'Address': '735 Dolores St', 'City': 'San Francisco', 'State': 'CA 94119', 'Country': 'USA', 'Name': 'Bready Shop', 'Employees': 15}, {'ID': 3, 'Address': '332 Hill St', 'City': 'San Francisco', 'State': 'California 94114', 'Country': 'USA', 'Name': 'Super River', 'Employees': 25}, {'ID': 4, 'Address': '3995 23rd St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': "Ben's Shop", 'Employees': 10}, {'ID': 5, 'Address': '1056 Sanchez St', 'City': 'San Francisco', 'State': 'California', 'Country': 'USA', 'Name': 'Sanchez', 'Employees': 12}, {'ID': 6, 'Address': '551 Alvarado St', 'City': 'San Francisco', 'State': 'CA 94114', 'Country': 'USA', 'Name': 'Richvalley', 'Employees': 20}]
>>> 