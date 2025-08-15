#!/usr/bin/env python3
import sys
import pandas as p
import json
from EmployeeClasses import Employee, Manager


script_name = sys.argv[0]
arguments = sys.argv[1:]
argLen = len(arguments)
print(f"Executing script : {script_name}")

if argLen == 0:
    print('Missing command line argument')
    #sys.exit(1)
else:
    #different ways of formatting a string
    print(f'Checking even odd for input val= {arguments[0]} and argCount = {argLen}')
    num = int(arguments[0])  #Default data type for sys.argv is str
    if num%2 == 0:
        	print('even')
    elif num%2 != 0:
        	print('odd')

print(type(range(0,10)))

i=2

print('while loop:')
while i>0:
    print(i)
    i=i-1
  
print('for loop:')
for i in range(10):
    i=i+1
    if i==2:
        continue
    elif i == 6:
        break
    else:
     print(i)
    
b = 'abc'
print(b[1])
#b[1]='B' this cant be done as strings are immutable
b='xyz' #this is string overriding
print(b) 
c = b.upper()
for i in c:
    print(i)
    
d='123'
print(int(d))
# print(int(c)) cant be done

e=1234
f=str(e)
print('Reversed string/number =',f[::-1])

def donut(count):
    if count > 5:
        return 'Number of dounts is many'
    else:
        return 'Number of dounts is ' + str(count)
    
print(donut(5))
        
#Function to return first 2 characters and the last two characters of a string        
def strFunc(str):
    if len(str) <=2 :
        return ''
    return str[:2] + str[-2:]
        
print(strFunc('Spring'))  

#Function to replace re-occurence of 1st character by stars
def starrify(str):
    return str[0] + str[1:].replace(str[0], '*')

print(starrify('babble'))

#Function that takes an array of strings and returns count of strings
# where size is greater than 1 and 1st and last characters are the same
def matchEnds(words):
    count = 0
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            count += 1
    return count

words = ['ata','f','babble','eerie','yay']
print(matchEnds(words))      
            
#Function that takes an array of words and returns sorted list
#with words starting with x sorted first followed by other words
def sortXfirst(words):
    xList = []
    otherList = list() #two ways to make empty list
    for word in words:
        if word.startswith('x'):
            xList.append(word)
        else:
            otherList.append(word) 
    return sorted(xList) + sorted(otherList) 

words = ['atad','xf','xinjaou','eerie','yay']
print(sortXfirst(words))      

#Check if ab exists in value lists in a dictionary
dic = {1:['ab','bc'], 2:['ef', 'gh']}
abExists = False
for valList in dic.values():
    if 'ab' in valList:
        abExists = True
        break
print('abExists=' + str(abExists))

#Try-Catch with file operations
try:
    f=open('MyFile.txt', 'r')
    #print(f.read())  #reads entire file
    for line in f.readlines():  #reads file into memory and returns array of lines
        for w in line.split():  #split() splits line by white spaces
            print(w)
except IOError as e:  #Give a wrong file name above and see this exception
    print('IO error - '+str(e))
except Exception as e:
    print('Some error -'+str(e))
else:
    print('No exception occured.')         

f=open('FileToWrite.txt', 'w') #w mode creates file or over writes existing contents
f.write("Hello\n")
f.write("World 1\n")
f.close()

f=open('FileToWrite.txt', 'a') #a mode appends data in exisiting file
f.write("Hello\n")
f.write("World 2\n")
f.close()

f=open('FileToWrite.txt', 'r+')  #r+ mode for both read and write
f.write("Rplus\n")
f.write("Mode\n")
line=f.read()
print(line)
f.close()

# you can pass functions as parameters to other functions
def PrintIt(x):
    print("Value = "+str(x)+"\n")
    
def CallAnotherFunc(f,x):
    return f(x)

CallAnotherFunc(PrintIt, 3)

#Lambdas let you inline simple functions (equivalent to a func taking an arg and returning a value)
print(CallAnotherFunc(lambda x: x*x, 3))

#sort dictionary based on Values using Lambda 
map = {1:'a', 2:'d', 3: 'c', 4: 'b'}
print(sorted(map.items(), key=lambda x:x[1]))

#Zip creates a multiple Tuple
list1 = [1,2,3]
list2 = (4,5,6,7)
list3 = list(zip(list1,list2))
print(list3)

#DP in python
a=[1,2,3]
b=[]
for i in a:
    b+=[i]  #equal to b.append(i)

print(b)

#Pandas
employees=p.read_csv('Employee.csv')
print(employees)

#DataFrames
df = p.DataFrame(data=[['Alex',10],['Ramit',100],['Clarke',13],['Gulati',100],['Bob',12]],
                  index=['A','B','C','D','E'],
                  columns=['Name', 'Salary'])
df=df.sort_values(by=['Salary','Name'], ascending=[False,True])
print(df)
print(df.to_json())

#Object Oriented Programming
emp1 = Employee(1, "Modi", "IT", "1000")
print(emp1.toString())  

manager = Manager(2, "Ramit", "IT", "100000", "A")
print(manager.toString())  #Runtime polymorhism

manager.appraisal()
manager.appraisal(15)

#Using custom class objects as keys in dictionary; or removing duplicates from set
emp2 = Employee(3, "Sodhi", "HR", "1")
emp3 = Employee(3, "Sodhi", "SALES", "10")

employee_set = set()
employee_set.add(emp1)
employee_set.add(emp2)
employee_set.add(emp3)
print(len(employee_set)) #Duplicate object not present

names = ('a','b','c','d','e')
scores = (1,2,3,4,5)
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5))) # o/p is {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5};
# you can also do list(zip(..) would give o/p like [(a,1), (b,2)...etc]
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)
print(A6)


# A generator function 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
# x is a generator object 
x = simpleGeneratorFun() 
  
# Iterating over the generator object using next 
print(x.__next__()) # In Python 3: __next__() , Python 2: next()
print(x.__next__()) 
print(x.__next__()) 
#Calling more next than yields, will cause exception

# Convert json (name-city pairs) string to dict of name-city pairs
# note we imported json module at the top
jsonStr = '[{"name": "ramit","city": "delhi"}, {"name": "warner","city": "sydney"}]'
jsonData = json.loads(jsonStr)
name_dict = {}
for obj in jsonData:
     name_dict[obj['name']] = obj['city']
print(name_dict)

#Multithreading example
import threading

#Python threads dont return values, capture them in a shared context instead.
results = [None]*3  # sizethe array to avoid index out of bounds 
def worker(name, result_container, index):
    print(f"Thread {name} starting")
    result_container[index] = f'Hello from thread {name}'
    # Simulate I/O task
    import time; time.sleep(2)
    print(f"Thread {name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Worker-{i}",results, i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for result in results:
    print(result);

# Make HTTP call
import requests

response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
if response.status_code == 200:
    responseBody = response.json()  # Converts response body to a Python dict
    print(responseBody) 
    print(responseBody[0]['email']) #print a specific field in the list of responses
