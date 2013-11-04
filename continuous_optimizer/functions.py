from numpy import *

# RosenBrock function
class RosenBrock:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2.048, max=2.048):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)-1):
            res += (1.-pos[i])**2 + 100.*(pos[i+1]-pos[i]**2)**2;
        return res;

# Goldstein and Price function
class GoldStein:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2, max=2):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        return (1 + (1 + pos[0] + pos[1])**2 * (19 - 14*pos[0] + 3*pos[0]*pos[0] - 14*pos[1] + 6*pos[0]*pos[1] + 3*pos[1]*pos[1]))*(30 + (2*pos[0] - 3*pos[1])**2 * (18 - 32*pos[0] + 12*pos[0]*pos[0] + 48*pos[1] - 36*pos[0]*pos[1] + 27*pos[1]*pos[1]))

# Michalewicz function
class Michalewicz:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=0, max=pi):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += -sin(pos[i])*(sin((i+1)*pos[i]*pos[i]/pi))**20
        return res;

# De Jong 1 function
class DeJong1:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5.12):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += pos[i]*pos[i];
        return res;

# De Jong 2 function
class DeJong2:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-2.048, max=2.048):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        return (1.-pos[0])**2 + 100.*(pos[1]-pos[0]**2)**2;

# De Jong 3 function
class DeJong3:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
    
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += floor(pos[i]);
        return res;

# Hyper Ellipsoid function
class Ellipsoid:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-65.536, max=65.536):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            subres = 0;
            for j in range(i):
                subres += pos[j];
            res += subres*subres;
        return res;

# RastRigin function
class RastRigin:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5.12, max=5.12):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += pos[i]*pos[i] - 10.*cos(2.*pi*pos[i]);
        return 10*len(pos) + res;

# Schwefel function
class Schwefel:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-500, max=500):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        for i in range(len(pos)):
            res += -pos[i]*sin(sqrt(abs(pos[i])));
        return res;

# Zakharov function
class Zakharov:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-5, max=10):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        res = 0;
        first = 0;
        second = 0;
        for i in range(len(pos)):
            first += pos[i]*pos[i];
            second += 0.5*(i+1)*pos[i];
        return first + second**2 + second**4;

# Easom function
class Easom:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=pi-2, max=pi+2):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        return -cos(pos[0])*cos(pos[1])*exp(-((pos[0]-pi)**2 + (pos[1]-pi)**2));

# Six-Hump Camel Back function
class CamelBack:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-3, max=3):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = min;
        self.max = max;
        
    def getValue(self, pos):
        return (4.-2.1*pos[0]*pos[0]+pos[0]**(4./3.))*pos[0]*pos[0] + pos[0]*pos[1] + (-4.+4.*pos[1]*pos[1])*pos[1]*pos[1];

# Ackley's path function
class AckleyPath:
    def __init__(self, dim=2, max_particules=25, max_it=1000, min=-32.768, max=32.768):
        self.max_particules = max_particules;
        self.max_it = max_it;
        self.dim = dim;
        self.min = -2;
        self.max = 2;
        
    def getValue(self, pos):
        a = 20.;
        b = 0.2;
        c = 2.*pi;
        
        c1 = 0;
        c2 = 0;
        for i in range(len(pos)):
            c1 += pos[i]*pos[i];
            c2 += cos(c*pos[i]);
            
        return -a*exp(-b*sqrt(c1 / len(pos))) - exp(c2 / len(pos)) + a + exp(1)