#imporing libaries
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
import numpy as np
############################################################################################################################
#Allowing user to input coordinates
x = eval(input("Please enter x-coordinate of starting point for robot: "))
y = eval(input("Please enter y-coordinate of starting point for robot: "))

gx = int(input("Please enter x-coordinate of target goal: "))
gy = int(input("Please enter y-coordinate of target goal: "))

obstacles = int(input("Enter number of obstacles: "))

#Add image to robot
icon = VehicleIcon('RR.png',scale = 2.5)
#creating car like model
veh = Bicycle(
    animation = icon,
    control = RandomPath,   #generate the control inputs for the vehicle
    dim = 10,   
    x0 = (x, y, 0)  #setting starting coordinates
    )
#print(veh.x)    #print vehicle position

#initialize vehicle
veh.init(plot=True)

#Select number of obstacles
map = LandmarkMap(obstacles,10);  
map.plot();

#set goal marker
goal = [gx,gy]; 
goal_marker_style = {
    'marker' : 'D',
    'markersize' : 2.5,
    'color' : 'b',
}
plt.plot(goal[0], goal[1], **goal_marker_style)
###########################################################################################################################

#Move to target
run = True
while(run):
    goal_heading = atan2(  #angle of vehicle to target
    goal[1] - veh.x[1],
    goal[0] - veh.x[0])
    steer = goal_heading - veh.x[2]
    veh.step(1,steer)
    if((abs(goal[0]-veh.x[0]) > 0.5) or (abs(goal[1] - veh.x[1]) > 0.5)):
        run=True
    else:
        run=False
###########################################################################################################################                

#show plot
    veh._animation.update(veh.x)
    plt.pause(0.05)
plt.pause(1000)