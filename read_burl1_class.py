# OCNG 689 Python for Geoscientists 
# HW 1
# Part 3: Class 
# This script contains a class that will return a single instance of
# reading in burl1 data and output wind components, 
# sea-level pressure, & dates (in datetime format) from created arrays in the
# way that the original script (not the function) printed the data.
# Notes:  
# 1) the wind components of speed & direction will be converted to 
# northward & eastward wind vectors. 
# 2) the entire array will not be displayed (i.e. [###, ... ###])
# 3) used datetime.strptime object 
# 4) used data output instead of print data arrays individually

import numpy as np
from datetime import datetime 
from math import cos
from math import sin

class read_burl1():
    
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        
        f = open(self.name_of_file)
        slp = []
        windsp = []
        winddir = []
        date = []
        Nwind_v = [] 
        Ewind_u = []
        
        #data import to fill above lists (that will soon be arrays) 
        for line in f.readlines()[2:]:
            data = line.split() 
            slp.append(float(data[12]))
            windsp.append(float(data[6]))
            winddir.append(float(data[5])*(np.pi/180))
            # the above is converting the degrees to radians for upcoming conversion
            date.append(str(data[0]+ data[1]+ data[2]+ data[3]))

        #converting date string to datetime 
        date = [datetime.strptime(date[z],'%Y%m%d%H')for z in range(len(date))]
        
        #creating arrays 
        date_1 = np.array(date)
        windsp = np.array(windsp)
        winddir = np.array(winddir)
        slp = np.array(slp)

        #converting wind speed & direction to vectors 
        Nwind_v = -windsp*np.cos(winddir)
        Ewind_u = -windsp*np.sin(winddir)
        
        self.output = {'Date (year,month,day,hours)':date_1, 'Sea-level Pressure': slp,'Eastward Wind':Ewind_u, 'Northward Wind': Nwind_v}
        
        
    def __repr__(self):
        return self.output 
        
data = read_burl1('burl1h2011.txt')
print data.output