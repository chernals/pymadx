import re as _re
import pylab as _pl

#***********************************************************************************************    
class Inrays : 
    '''Class to store madx ptc input rays
    x  : horizontal position [m]
    px : horizontal canonical momentum p_x/p_0 
    y  : vertical position [m]
    py : vertical canonical momentum p_y/p_0
    t  : c*(t-t0)
    pt : (delta-E)/(pc)
    '''

    def __init__(self) :
        self.x  = []
        self.px = [] 
        self.y  = []
        self.py = []
        self.t  = []
        self.pt = []
       
    def addParticle(self,x=0.0,px=0.0,y=0.0,py=0.0,t=0.0,pt=0.0) : 
        '''Add new particle to internal lists'''
        self.x.append(x)
        self.px.append(px)
        self.y.append(y)
        self.py.append(py)
        self.t.append(t)
        self.pt.append(pt)

    def clear(self) : 
        '''Empty internal lists'''
        self.x  = []
        self.px = []
        self.y  = [] 
        self.py = [] 
        self.t  = []
        self.pt = []

    def nParticles(self) : 
        '''Gives the number of rays in the structure'''
        return len(self.x)
    
    def stats(self) : 
        '''Returns moments and beam parameters as quick cross check'''
        
#***********************************************************************************************    
def LoadInrays(fileName) : 
    '''Load input rays from file
    fileName : inrays.madx 
    return   : Inrays instance''' 
    i = Inrays()
    
    # open file 
    f = open(fileName) 
    for l in f : 
        inre_x  = _re.search('\s*x\s*=\s*([0-9.eE+-]+)\s*',l)
        inre_px = _re.search('\s*px\s*=\s*([0-9.eE+-]+)\s*',l)
        inre_y  = _re.search('\s*y\s*=\s*([0-9.eE+-]+)\s*',l)
        inre_py = _re.search('\s*py\s*=\s*([0-9.eE+-]+)\s*',l)
        inre_t  = _re.search(' t\s*=\s*([0-9.eE+-]+)\s*',l)
        inre_pt = _re.search('\s*pt\s*=\s*([0-9.eE+-]+)\s*',l)

        if inre_x : 
            x = float(inre_x.group(1))
        else :
            x = 0.0
        if inre_px : 
            px = float(inre_px.group(1))
        else : 
            px = 0.0 
        if inre_y : 
            y  = float(inre_y.group(1))
        else : 
            y  = 0.0
        if inre_py :             
            py = float(inre_py.group(1))
        else : 
            py = 0.0
        if inre_t :             
            t  = float(inre_t.group(1))
        else : 
            t = 0.0

        pt = float(inre_pt.group(1))

        i.addParticle(x,px,y,py,t,pt)
        

    print 'LoadInrays> Loaded ',i.nParticles()
    return i

#***********************************************************************************************    
def WriteInrays(fileName, i) : 
    
    f = open(fileName, 'w') 
    
    for c in range(0,i.nParticles(),1) : 
        ptcLine = 'ptc_start, x='+str(i.x[c]) + ', px='+str(i.px[c])+', y='+str(i.y[c])+', py='+str(i.py[c])+', t='+str(i.t[c])+', pt='+str(i.pt[c])+';\n'
        f.write(ptcLine)

    f.close()



#***********************************************************************************************    
def PlotIntrays(i) : 
    '''Plot Inrays instance, if input is a sting the instance is created from the file'''    

    if type(i) == str : 
        i = LoadInrays(i)
        
    _pl.figure(1) 
    _pl.clf()

    _pl.subplot(3,2,1)    
    _pl.hist(i.x,50,histtype='step')
    _pl.subplot(3,2,2)    
    _pl.hist(i.px,50,histtype='step')

    _pl.subplot(3,2,3)    
    _pl.hist(i.y,50,histtype='step')
    _pl.subplot(3,2,4)    
    _pl.hist(i.py,50,histtype='step')

    _pl.subplot(3,2,5)    
    _pl.hist(i.t,50,histtype='step')
    _pl.subplot(3,2,6)    
    _pl.hist(i.pt,50,histtype='step')

#***********************************************************************************************    
class Generator : 
    '''Simple ptx inray file generator'''
    
    def __init__(self,
                 gemx = 1e-8, betax = 0.1, alfx = 0.0 , 
                 gemy = 1e-8, betay = 0.1, alfy = 0.0,
                 sigmat = 1e-6, sigmapt= 1e-6) : 
        '''Simple gaussian beam
        gemx   : x geometric emittance 
        betax  : x beta function
        alfx   : x alpha function
        gemy   : y geometric emittance
        betay  : y beta function
        alfy   : y alpha function 
        sigmat : gaussian spread in time around the reference time 
        sigmapt: gaussian spread in relative energy 
        '''
        
        self.gemx    = gemx
        self.betax   = betax
        self.alfx    = alfx
        self.gemy    = gemy
        self.betay   = betay
        self.alfy    = alfy 
        self.sigmat  = sigmat 
        self.sigmapt = sigmapt

    def __repr__(self) : 
        return ""

    def generate(self, nToGenerate) : 
        ''' returns a Inrays structure''' 
        i = Inrays()
        
        for c in range(0,nToGenerate,1) : 
            i.AddParticle() 

        return i