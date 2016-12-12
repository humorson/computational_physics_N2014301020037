##electric potentials and fields:Laplace's equation  Problem 5.1 and 5.3
***   
##abstract        
1、solve for the potential in the prism geometry in Figure 5.4(the following picture)       
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/001.png)        
2、use the symmetry of the capacitor problem(figure 5.6) to write a problem that obtains the result by calculating the potential in only one quadrant of the x-y plane.         
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/012.png)        
##background  
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/015.gif)       
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/004.jpg)               
Laplace's equation(in region of space do not contain any elctric charges)         
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/005.png)       
jacobi method         
In numerical linear algebra, the Jacobi method (or Jacobi iterative method) is an algorithm for determining the solutions of a diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges.       
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/006.png)     
Gauss-seidel method       
In numerical linear algebra, the Gauss–Seidel method, also known as the Liebmann method or the method of successive displacement, is an iterative method used to solve a linear system of equations.       
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_12/007.png)           
##main body      
```   
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
class ef:
    def __init__(self,alpha=1,n=20):
        self.n=n
        self.field=[[0]*(self.n) for i in range(self.n)]
    def field1(self):
        for i in range(int(self.n/4),int(self.n*3/4)):
            for j in range(int(self.n/4),int(self.n*3/4)):
                self.field[i][j]=1
        self.kk=1
        while(1):
            self.kk+=1
            for i in range(1,self.n-1):
                for j in range(1,self.n-1):
                    if int(self.n/4)<=i<=int(self.n*3/4) and int(self.n/4)<=j<=int(self.n*3/4):
                        self.field[i][j]=1
                    else:
                        self.field[i][j]=(self.field[i+1][j]+self.field[i-1][j]+self.field[i][j+1]+self.field[i][j-1])/4
            if self.kk>1000:
                break
    def field2(self):
        for i in range(1,self.n-1):
            for j in range(1,self.n-1):
                if j==int(self.n/4) and i>=self.n/4 and i<=self.n*3/4:
                    self.field[i][j]=1
                elif j==int(self.n*3/4) and i>=self.n/4 and i<=self.n*3/4:
                    self.field[i][j]=-1
        self.kk=1
        while(1):
            self.kk+=1
            for i in range(1,self.n-1):
                for j in range(1,self.n-1):
                    if j==int(self.n/4) and i>=self.n/4 and i<=self.n*3/4:
                        self.field[i][j]=1
                    elif j==int(self.n*3/4) and i>=self.n/4 and i<=self.n*3/4:
                        self.field[i][j]=-1
                    else:
                        self.field[i][j]=(self.field[i+1][j]+self.field[i-1][j]+self.field[i][j+1]+self.field[i][j-1])/4
            if self.kk>5000:
                break
    def show_field(self):
        fig = plt.figure()  
        ax = Axes3D(fig)
        X=np.linspace(-1,1,self.n)
        Y=np.linspace(-1,1,self.n)
        X, Y = np.meshgrid(X, Y)
        Z=self.field
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.hot)  
        ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)  
        ax.set_zlim(-2,2) 
a=ef()
a.field2()
a.show_field()    
```   
###results    
problem5.1  
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/013.png)    
problem5.3   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/014.png)    
##conclusion   
we can use jacobi method to solve some simple problems of electric potntials and fields.   
##aknowledgement   
thanks qingdayue for some codes' problems.
