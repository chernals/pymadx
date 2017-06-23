# pybdsim._General - general python scripts / tools
# Version 1.0
# L. Nevay, S.T.Boogert
# laurie.nevay@rhul.ac.uk

"""
General utilities for day to day housekeeping
"""

import os
import pymadx.Tfs
import pymadx.Aperture

def CheckFileExists(filename):
    i = 1
    parts = filename.split('.')
    basefilename = parts[0]
    if len(parts) > 1:
        extension = '.' + parts[1]
    else:
        extension = ''
    while os.path.exists(filename) :
        filename = basefilename+str(i)+extension
        i = i + 1
    return filename

def Chunks(l, n):
    """ Yield successive n-sized chunks from l.    """
    return [l[i:i+n] for i in range(0,len(l),n)]

def NearestEvenInteger(number):
    number = int(number)
    return number + number%2

def Cast(string):
    """
    Cast(string)
    
    tries to cast to a (python)float and if it doesn't work, 
    returns a string

    """
    try:
        return float(string)
    except ValueError:
        return string

def IsFloat(stringtotest):
    try:
        float(stringtotest)
        return True
    except ValueError:
        return False

def IndexOfElement(tfsinstance,markername):
    t = tfsinstance
    names = list(t.data['NAME'])
    try:
        i = names.index(markername)
    except ValueError:
        i = 0
        print 'Unknown element name'
    return i

def CheckItsTfs(tfsfile):
    """
    Ensure the provided file is a Tfs instance.  If it's a string, ie path to
    a tfs file, open it and return the Tfs instance.
    
    tfsfile can be either a tfs instance or a string.
    """
    if type(tfsfile) == str:
        madx = pymadx.Tfs(tfsfile)
    elif type(tfsfile) == pymadx.Tfs:
        madx = tfsfile
    else:
        raise IOError("Not pymadx.Tfs file type: "+str(tfsfile))
    return madx

def CheckItsTfsAperture(tfsfile):
    """
    Ensure the provided file is an Aperture instance.  If it's a string, ie path to
    a tfs file, open it and return the Tfs instance.
    
    tfsfile can be either a tfs instance or a string.
    """
    if type(tfsfile) == str:
        aper = pymadx.Aperture.Aperture(tfsfile)
    elif type(tfsfile) == pymadx.Aperture.Aperture:
        aper = tfsfile
    else:
        raise IOError("Not pymadx.Aperture.Aperture file type: "+str(tfsfile))
    return aper
