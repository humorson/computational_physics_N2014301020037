#exercise10:Chapter4 the solar system problem 4.19    
***   
##abstract    
 * Study the behavior of our model for Hyperion for different initial conditions.   
Estimate the Lyapunov exponent from calculations of ![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/01.png)  
And examine how this exponent varies as a function of the eccentricity of the orbit.   

##background    
Hyperion, also known as Saturn VII,is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered.   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/1.jpg)
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/2.jpg)         
The Voyager 2 images and subsequent ground-based photometry indicated that Hyperion's rotation is chaotic, that is, its axis of rotation wobbles so much that its orientation in space is unpredictable. Its Lyapunov time is around 30 days.[16] Hyperion, together with Pluto's moons Nix and Hydra,[17][18] is among only a few moons in the Solar System known to rotate chaotically, although it is expected to be common in binary asteroids.[19] It is also the only regular planetary natural satellite in the Solar System known not to be tidally locked.    
Hyperion is unique among the large moons in that it is very irregularly shaped, has a fairly eccentric orbit, and is near a much larger moon, Titan. These factors combine to restrict the set of conditions under which a stable rotation is possible. The 3:4 orbital resonance between Titan and Hyperion may also make a chaotic rotation more likely. The fact that its rotation is not locked probably accounts for the relative uniformity of Hyperion's surface, in contrast to many of Saturn's other moons, which have contrasting trailing and leading hemispheres.   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/5.png)   
- equations for Hyperion's trajectory    
the inverse-square law of gravitation:  
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/6.png)     
we write it as two first-order differental equation so that we can use euler-cromer method:   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/7.png)  
which leads to   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/8.png)   
where we chose proper units(unit of lenth to be radius of Hyperion's orbit,which we might called 1 HU= "Hyperion unit",and that of time to be the orbit period of Hyperion around Saturn(1"Hyperion-year")):   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/9.png)   
Given the equations above and Euler-cromer method, we can calculate the trajectory of Hyperion. 
- equations for qualitively estimate the chaotic tumbling of Hyperion     
since our objective is simply to show that teh motion of such an irregularly shaped moon can be chaotic,we consider the model as two particles ,m1 and m2 ,connected bby a massless rod in orbit around a massive object located at the origion.   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/10.png)    

##main body   
 * the code
```  
import numpy as np
import pylab as pl
import math
class hyperion:
    def __init__(self,x0=1,y0=0,vx=0,vy=2*math.pi,dt=0.0001,total_time=10,initial_theta=0,initial_omega=0):
        self.x=[x0]
        self.y=[y0]
        self.r=[math.sqrt(x0**2+y0**2)]
        self.vx=[vx]
        self.vy=[vy]
        self.dt=dt
        self.t=[0]
        self.tt=total_time
        self.th=[initial_theta]
        self.om=[initial_omega]
        self.a=0
        self.b=0
        self.ecc=0
        self.dtheta=[]
    def run(self):
        while self.t[-1]<self.tt:
            self.vx.append(self.vx[-1]-4*math.pi**2*self.x[-1]/self.r[-1]**3*self.dt)
            self.vy.append(self.vy[-1]-4*math.pi**2*self.y[-1]/self.r[-1]**3*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.r.append(math.sqrt(self.x[-1]**2+self.y[-1]**2))
            temp=-12*math.pi**2*(self.x[-1]*math.sin(self.th[-1])-self.y[-1]*math.cos(self.th[-1]))\
            *(self.x[-1]*math.cos(self.th[-1])+self.y[-1]*math.sin(self.th[-1]))
            self.om.append(self.om[-1]+temp*self.dt)
            self.th.append(self.th[-1]+self.om[-1]*self.dt)
            if self.th[-1]>math.pi:
                self.th[-1]-=2*math.pi
            elif self.th[-1]<-math.pi:
                self.th[-1]+=2*math.pi
            self.t.append(self.t[-1]+self.dt)
        self.a=(max(self.x)-min(self.x))/2
        self.b=(max(self.y)-min(self.y))/2
        self.ecc=math.sqrt(math.fabs(self.a**2-self.b**2))/self.a
    def showth(self):
        pl.title("Hyperion $\\theta$ versus time")
        pl.xlabel("time(Hyperion-year)")
        pl.ylabel("$\\theta (radius)$")
        pl.xlim(0,10)
        pl.plot(self.t, self.th,label="eccentricity=%.2f"%self.ecc) 
        pl.legend()
        pl.grid(True)
        pl.show()
    def showom(self):
        pl.title("Hyperion $\\omega$ versus time")
        pl.xlabel("time(Hyperion-year)")
        pl.ylabel("$\\omega (radius)$")
        pl.xlim(0,10)
        pl.plot(self.t, self.om,label="eccentricity=%.2f"%self.ecc)  
        pl.legend()
        pl.grid(True)
        pl.show()
#plot theta or omega versus time

a=hyperion()
a.run()
a.showth()
a=hyperion()
a.run()
a.showom()

#plot delta theta versus time and calculate the lyapuniv exponent
class qwer(hyperion):
    def haha(self):
        _d=0.01
        _vy=2*math.pi-1.1
        a=hyperion(vy=_vy)
        a.run()
        print(a.ecc)
        tempth1=a.th
        a=hyperion(vy=_vy,initial_theta=_d)
        a.run()
        tempth2=a.th
        for i in range(len(tempth2)):
            a.dtheta.append(math.log(math.fabs(tempth2[i]-tempth1[i])))
        pl.plot(a.t,a.dtheta,label="eccentricity=%.4f"%a.ecc)
        dd=[]
        tt=[]
        for j in range(len(a.dtheta)):
            dd.append(a.dtheta[j])
            tt.append(a.t[j])
        z=np.polyfit(tt,dd,1)
        p=np.poly1d(z)
        print(p)
        linspx=np.linspace(0,8)
        linspy=z[0]*linspx+z[1]
        pl.plot(linspx,linspy,label="lyapunov exp=%.4f"%z[0])
        pl.xlabel("time(Hyperion-year)")
        pl.ylabel("$\\Delta\\theta(radius)$")
        pl.title("Hyperion $\\Delta\\theta$ versus time for initial $\\Delta\\theta$=%.3f"%_d)
        pl.legend()
b=qwer()
b.haha()   
```    
###the results  
decrease the velocity of y, the eccentricity rises from zero and the system become more chaotic. 
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/98.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/97.png) 
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/99.png)   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/95.png)   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/94.png)   
the lyapunov exponnet varies with the eccentricity.
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/96.png)   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/93.png)   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_11/92.png)    
an important factor step-time can not be ignored, because the programme runs out that eccentricity is 0.0004 rather than zero.
if we want to avoid this problem, we need to have a smaller step-time.    

##conclusion    
1.A moon which have a irregular shape most probably tumbling chaoticly.   
2.A smaller step-time can avoid some errors. 

##acknowledgement   
thanks qdy for some codes' problems.
  
