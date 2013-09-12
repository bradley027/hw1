# OCNG 689 Python for Geoscientists 
# HW 1
# Part 2: Function 
# This script will read in burl1 data and output wind components, 
# sea-level pressure, & dates (in datetime format) from created arrays.
# Notes:  
# 1) the wind components of speed & direction will be converted to 
# northward & eastward wind vectors. 
# 2) the entire array will not be displayed (i.e. [###, ... ###])
# 3) used different way of creating date data 
# 4) printed data arrays individually to see if that would make a difference 
#    in printing style 

import numpy as np
from datetime import datetime 

def burl1_read():
    f = open('burl1h2011.txt')

    #variable initilization (lists, not converted to arrays yet)
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

        #converting date data to real dates  
        year = (int(data[0]))
        month = (int(data[1]))
        day = (int(data[2]))
        hours = (int(data[3]))
        date.append(datetime(year, month, day, hours))

    #creating arrays 
    date = np.array(date)
    windsp = np.array(windsp)
    winddir = np.array(winddir)
    slp = np.array(slp)

    #converting wind speed & direction to vectors 
    Nwind_v = -windsp*np.cos(winddir)
    Ewind_u = -windsp*np.sin(winddir)
    
    print 'Date (year,month,day,hour): ', date 
    print 'Sea-level Pressure (mb): ', slp
    print 'Eastward wind (kts): ', Ewind_u
    print 'Northward wind (kts): ', Nwind_v

burl1_read()