#series
from pandas import Series
se = Series([100,200,300], index=['a','b','c'])
se
se['b']
#converting dictionary to series
salary = {'John': 300,'Tim':4500,'Rob':5600}
se3 = Series(salary)
se3
se3['Rob']
#data frame
data = {'Name':['John','Tim','Rob'],
        'Age':[34,35,36],
        'Salary':[4500,3400,2300]
        }
from pandas import DataFrame
frame = DataFrame(data)
frame
new_frame = DataFrame(data, columns=['Agge','Name','Salary'])
new_frame
new_frame['Salary']
new_frame.ix[2]
#transposing
new_frame['Profile']="Doctor"
new_frame
new_frame['Education']="Ms"
new_frame
new_frame = new_frame.T
new_frame
#Reindexing
from pandas import Series
obj = Series([100,200,300,400,500], index=['d','e','a','b''c'])
obj
obj = obj.reindex(['a','b','c','d','e'])
#datframe
data = {'Name':['John','Tim','Rob'],
        'Age':[34,35,36],
        'Salary':[4500,3400,2300]
        }
from pandas import DataFrame
frame = DataFrame(data)
frame
frame=frame.reindex([0,2,1])
frame
fields = ['Name','Age','Salary']
frame=frame.reindex(columns=fields)
frame
#deletion
frame2= frame.drop([2])
frame2
frame3=frame.drop("Age",axis=1)
#Arithmetic operation
from pandas import Series
series1 = Series([1,2,3,4,5])
series2 = Series([100,200,300,400,500])
series1+series2


from pandas import DataFrame
data1 = {'Speed':[100,103,105],
         'Temp':[34,23,42]
         }
data2 = {'Speed':[100,103,105],
         'Temp':[34,23,42],
         'Humidity':[45,46,47]
         }
frame1=DataFrame(data1)
frame2=DataFrame(data2)
frame1+frame2

#operation in dataframe and series
series2 = Series([100,200,300], index=['Speed','Temp','Humidity'])
frame2+series2

series3 = Series([100,200],index=['Speed','Temp'])
series3
frame2+series3
#sorting series and dataframe
ser = Series([3,4,6,7,8,5,3,2], index=[2,3,5,7,6,9,4])
ser
ser.sort_index()

frame2 = frame2.reindex([2,1,0])
frame2
frame2.sort_index()

frame2 = frame2.reindex(columns = ["Speed","Humidity","Temp"])
frame2
frame2.sort_index(axis=1, ascending=False)

series2=Series([100,200,500,50],index=['S',['p','o','u']])
series2
series2.sort_values()

frame2.sort_value (by='Humidity')

#check for duplicate
series.index.is_unique
#sum
frame2.sum()
frame2.sum(axis=1)
frame2.idxmax()
frame2.idxmin()
#removing nan
from pandas import Series
import  numpy as np
ser = Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])
ser
ser = ser.dropna()
ser
frame2 = frame2.dropna()
#fillna value with 0
frame2.fillna(0)
frame2.fillna(100)
#loading data from file
import  pandas
data_frame = pandas.read_csv("PMTCT.csv")
data_frame

import  pandas
data_frame = pandas.read_json("PMTCT.json")
data_frame

import  pandas
data_frame = pandas.read_excel("PMTCT.xlsx")
data_frame

#analyzing file data
from  pandas import DataFrame
data_frame = DataFrame(data_frame,columns=['SN','Existing Concepts','Unnamed: 2','To be changed','Unnamed: 4'])
data_frame

data_frame = data_frame.drop([992])
data_frame

data_frame = data_frame.drop(['Unnamed2', axis=1])
data_frame
data_frame = data_frame.sort_values by='Unnamed2'
data_frame

data_frame.sum(numeric_only=True)
#numpy array
import  numpy as np
a=np.array([1,2,3,4])
print(a)
a.reshape(2,2)
#new way to create array
import numpy as np
a=np.array(24)
print(a)
b=a.reshape(2,4,3)
print(b)
x=np.zeros(5,dtype=np.int)
print(x)
#linspace
import numpy as np
x-np.linspace(10,20,5,endpoint=False)
print(x)
#logspace
a=np.logspace(1,0,2,0,num=10)
print(a)
#slicing
import numpy as np
a=np.arrange(10)
print(a)

s=slice(2,7,2)
print((a[s]))

b=a[2:7:2]
print(b)
print(a[2:5])
#multidimensional
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[2:])
#select 0th array 0th element then 1st array 1st element then 2nd array 0th element
b=a[[0,1,2],[0,1,0]]
print(b)
soln:[1,5,7]
row = np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
y=x[row,cols]
print(y)
print(x[x>5])
#broadcasting
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([1,2,3])
print(a)
print(b)
print(a+b)
#nditer
a=np.arrange(0,60,5)
a=a.reshape(3,4)
print(a)
for x in np.nditer(a):
    print(x)
#matplotlib for graph
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=2 * x + 5
plt.title("This is the title")
plt.xlabel("This is x label")
plt.ylabel("This is y label")
plt.plot(x,y)
plt.show()










































