# Assesement 3

## __By Ali El Naggari and Yehia Sulaiman__

### Dependancies:
  - [Ubuntu 18.04](https://releases.ubuntu.com/18.04.5/)
  - [Python 3.10.4](https://www.python.org/downloads/)
  - [petercorke /robotics-toolbox-python](https://github.com/petercorke/robotics-toolbox-python/tree/71183f3221cf9ced69420f07ade06f4514c256ba)
  - [Visual Studio Code](https://code.visualstudio.com/)
 
 **Warning: Newer or older version of installed software may not work correctly due to constant chanages by updates, ensure correct versions are installed for your conveniance.**
**********************************************************************************************************************************************************

This code simulates a robot moving to target coordinates in MATLAB.
 Robot is placed at coordinates specified by user input and moves to target from input. Program also asks for number of obstacles wanted and randomly generates them.
 
**In Line 17 add name of image downloaded on device that is in the same directory as the code instead of RR.jpg in code.**
 
 ### Libaries Used:
| roboticstoolbox    | math  | mathplotlib.pyplot | numpy |
| ------------------ | ----- | ------------------ | ----- |
| Bicycle            | pi    | imported as plt    | as np |
| RandomPath         | atan2 |         ----       | ----  |
| VehicleIcon        | ----  |         ----       | ----  |
| RangeBearingSensor | ----  |         ----       | ----  |
| LandmarkMap        | ----  |         ----       | ----  |
     
 
 ### Funtions Used:
     - int(input(" Insert text here ") // Asks for integer input by printing text between quotations
     - VehicleIcon('RR.png',scale = 2) // Selects Image downloaded and loads it into the simulation at desired scale.
     - Bicycle( animation = icon,      // Gives robot vehicle features such as speed, acceleration, direction, etc. , animation = "Variable set for VehicleIcon function" 
     - plt.plot(x, y, z )              // Plots coordinates x, y, z
     - run = true                      // Begins running or action of the program
     - While(run)                      // Goes into loop till specified conditions are met
     - veh.step(x, y, z )              // Moves vehicle in coordinated entered direction
     - abs( integer )                  // Gives abseloute of integer
     - veh._animation.update(veh.x)    // Updates plotting
     - plt.pause( integer )            // Runs loop for specified seconds after plotting is completed
     
 ### Future Work:
    - Be able to implment faster and more smooth plotting to provide more realistic simulations
    - Imporove obstacle avoidance
    - Add moving obstacles to enhance simulation
