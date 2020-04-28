# python

# https://www.learnpython.org/en/Welcome

# this means that if this script is executed, then main() will be executed
if __name__ == '__main__':
    main()

Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

# Pandas
Pandas is a high-level data manipulation tool developed by Wes McKinney. It is built on the Numpy package and its key data structure is called the DataFrame. DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

## Packaging Unpacking
i/p -->
    t=(1,2,3,4)
    (a,b,c,d)=t
    print(a)
    print(b)
    print(c)
o/p -->
    1
    2
    3
## Functions of an object -- Here tuple
i/p -->
    t=()
    print(dir(t))
o/p -->
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
    
# Tuples --> No bracket or () brackets
# Lists --> [] Square brackets
# Sets --> {} brackets or set(<list_object>) or  set(<tuple_object>) --> Empty Sets --> set({})
Example
a = {1,2,3,4,5,6,6,7,8}
# Dictionary --> {} Key Value Pairs
Example 
x = {'India' : 'INR', 'New Zealand' : 'NZD'}
value = x.get('Australia', 'NA') # Value not present
o/p --> NA
