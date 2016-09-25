import os  
import time
myname=["#####   #   #   #####","   #     # #       # ","  #       #       #  "," #        #      #   ","#####     #     #####"]
space=' '
x=0
while x<50:
    print(space*x+myname[0])
    print(space*x+myname[1])
    print(space*x+myname[2])
    print(space*x+myname[3])
    print(space*x+myname[4])
    x=x+1
    time.sleep(0.1)
    i = os.system('cls')
    

    

