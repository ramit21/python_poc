# python_poc
## Python POC


Python is dynamic, interpreted language. There are no type declation of variables, paramters or functions. This makes code short and flexible, but you lose the compiler time type checking of the source code. Python tracks type of variables at runtime. Being interpreted, its read first and execute later, so all function etc should be defined before use.

Setup Python on local:
1. Install Anaconda from https://www.anaconda.com/download
2. After installation, launch Jupyter and Spyder(IDE)
3. Verify python installation by typing python —version on cmd promp
4. Run the POC script on command line with an argument value:
	:> python PythonConcepts.py 10
	
———————————————————————————————  
**Learnings:**

On cmd prompt, type python, it opens python prompt, then type following  
var = 10  
var —> prints 10  
type(var) —> prints int  

Commonly used data types - string, range, int, float, long, boolean, enum etc.  
———————————————————————————————  
## Typecasting in py:

a= “hi”  
b= len(a). — gives 2  
a+b — error  
a+str(len(a)) — gives hi2  
String in python is indexed, hence is also used as a data structure (like array or list)  
str[lower limit inc : upper limit not included : stepsize] -> substring. eg str[::2], str[1:3]  
Hello : indexes start from 0 from left, and also from -1 from the right  
So H has indexes 0 and -5, e has 1/-4, and o has 4/-1  
import sys -> includes sys module  
dir(sys) -> shows everything abt a mdule  
sys.exit(0) takes you out of python cmd prompt  
help(sys.argv) — gives u help on argv  
Note that Python demands that code is properly formatted  
_ is a special command in python (just like $ in unix), gives result of last called function  
———————————————————————————————  
## Python data structures:

**List**: (indexed linked lists). eg. colors = [’abc’, ‘def’ , ‘ghi’]  
split(‘’) function returns a list  
if ‘def’ in colors:  #list.contains of python  
list methods: list.sort, list.append, insert 
sorted(arr, key=len, reverse=True) Using key we specify how to sort the list, reverse=True for reverse sort  
Unpacking ->   
a,b,c = [1,2,3]. #Variables on left should match te size of the list  
list.insert(index, elemnt)  
list.remove(element)  

**Tuple**:  
x=(1,2,3) Or x=tuple([1,2,3])  
x[0] is 1, x[-1] is 3;; x[0]=10 gives error, append is also not allowed on tuples  
Tuples support indexing and slicing just as in Lists  
List in pyton is mutable, but tuple is not  
Python supports list within list, or tuple within tuple  

**Set**: removes duplicates  
s=set() #Empty set  
s=set([1,2,3,1,2])  
Set does not support inexing, so s[0] will give an error  
Set is also immutable (just like tuple) so you can’t append, you can still remove  
When creating a set of objects of custom class, you can override __eq__ method in the class  
I can type cast set/tuple into a new list  

**Dictionary**: Key Value pairs. Key can be anything except list/tuple/set  
dict = {‘key1’:’Val1’, ‘key2’: ‘val2’}  
if ‘key1’ in dict:    #Avoid KeyError  
for key in dict : #by default iterates over keys of dictionary  
dict.keys() -> returns tuple of keys of dictionary   
dict.values() -> returns tuple of values of dictionary  
dict.items() -> returns entire dictiionary with key value pairs  
if key <> dict[key]:   #To check if key is present in the dictionary  
	dict[ky] = some Value  
	
Unpacking: for k,v in dict.items():  
                print( key = k, value = v)  
———————————————————————————————  
## File handling:  

f= open(‘name’, ‘r’) opens the file into variable f  
Various modes:  
r: Read  
w: Write (overrite the content if already existing)  
a: Append to an existing file  
r+: read/write  
for i in f:  
  print(i)  # prints the file line by line  
