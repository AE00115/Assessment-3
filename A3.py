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
icon = VehicleIcon('RR.png',scale = 2)
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

#Head to goal     LAB 8
# run = True
# while(run):
#     goal_heading = atan2(  #angle of vehicle to target
#     goal[1] - veh.x[1],
#     goal[0] - veh.x[0])
#     steer = goal_heading - veh.x[2]
#     veh.step(0.5,steer)
#     if((abs(goal[0]-veh.x[0]) > 0.05) or (abs(goal[1] - veh.x[1]) > 0.05)):
#         run=True
#     else:
#         run=False

# # #Range bearing sensor LAB 9
sensor = RangeBearingSensor(robot = veh, map=map,animate = True)

print('Sensor Readings: /n', sensor.h(veh.x))
distances = [i[0] for i in sensor.h(veh.x)]
angles = [i[1] for i in sensor.h(veh.x)]
run = True
while(run):
    for i in sensor.h(veh.x):
        if i[0] < 2 :
            if abs(i[1] < pi):
                 run = False
        else:
            run = True
            while(run):
                goal_heading = atan2(  #angle of vehicle to target
                goal[1] - veh.x[1],
                goal[0] - veh.x[0])
                steer = goal_heading - veh.x[2]
                veh.step(1,steer)
                if((abs(goal[0]-veh.x[0]) > 1) or (abs(goal[1] - veh.x[1]) > 1)):
                    run=True
                else:
                    run=False
                

#show plot
                veh._animation.update(veh.x)
                plt.pause(0.05)
plt.pause(1000)