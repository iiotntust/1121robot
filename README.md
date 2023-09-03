# 1121 Introduction to Robotics Tutorial 
## ME4609301 (for Taiwan-Paraquay Polytechnic University)
:::info
:bulb: In this class, the students can learn the basics manipulating operation of industrial robot arms (EPSON robot). The class introduces two types robots, 6-Axis robot and SCARA robot, but only utiliz 6-Axis robots in exercises. The main subjects include: Introduction to Industrial Robot Arm, Software and Simulation, Calibartion and Alignemnt, I/O port Commmunication, Human-Machine Interface (HMI), Machine vision. In final, the students possess the capability to deisgn an automatic work cell with robot. 
:::

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

:::success
Basic tasks
:::
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


:::success
Challenging tasks (Coming soon)
:::

#### Task 1. (Coming soon)

#### Task 2. (Coming soon)

#### Task 3. (Coming soon)

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
![image](https://github.com/iiotntust/1121robot/assets/56021651/e30f6db4-7f5f-48d5-9b88-12e4757903e4)
![](https://hackmd.io/_uploads/SJ2SrFbAn.png)
2. ![](https://hackmd.io/_uploads/BJ_uHt-C3.png)
3. ![](https://hackmd.io/_uploads/r189rYWC2.png)
4. ![](https://hackmd.io/_uploads/Bk7jrYW0h.png)
5. ![](https://hackmd.io/_uploads/SyBhHt-R2.png)
6. ![](https://hackmd.io/_uploads/SJ76SKWCh.png)

### :small_blue_diamond: CAD files from vendors, Chelic. (Solenoid, Gripper, vacuum nozzle)
1. Chelic components download: https://chelic.partcommunity.com/
2. Vacuum nozzle, Vacuum generator, Solenoid Valve - 3 port / 2 state: https://www.chelic.com/en/Contact/OfficeT#north

### :small_blue_diamond: EPSON manuals
1. EPSON manual:
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://files.support.epson.com/far/docs/epson_rc_pl_70_users_guide-rc700a_rc90_t(v73r4).pdf  
2. Delta HMI manual: chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://filecenter.deltaww.com/Products/download/06/060302/Manual/DELTA_IA-HMI_DOPSoft_UM_EN_20211230.pdf



