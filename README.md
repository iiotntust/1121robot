# 1121 Introduction to Robotics Tutorial 
## ME4609301 (for Taiwan-Paraquay Polytechnic University)
:bulb: In this class, the students can learn the basics manipulating operation of industrial robot arms (EPSON robot). The class introduces two types robots, 6-Axis robot and SCARA robot, but only utiliz 6-Axis robots in exercises. The main subjects include: Introduction to Industrial Robot Arm, Software and Simulation, Calibartion and Alignment, I/O port Commmunication, Human-Machine Interface (HMI), Machine vision. In final, the students possess the capability to deisgn an automatic work cell with robot. 
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
    - [ ] 2 shift per week. (3 hours/shift)

## :triangular_flag_on_post: Basic and Challenging tasks
The suggested basic tasks can help students familiarize the World, Local, and Tool coordinates settings, and utilize essential functions and commands.
The challenging tasks provide ideas and drill exercises for students to improve their coding and planning skills. These tasks only depicted the targets (specification or functionality) without the detail instructions. Students should leverage the functions and commands they learned in the lectures and robot manuals with their creativity.

### Basic tasks
- Task 1. Exploring the robot envelop and the workcell:

Install tools and components (feeder, fixture, tray) and explore their coordinates with tools (extra parts may be required to proceed the calibration)
1. Define the World (local0), Local, tool(tool0), tool coordinates. (Based on the robots and works cell)
2. Measure the tool dimension and the center offset between tool0(J6, robot) and tools.(Tool1: gripper, Tool2: vacuum nozzle)
3. Decide the space between "objects"(tokens and blocks) at pick-up and approach gap when place

Exercise: transfer tokens from feeder to fixture first, and then move to the tray. 
- Task 2. Building the simulation environment:

There are two way to build the simulaton environment:
1. Use the measured dimension of robot envelop and the workcell in Basic: Task 1.
2. Start a new layout arrangement with the CAD files
Exercise: insert CAD models in robot envelope. 

### Challenging tasks (draft)

- #### Task 1. Tools
1. Gripper - high accuracy (can skip the alignment process in specific circustance); can use as a tool to align objects at fixtures (alignment)
2. Vacuum nozzle - with presure sensor, can use to check objects; can use as tool to align object, too. 
3. Explore the status by vaccume presure: check feeder, fixture, tray status. (quanity, occupied or vaccancy)
- #### Task 2. Feeder
1. Two feeders (A, B)
2. Mixed tokens and blocks
3. Stack up not neatly (not aligned)
4. Unfull-fill the feeder (checking quanlity)
- #### Task 3. Fixture
1. Two fixtures (for different orientation - block 20 mm x 24 mm)
2. How to distinguish the block in (20 mm x 24 mm) or (24 mm x 20 mm)
- #### Task 4. Tray
1. One tray 
2. Two tray stack up (two layer)
3. Two tray, one at essientail location, one at other location with angle(30 degree). 
- #### Task 5. Others
1. HMI - check token or block 
2. HMI - check orientation of "rectangle" blocks
3. ......... to be continue. 
## 📈  Level of achievement:

:::success
To measure the capability of implmenation robotic project.
:::

|     **Level**    |   **Capbility**  |**To achieve assignments** |
|:------------------:|:--------------:|:-----:|
| 01      | Can set cooridinates (world,local,tools), and align tool to workcell.| Complete basic tasks; like the 6 piceces pick-n-place task (one feeder, one fixture, one tray)
| 02   |Can communicate robot to perform selection or judgement via I/O or network | like conduct select feeder, sort token and block via HMI by human.  |
| 03   |Can plan process to handle expected changes|like when one feeder empty, automatically changes to the other one. |
| 04   |Can handle unexpected changes|like when lost power, lost pneumatic, E-Stop, can restored system by interference.          |
| 05    |Can perform continously operation with auto restore capabilityreponse to anomal and continue to operates| Automatic drop the token or block when anomal happened and restore. |  

The goal is to make the robot can run continuesly without ma





## :feet: Resources (CAD files, manuals):

:::success
CAD software, files, manuals.
:::

### :small_blue_diamond: CAD software
1. Mechanical Engineering Department - CAD software 
https://www.me.ntust.edu.tw/p/405-1005-35690,c2568.php?Lang=zh-tw
2. Free auto cad, register with students id. 
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



