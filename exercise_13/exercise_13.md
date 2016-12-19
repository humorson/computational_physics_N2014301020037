##exercise_13:chapter:waves, problem 6.1&6.2    
***    
##abstract   
consider the particular case of waves on a string with fixed ends (different values of r less than 1) or free ends.   

##background   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/233.jpg)      
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/204.gif)     

the center equation of wave motion for ideal cases:   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/200.png)   
construct a numerical approach to the wave equation in finite difference form:   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/202.png)    
"Gaussian pluck":    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/201.png)     

##main body   
```   

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
class waves:
    def __init__(self,r=1,length=1,amplitude=1,n=100,update_times=5000,pluck_point=0.5,):
        self.r=r
        self.l=length
        self.A=amplitude
        self.n=n
        self.N=update_times
        self.p=pluck_point
        self.x=np.linspace(0,length,n)
        self.y0=[]
        self.y1=[]
        self.y=[]
        self.ss=[]
        self.fss=[]
    '''fixed ends'''
    def wave1(self):
        #self.y0=np.sin(4*np.pi*np.linspace(0,self.l,self.n))#initial wave
        self.y0=np.exp(-1000*(self.x-self.p)**2)#Gaussian plucking
        self.y1=np.linspace(0,0,self.n)
        for i in range(len(self.y0)-2):
            self.y1[i+1]=2*(1-self.r**2)*self.y0[i+1]-self.y0[i+1]+self.r**2*(self.y0[i+2]+self.y0[i])
        self.y.append(self.y0)
        self.y.append(self.y1)
    
    def propagate1(self):
        counter=1
        while(1):
            counter+=1
            temp_y=np.linspace(0,0,self.n)
            for i in range(len(self.y0)-2):
                temp_y[i+1]=2*(1-self.r**2)*self.y[-1][i+1]-self.y[-2][i+1]+self.r**2*(self.y[-1][i+2]+self.y[-1][i])
            self.y.append(temp_y)
            if counter>self.N:
                break
    '''free ends'''
    def wave2(self):
        self.y0=np.sin(4*np.pi*np.linspace(0,self.l,self.n))#initial wave
        #self.y0=np.exp(-1000*(self.x-self.p)**2)#Gaussian plucking
        self.y1=np.linspace(0,0,self.n)
        for i in range(len(self.y0)-2):
            self.y1[i+1]=2*(1-self.r**2)*self.y0[i+1]-self.y0[i+1]+self.r**2*(self.y0[i+2]+self.y0[i])
        self.y1[0]=2*self.y1[1]-self.y1[2]
        self.y1[-1]=2*self.y1[-2]-self.y1[-3]
        self.y.append(self.y0)
        self.y.append(self.y1)
    def propagate2(self):
        counter=1
        while(1):
            counter+=1
            temp_y=np.linspace(0,0,self.n)
            for i in range(len(self.y0)-2):
                temp_y[i+1]=2*(1-self.r**2)*self.y[-1][i+1]-self.y[-2][i+1]+self.r**2*(self.y[-1][i+2]+self.y[-1][i])
            temp_y[0]=2*temp_y[1]-temp_y[2]
            temp_y[-1]=2*temp_y[-2]-temp_y[-3]
            self.y.append(temp_y)
            if counter>self.N:
                break


a=waves()
a.wave2()
a.propagate2()
#show animated result
fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)
def init():  
    line.set_data([], [])  
    return line,
def animate(i):
    x = a.x
    y = a.y[i]
    line.set_data(list(x), list(y))   
    return line,
anim=animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=25)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


''' spectra'''

class fourier_tr(waves):
    def vibrate(self):
        for i in range(len(self.y)):
            self.ss.append(self.y[i][int(self.n/2)])
    def show_vib(self):
        temp_t=np.linspace(0,len(self.ss),len(self.ss))
        plt.plot(temp_t,self.ss,label='pluck point=%.2f'%self.p)
        plt.xlabel('t')
        plt.ylabel('signal')
        plt.title('string signal versus time')
        plt.grid(True)
        plt.legend(frameon=True)
    def ft(self):
        temp=np.fft.fft(self.ss)
        for i in temp:
            self.fss.append(i.real**2+i.imag**2)
        temp_f=np.linspace(0,int(len(self.fss)),int(len(self.fss)))
        plt.figure(figsize=(15,3))
        plt.plot(temp_f,self.fss,label='pluck point=%.2f'%self.p)
        plt.xlim(0,len(temp_f)/2)
        plt.title('power spectrum')
        plt.xlabel('f')
        plt.ylabel('power')
        plt.xlim(0,1000)
        plt.legend(frameon=True)
        
          
b=fourier_tr()
b.wave1()
b.propagate1()
b.vibrate()
b.show_vib()
b.ft()    
```    
###the results   
1.wave propagating on a fixed ends   
a sin initial pluck   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/205.gif)   
a gaussian initial pluck     
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/215.gif)    
2.wave propagating on a free ends     
a sin initial pluck     
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/216.gif)    
a gaussian initial pluck     
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/217.gif)     
3.spectrums    
spectrum of a sine vibration           
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/221.png)        
spectrum of a signal with a initial gaussian pluck           
string signal varies with time for different initial pluck point
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/207.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/208.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/209.png)     
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/210.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/211.png)     
the spectrum varies with different pluck point    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/212.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/213.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/214.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/218.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_13/219.png)    

##conclusion   
different ends condition vary the results of the wave motion of string.   
with different initial pluck point, there are also different wave motion of string and different spectrums.    

##acknowledgement  
thanks qingdayue for some codes' problems.    

