##Final:Chapter 7 random systems 
***   
###abstract   
1.random walks    
2.self-avoiding walks   
###background    
1.random walks: consider the simulation of several different types of random walks with every step being independent of all prior steps.    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/600.png)   
2.self-avoiding walks: It is a random walk that is subject to a constraint. The constraint is that a sequence of moves on a lattice  that does not visit the same point more than once.  
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/601.png)       
###main body    
1.random walks   
```   
import random
import matplotlib.pyplot as plt
class random_walks:
    def __init__(self,n=100,step_length=0.1):
        self.x=[0]
        self.y=[0]
        self.x2=[0]
        self.n=n
        self.l=step_length
    def walk1(self):#random walk with step_length=1
        for i in range(1,self.n):
            self.x.append(i)
            temp=random.random()
            if temp < 0.5:
                self.y.append(self.y[-1]-self.l)
            elif temp > 0.5:
                self.y.append(self.y[-1]+self.l)
            self.x2.append(self.x2[-1]+self.l**2)
    def walk2(self):#random walk with random step-length
        for i in range(1,self.n):
            self.x.append(i)
            temp=random.random()
            self.l=random.random()
            if temp < 0.5:
                self.y.append(self.y[-1]-self.l)
            elif temp > 0.5:
                self.y.append(self.y[-1]+self.l)
            self.x2.append(self.x2[-1]+self.l**2)
    def show1(self):
        plt.plot(self.x,self.y,'o')
        plt.title('random walk in one dimension')
        plt.xlabel('step number')
        plt.ylabel('x')
        plt.grid(True)
    def show2(self):
        plt.plot(self.x,self.x2,'.',label='$<x^2>$ versus time')
        plt.title('random walk in one dimension')
        plt.xlabel('step number')
        plt.ylabel('$<x^2>$')
        plt.legend(frameon=True)
        plt.grid(True)
a=random_walks()
a.walk1()
a.show1()
b=random_walks()
b.walk1()
b.show1()
```   
####results  
random walk with a specific step-length   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/602.png)
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/603.png)    
random walk with a random step-length    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/604.png)
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/605.png)     

2.self-avoiding walks     
```   
import matplotlib.pyplot as plt
import random
class SAW:
    def __init__(self,l=1000,n=1000):
        self.l=l
        self.n=n
        self.r2=[0]
        self.t=[0]
        self._fig=[[0]*self.l for i in range(self.l)]
        self.loc=[[int(self.l/2),int(self.l/2)]]
    def walk1(self):
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        while(1):
            temp=random.random()
            if temp<0.25:
                temp1=self.loc[-1][0]-1
                temp2=self.loc[-1][1]
            elif 0.25<temp<0.5:
                temp1=self.loc[-1][0]
                temp2=self.loc[-1][1]-1
            elif 0.5<temp<0.75:
                temp1=self.loc[-1][0]+1
                temp2=self.loc[-1][1]
            elif 0.75<temp<1:
                temp1=self.loc[-1][0]
                temp2=self.loc[-1][1]+1
            self.loc.append([temp1,temp2])
            self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
            self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
            self.t.append(self.t[-1]+1)
            if self.t[-1]>=self.n:
                break
    def walk2(self):
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        temp=random.random()
        if temp<0.25:
            temp1=self.loc[-1][0]-1
            temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
        elif 0.25<temp<0.5:
            temp1=self.loc[-1][0]
            temp2=self.loc[-1][1]-1
            self.loc.append([temp1,temp2])
        elif 0.5<temp<0.75:
            temp1=self.loc[-1][0]+1
            temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
        elif 0.75<temp<1:
            temp1=self.loc[-1][0]
            temp2=self.loc[-1][1]+1
            self.loc.append([temp1,temp2])
        self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
        self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
        self.t.append(self.t[-1]+1)
        while(1):
            if self.loc[-2][0]==self.loc[-1][0]+1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1
                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]
                elif temp>2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
            elif self.loc[-2][1]==self.loc[-1][1]+1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]-1
                    temp2=self.loc[-1][1]
                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1
                elif temp>2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]
            elif self.loc[-2][0]==self.loc[-1][0]-1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]-1

                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]

                elif temp>2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
            elif self.loc[-2][1]==self.loc[-1][1]-1:
                temp=random.random()
                if temp<1/3:
                    temp1=self.loc[-1][0]+1
                    temp2=self.loc[-1][1]

                elif 1/3<temp<2/3:
                    temp1=self.loc[-1][0]
                    temp2=self.loc[-1][1]+1
                elif temp>2/3:
                    temp1=self.loc[-1][0]-1
                    temp2=self.loc[-1][1]
            self.loc.append([temp1,temp2])
            self._fig[self.loc[-1][0]][self.loc[-1][1]]=1
            self.r2.append((self.loc[-1][0]-self.loc[0][0])**2+(self.loc[-1][1]-self.loc[0][1])**2)
            self.t.append(self.t[-1]+1)
            if self.t[-1]>=self.n:
                break
    def show1(self):
        plt.grid(True)
        plt.plot(self.t,self.r2,'.',label='usual random walk')
        plt.xlabel('time')
        plt.ylabel('$<r^2>$')
        plt.legend(frameon=True)
    def show2(self):
        plt.grid(True)
        plt.plot(self.t,self.r2,'.',label='self-avoiding random walk')
        plt.xlabel('time')
        plt.ylabel('$<r^2>$')
        plt.legend(frameon=True)
a=SAW()
a.walk1()
a.show1()
b=SAW()
b.walk1()
b.show1()   
```    
####results   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/609.png)   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/final/608.png)     

###conclusion  
run the programme several times, it will give out different results. These results are totally different because of random.   

###aknowledgement   
Nicholas J.Giodano's computational physics.
wiki.
and thanks Qing Dayue for some codes' problems.   



