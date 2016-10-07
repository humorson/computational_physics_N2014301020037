#exercise_04   
***      
##abstract            
 * finish the problem 1.5  
     
##background     
 * after solving the problem of radioactive decay in Chapter 1 and testing the program, we could use python, matplotlib and Euler's method of math to work out a universal solution to this kind of problems.   
 
##main body    
**Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D),<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D),<br>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , . Solve the system of equations for the numbers of nuclei,  and , as functions of time. Consider different initial confitions, such as , , etc., and take  s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which  and  are constant. In such a steady state, the time derivatives  and should vanish.




