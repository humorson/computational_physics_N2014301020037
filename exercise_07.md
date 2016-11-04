#exercise07：problem3.12
##abstract
####in constructing with the poincare section，i plotted points at some specific times.
##background
###physical equations
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercis_07/1.png
)
###Euler_cromer calculation
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercis_07/2.png
)
###parameters
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercis_07/3.png
)
##main body
```
import math
import pylab as pl
class chaotic_pendulum:
    def __init__(self,intial_theta=0.2,intial_w=0,time_of_duration=5000):
        self.theta=[intial_theta]
        self.t=[0]
        self.w=[intial_w]
        self.dt=0.01
        self.q=0.5        
        self.F_D=1.2
        self.w_D=0.6666667
        self.nsteps = int(time_of_duration // self.dt + 1)
        self.tmp_w1=[]
        self.tmp_theta1=[]
        self.tmp_w2=[]
        self.tmp_theta2=[]
        self.tmp_w3=[]
        self.tmp_theta3=[]
    def penludums(self):
        for i in range(self.nsteps):
            tmp_w=self.w[i]-(math.sin(self.theta[i])+self.q*self.w[i]-self.F_D*math.sin(self.w_D*self.t[i]))*self.dt
            self.w.append(tmp_w)  
            tmp_theta=self.theta[i]+self.w[i+1]*self.dt                        
            self.theta.append(tmp_theta)
            while self.theta[-1]>1*math.pi:
                self.theta[-1]=self.theta[-1]-2*math.pi
            while  self.theta[-1]<-1*math.pi:
                self.theta[-1]=self.theta[-1]+2*math.pi 
            self.t.append(self.t[i]+self.dt)
        for i in range(self.nsteps):           
           if math.fabs(self.t[i]%(2*math.pi/self.w_D))<0.005:
                self.tmp_w1.append(self.w[i])
                self.tmp_theta1.append(self.theta[i])
        for i in range(self.nsteps):           
           if math.fabs(self.t[i]%(2*math.pi/self.w_D)-math.pi/4)<0.005:
                self.tmp_w2.append(self.w[i])
                self.tmp_theta2.append(self.theta[i])
        for i in range(self.nsteps):           
           if math.fabs(self.t[i]%(2*math.pi/self.w_D)-math.pi/2)<0.005:
                self.tmp_w3.append(self.w[i])
                self.tmp_theta3.append(self.theta[i])
    def show_results(self):
        pl.plot(self.tmp_theta1, self.tmp_w1,'.',label='t=$2n\pi$')
        pl.plot(self.tmp_theta2, self.tmp_w2,'.',label='t=$2n\pi+\pi/4$')
        pl.plot(self.tmp_theta3, self.tmp_w3,'.',label='t=$2n\pi+\pi/2$')
        pl.xlabel('$\\theta$ (radians)')
        pl.ylabel('$w$(radius/s)')
        pl.title('$w$ versus $\\theta$')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)        
        pl.show()
a=chaotic_pendulum()
a.penludums()
a.show_results()
```
###result:
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercis_07/results.png)
##conclusion
##acknowledgement
