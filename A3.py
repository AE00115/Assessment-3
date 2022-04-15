#imporing libaries
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon, RangeBearingSensor, LandmarkMap
from math import pi , atan2
import matplotlib.pyplot as plt
import numpy as np

#Allowing user to input coordinates
x = int(input("Please enter x-coordinate of starting point for robot: "))
y = int(input("Please enter y-coordinate of starting point for robot: "))

gx = int(input("Please enter x-coordinate of target goal: "))
gy = int(input("Please enter y-coordinate of target goal: "))

#Add image to robot
icon = VehicleIcon('RR.png',scale = 5)
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
map = LandmarkMap(20,20)  #setting dimension of map
map.plot()
#set goal marker
goal = [gx,gy]; 
goal_marker_style = {
    'marker' : 'D',
    'markersize' : 5,
    'color' : 'b',
}
plt.plot(goal[0], goal[1], **goal_marker_style)
#Range bearing sensor
sensor = RangeBearingSensor(robot = veh, map=map,animate = True)

print('Sensor Readings: /n', sensor.h(veh.x))
distances = [i[0] for i in sensor.h(veh.x)]
angles = [i[1] for i in sensor.h(veh.x)]
run = True
while(run):
    for i in sensor.h(veh.x):
        if i[0] < 3 :
            if abs(i[1] < 5):
                 run = False
        else:
            veh.step(2,0)
            veh._animation.update(veh.x)
            plt.pause(0.005)
#show plot
veh._animation.update(veh.x)
plt.pause(1000)