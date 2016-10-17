import math
import pylab as pl
class canon_trajectory:
    def __init__(self,initial_velocity=700,angle_of_depature=45,altitude=0,
                 step_time=0.001,mass=10):
        self.i=0
        self.v=[initial_velocity]
        self.angle=angle_of_depature/180*math.pi
        self.vx=[initial_velocity*math.cos(angle_of_depature/180*math.pi)]
        self.vy=[initial_velocity*math.sin(angle_of_depature/180*math.pi)]
        self.x_0=[0]
        self.y_0=[altitude]
        self.x_1=[0]
        self.y_1=[altitude]
        self.x_2=[0]
        self.y_2=[altitude]
        self.t=[0]
        self.dt=step_time
        self.m=mass
        print("mass---------------->",self.m)
        print("initial_velocity---->",self.v[0])
        print("angle_of_depature--->",self.angle/math.pi*180)
        print("altitude------------>",self.y_0[0])

    def gravity(self):
        while(self.y_0[-1]>=0):
            temp_vx=self.vx[self.i]
            temp_vy=self.vy[self.i]-9.8*self.dt
            temp_v=math.sqrt(temp_vx**2+temp_vy**2)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.v.append(temp_v)
            temp_x=self.x_0[self.i]+temp_vx*self.dt
            temp_y=self.y_0[self.i]+temp_vy*self.dt
            self.x_0.append(temp_x)
            self.y_0.append(temp_y)
            self.i=self.i+1
    def show_result0(self):
        temp_plot0,=pl.plot(self.x_0,self.y_0,"g")
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
        pl.ylim(0,)
        pl.legend([temp_plot0],["constant gravity"])
        land_point0=self.x_0[-2]-self.y_0[-2]*(self.x_0[-1]-self.x_0[-2])/(self.y_0[-1]-self.y_0[-2]) 
        print("with constant gravity,the canon land at\n","x=",land_point0,"y=0") 
a=canon_trajectory()
a.gravity()
a.show_result0()


class trajectory_with_varing_g(canon_trajectory):       
    def gravity_varies_with_altitude(self):
        self.i=0
        while(self.y_1[-1]>=0):
            temp_vx=self.vx[self.i]
            temp_vy=self.vy[self.i]-3.989*10**14/((6370000+self.y_1[self.i])**2)*self.dt
            temp_v=math.sqrt(temp_vx**2+temp_vy**2)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.v.append(temp_v)
            temp_x=self.x_1[self.i]+temp_vx*self.dt
            temp_y=self.y_1[self.i]+temp_vy*self.dt
            self.x_1.append(temp_x)
            self.y_1.append(temp_y)
            self.i=self.i+1
    def show_result1(self):
        temp_plot1,=pl.plot(self.x_1,self.y_1,"b")
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
        pl.ylim(0,)
        pl.legend([temp_plot1,],["varing gravity"])
        land_point1=self.x_1[-2]-self.y_1[-2]*(self.x_1[-1]-self.x_1[-2])/(self.y_1[-1]-self.y_1[-2])
        print("with gravity varing with altitude,the cannon land at\n","x=",land_point1,"y=0")
b=trajectory_with_varing_g()
b.gravity_varies_with_altitude()
b.show_result1()
        
        
        
        
        
class trajectory_with_drag(canon_trajectory):            
    def _with_air_drag(self):
        self.i=0
        while(self.y_2[-1]>=0):
            temp_vx=self.vx[self.i]-0.0006465*math.exp(-self.y_2[self.i]/10000)*(self.v[self.i]**2)/self.m*self.vx[self.i]/self.v[self.i]*self.dt
            temp_vy=self.vy[self.i]-0.0006465*math.exp(-self.y_2[self.i]/10000)*(self.v[self.i]**2)/self.m*self.vy[self.i]/self.v[self.i]*self.dt-9.8*self.dt
            temp_v=math.sqrt(temp_vx**2+temp_vy**2)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.v.append(temp_v)
            temp_x=self.x_2[self.i]+temp_vx*self.dt
            temp_y=self.y_2[self.i]+temp_vy*self.dt
            self.x_2.append(temp_x)
            self.y_2.append(temp_y)
            self.i=self.i+1
    def show_result2(self):
        temp_plot2,=pl.plot(self.x_2,self.y_2,"y")
        pl.xlabel("x(m)")
        pl.ylabel("y(m)")
        pl.title("trajectory of the canon")
        pl.ylim(0,)
        pl.legend([temp_plot2],["with drag force"])
        land_point2=self.x_2[-2]-self.y_2[-2]*(self.x_2[-1]-self.x_2[-2])/(self.y_2[-1]-self.y_2[-2])
        print("take the air drag force into consideration,the cannon land at\n","x=",land_point2,"y=0")
c=trajectory_with_drag()
c._with_air_drag()
c.show_result2()

  