f.read(): reads all the file in a single line  
f.readLine() reads all the file into memory and returns its contents as a list of lines.  
———————————————————————————————  
## NumPy pandas: 
**NumPy**:    
Useful when operating on large data sets. Saves code and memory compared to oprating on normal Lists. T
his feature has been taken from Matlab. R came with these features, then Python came with this Numpy package. 
Full form - “Numercal Python”. Good for Data analaytics.
Numpy package is written in Cython(C+Python)  
import numpy as np -> then use np in code  
List is a linked list, Numpy provides Array  
a = np.array(someList) -> gives Array  
a.ndim -> gives 1; n.shape -> gives (4,)  meaning 4 rows, and no columns  
a=a*5 -> multiplies all elements by 5  
a+b -> adds all elements of a and b index by index  
np.ones((4,5)) -> creates 2 D array of 4X5 with values 1  
np.emty(5) ->   array of 5 non elelemtns. there is no null/undefined in python, there are None and Nan  
np.linspace(1,10,5,endpoint=false) -> gives an array of 5 equal partitions of range 1-10 -> very useful for generating graphs  
np.arrange(1,10,1) -> gives array of [1,2,3…… 9]  
np.arrange(0,8,5) -> [0,5]  
np.full (2,2,7)-> constand array 2X2 with value of 7  
np.eye(3) -> gives 3X3 Identity matrix (T=T’) of random numbers using uniform distribution  
np.random.rand(3,4) -> generates 2 d array 3X4 with random values in range (0,1). 
You can get random numbers above 1 also by specifying spl paramaters:  
np.random.randn(4,5) -> generates +ve and -ve values, values this time can go beyonf 1 or -1  
np.random.randint(2,5,10) -> generates an array of 10 elements, with int values in the range (1,5)  
Numpy supports basic indexing, slicing and reversing as in case of lists  
SciPy (Scientific Python) is often mentioned in the same breath with NumPy. 
SciPy extends the capabilities of NumPy with further useful functions for minimization, regression, 
Fourier-transformation and many others.  
———————————————————————————————  
**Pandas**: Used for processing of structured data, and process it in tabular format.  
import panda as pd  
data = pd.DataFrame((‘Country’: [‘Russia’,’Columbia’,’India’],  
					‘Rank’: [121,4,10]))  
data.sort_values(by=[field1,field2], ascending= , inplace = true)  
data.drop_duplicates() -> removes duplicate (entire row being duplicate)  
data.drop_duplicates(subset=‘Country’) -> removes duplicates (as per the given column  
pd.read_csv(‘csv file ’) -> reads csv data into tabular format  

import panda as pd  
from pandas series,dataFrame. -> for series and dataFrame functions  
s=pd.series([1,2,3]) -> creates with default indexes 0,1,2  
s=pd.series([1,2,3], indexes=[‘A’,B’,’C’]) -> creates data against given indices  

**DataFrame** is used to process data in tabular (2-D) struture. 
Good for processing Json files with keys as rows and values as data columns  
df=p.dataframe(list, indexes=, columns = )  
df.describe() -> shows entire dataFrame  
df[df[‘A’] > df[‘B’]] -> just like Sql select where clause  
groupBy is also supported  
df.to_csv(‘fileName’)-> converts dataFrame to csv file  
df.to_json(..)-> converts dataFrame to json  
import json  
json.load(path to json file)  
———————————————————————————————  
## Database connection:   
(using cx_Oracle)  

import cx_Oracle  
connection = cx_Oracle.connect('user/pass@someserver:port')    
cursor = connection.cursor()  
cursor.execute('select sysdate from dual')  
  
for row in cursor:  
    print row  
connection.close()  
———————————————————————————————  
## Machine Learning :  

using sklearn package  
sklearn.model_Selection import train_test_split  
sklearn.ensemble import RandomForestClassifier  
sklearn.cross_validation import cross_val_score  
sklearn.metrics import accuracy_score  

------------------------------
## Q&A:

Q. What is monkey patching in Python?
Ans. Dynamic modifications of a class or module at run-time. Consider the below example:

 m.py
class MyClass:
    def f(self):
        print "f()"

We can then run the monkey-patch testing like this:
import m
def monkey_f(self):
    print "monkey_f()"
 
m.MyClass.f = monkey_f
obj = m.MyClass()
obj.f()

The output will be as below:

monkey_f()


Q. Mention the differences between Django, Pyramid and Flask.
A. Flask is a “microframework” primarily build for a small application with simpler requirements. In flask, you have to use external libraries. Flask is ready to use.
Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.
Django can also used for larger applications just like Pyramid. It includes an ORM.


Q. You are required to scrap data from IMDb top 250 movies page. It should only have fields movie name, year, and rating.
Ans.
from bs4 import BeautifulSoup
 
import requests
import sys
 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
 
for movie in tr:
title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
row = title + ' - ' + year + ' ' + ' ' + rating
 
print(row)


Q. How to create custom exception classes?
A. It should inherit BaseException class.


Q. 
