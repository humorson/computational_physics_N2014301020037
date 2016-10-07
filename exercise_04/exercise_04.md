#exercise_04   
***      
##abstract            
 * finish the problem 1.5  
     
##background     
 * after solving the problem of radioactive decay in Chapter 1 and testing the program, we could use python, matplotlib and Euler's method of math to work out a universal solution to this kind of problems.   
 
##main body    
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies. The corresponding rate equations are   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f253543667261632537422535436d617468726d253742642537442532304e5f253742412537442537442537422535436d617468726d2537426425374425323074253744253344253543667261632537.gif),<br>   
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f253543667261632537422535436d617468726d253742642537442532304e5f253742422537442537442537422535436d617468726d2537426425374425323074253744253344253543667261632537424e5f.gif),<br>    
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , . Solve the system of equations for the numbers of nuclei,  and , as functions of time. Consider different initial confitions, such as , , etc., and take  s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which  and  are constant. In such a steady state, the time derivatives  and should vanish.    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f2535436c656674253543253742253543626567696e2537426d61747269782537442532304e5f25374241253744253344435f2537423125374426706c75733b435f25374232253744652535452537422d2535.gif)     
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/687474703a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f2535436c656674253543253742253543626567696e2537426d61747269782537442532304e5f25374241253744253344253543667261632537424e5f253742413025374426706c75733b4e5f253742423025.gif)      
[click here to check the code](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/problem1.5.py)  
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/20161007234948.png)    
![](https://github.com/humorson/computational_physics_N2014301020037/blob/master/exercise_04/20161007235947.png)   
##conclusion   
 * Using python, matplotlib and Euler's method could solve this kind of problem. Although there exists inaccuracy in
results, it can be confined in a controllable range.        

##acknowledgement   
 * thanks to Qing Dayue for some code's problems.




