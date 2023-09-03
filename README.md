# 1121 Introduction to Robotics Tutorial 
## ME4609301 (for Taiwan-Paraquay Polytechnic University)
:bulb: In this class, the students can learn the basics of manipulating the operation of industrial robot arms (EPSON robot). The class introduces two types of robots, Pro-6-Axis robots, and SCARA robots, but only utilizes Pro-6-Axis robots in exercises. The main subjects include Introduction to Industrial Robot Arm, Software and Simulation, Calibration and Alignment, I/O port Communication, Human-machine interface (HMI), and Machine vision. In the end, the students possess the capability to design an automatic work cell with the robot. 
## :beginner: Exercises and resources

- Basic and Challenging tasks:
    - [ ] Basic tasks
    - [ ] Challenging tasks
- Level of capability: 
    - [ ] Level 1,2,3,4,5.
- Resources (CAD files, manuals): 
    - [ ] CAD software
    - [ ] CAD files (tool, fixture, tray...)
    - [ ] CAD files from vendors, Chelic. (Solenoid, Gripper, vacuum nozzle)
    - [ ] EPSON manuals
- Extra-exercise time booking: 
    - [ ] 2 shifts per week. (3 hours/shift)

## :triangular_flag_on_post: Basic and Challenging tasks
The suggested basic tasks can help students familiarize the setting of the World, Local, and Tool coordinates with the robots and utilize essential functions and commands.
The challenging tasks provide ideas and drill exercises for students to improve their coding and planning skills. These tasks only depicted the targets (specification or functionality) without detailed instructions. Students should use their creativity to leverage the functions and commands they learned in the lectures and robot manuals.

### Basic tasks
- Task 1. Exploring the robot envelop and the work cell:

Install tools and components (feeder, fixture, tray) and explore their coordinates with tools (extra parts may be required to proceed the calibration)
1. Define the World (local0), Local, tool(tool0), tool coordinates. (Based on the robots and works cell)
2. Measure the tool dimension and the center offset between tool0(J6, robot) and tools.(Tool1: gripper, Tool2: vacuum nozzle)
3. Decide the space between "objects"(tokens and blocks) at pick-up and approach gap when place

Exercise: Transfer tokens from the feeder to the fixture first, then move them to the tray. 
- Task 2. Building the simulation environment:

There are two ways to build the simulation environment:
1. Use the measured dimension of the robot envelope and the work cell in Basic: Task 1.
2. Start a new layout arrangement with the CAD files
Exercise: Insert CAD models in a robot envelope. 

### Challenging tasks (draft)

- #### Task 1. Tools
1. Gripper - high accuracy (can skip the alignment process in specific circumstances); can be used as a tool to align objects at fixtures (alignment)
2. Vacuum nozzle - with the pressure sensor, can be used to check objects and as a tool to align objects. 
3. Explore the status by vacuum pressure gauge (sensor): check feeder, fixture, and tray status. (quantity, occupied or vacancy)
- #### Task 2. Feeder
1. Two feeders (A, B)
2. Mixed tokens and blocks
3. Stack up not neatly (not aligned)
4. Unfull-fill the feeder (checking quantity)
- #### Task 3. Fixture
1. Two fixtures (for different orientations - block 20 mm x 24 mm)
2. How to distinguish the block in (20 mm x 24 mm) or (24 mm x 20 mm)
- #### Task 4. Tray
1. One tray 
2. Two trays stack up (two layers)
3. Two trays, one at the essential location and one at another with an angle(30 degrees). 
- #### Task 5. Others
1. HMI - check token or block 
2. HMI - Check the orientation of "rectangle" blocks
3. ......... with any idea you can think of. (continue) 
## 📈  Level of achievement:

To measure the capability of implementation of a robotic project.

|     **Level**    |   **Capbility**  |**To achieve assignments** |
|:------------------:|:--------------:|:-----:|
| 01      | Can set coordinates (world, local, tools) and align tool to work cell.| Complete basic tasks, like the six pieces pick-n-place task (one feeder, one fixture, one tray)
| 02   |Can communicate with a robot to perform selection or make some judgment via I/O or network | like manually conduct select feeder, sort token and block via HMI. (in practice, the robot can communicate to the end effectors ( like a screwdriver, soldering gun, glue nozzle, welding torch, etc.; or machine vision to get the location or OCR information|
| 03   |Can plan process to handle expected changes|like when one feeder is empty, automatically changes to the other. |
| 04   |Can handle unexpected changes|like when lost power, lost pneumatic, E-Stop, can restore system by interference.|
| 05   |Can perform the continuous operation with auto restore capability response to the anomaly detection and continue to operate | Automatic drop the token or block when an anomaly is detected and restored. |  

The goal is to make the robot run continuously without human intervention. 

## :feet: Resources (CAD files, manuals):
CAD software, files, and manuals.
### :small_blue_diamond: CAD software
1. Mechanical Engineering Department - CAD software 
https://www.me.ntust.edu.tw/p/405-1005-35690,c2568.php?Lang=zh-tw
2. Free auto cad, register with student id. 
https://www.autodesk.com/products/fusion-360/education
3. Education account apply
https://www.autodesk.com/education/support

### :small_blue_diamond: CAD files (tool, fixture, tray…)
1. Tooling End Effector: https://a360.co/44fONAx 
2. Token: https://a360.co/3pmQSv7
3. Block: https://a360.co/3NmZcTH
4. Fixture, Tray: https://a360.co/3JyIhw6
5. Alignment/Infeed fixture: https://a360.co/3NNyUKD
6. Reference Point Setup Tool: https://a360.co/3PyeMhJ

### :small_blue_diamond: CAD files from vendors, Chelic. (Solenoid, Gripper, vacuum nozzle)
1. Chelic components download: https://chelic.partcommunity.com/

### :small_blue_diamond: EPSON manuals
1. EPSON manual:
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://files.support.epson.com/far/docs/epson_rc_pl_70_users_guide-rc700a_rc90_t(v73r4).pdf  
2. Delta HMI manual: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://filecenter.deltaww.com/Products/download/06/060302/Manual/DELTA_IA-HMI_DOPSoft_UM_EN_20211230.pdf



