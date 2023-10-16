# 1121 Introduction to Robotics Tutorial 
## ME4609301 (for Taiwan-Paraquay Polytechnic University)
:bulb: In this class, the students can learn the basics of manipulating the operation of industrial robot arms (EPSON robot). The class introduces two types of robots, Pro-6-Axis robots, and SCARA robots, but only utilizes Pro-6-Axis robots in exercises. The main subjects include Introduction to Industrial Robot Arm, Software and Simulation, Calibration and Alignment, I/O port Communication, Human-machine interface (HMI), and Machine vision. In the end, the students possess the capability to design an automatic work cell with the robot. 
## :beginner: Exercises and resources
- Basic and Challenging tasks: (by team)
    - [ ] Basic tasks
    - [ ] Challenging tasks
- Mechanical design and assembling: (group A and B collaboration)  
    - [ ] Gripper
    - [ ] Cylinder
    - [ ] Instruction and reference
- Electrical design and wiring: (group A and B collaboration)
    - [ ] I/O box
    - [ ] HMI
    - [ ] Instruction and reference
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

### Challenging tasks

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
1. Two fixtures, one as primary, the other as secondary (as buffer when there is no space at tray).  
2. Rotate the block in (20 mm x 24 mm) or (24 mm x 20 mm); from the unaligned block pile in Challeng task 2-3.
3. Develop the way to detect the orientations of the block (20 mm x 24 mm); might be gripper or vacuum nozzle. 
- #### Task 4. Tray
1. One tray - keep status in robot memory (occupied or vacancy)
2. Two trays, one at the essential location and one at another with an angle(30 degrees). 
- #### Task 5. GUI
- ##### A. Functionality: 
1. GUI#1 - stack up tokens and blocks alternately at fixture (from feeder to fixture); one button to stack and the other to unstack.
2. GUI#2 - Move tokens and blocks into the tray from feeder to tray (fixture optional); one button forward and one return.
- ##### B. Tools: 
1. I/O box: Start (Green), Reset (Org), Stop (Red); Forward(Blue), Reverse(White)
2. HMI: create the button on touch screen
3. EPSON robot GUI: create the button on touch screen
  
- #### Task 6. Others (optional)
- ##### A. Response to unexpected issues: 
1. Lose power
2. Lose pneumatic (or low pressure)
3. Los I/O signal (hardware malfunction)
4. Emergency Stop 
- ##### B. Function button or GUI - to complete operation cycle:
1. Auto mode / manual mode
2. Reset function 
3. Self-awareness (diagnosis)

## :joystick: Mechanical design and assembling: (group A and B collaboration)
In this sector, students learn how to design the mechanical parts for the gripper on the robot and the cylinder on the peripherals and print and assemble them on the robot system. 
- #### Gripper
1. Design "Finger"
2. 3D print  
3. Assembly
4. Github: drawing and files (for 3D printer).
- #### Cylinder
1. Design "Holder"
2. 3D print 
3. Assembly
4. Github: save drawings and files (for 3D printer).
- #### Instruction and reference
1. Instruction .ppt (follow TA)
2. 3D printer (Phrozen3)
   - Phrozen manual download (Sonic Mini 4K): https://phrozen3d.com/pages/manual
   - Test model file: https://phrozen3d.com/pages/phrozens-xp-finder-and-rp-tester-test-model-download-and-tutorials
   - Tutorial video: https://phrozen3d.com/pages/video-tutorial
   - Software download: https://phrozen3d.com/pages/software
   - Chitubox download: https://www.chitubox.com/en/download/chitubox-free
4. 3D printer (Roland)
   - Roland Technical Support: https://www.rolanddga.com/support/products/3d-printing-devices
   - Tutorial video: https://www.youtube.com/watch?v=uk_OII4pgcA
   - Taiwan Agent: http://www.twinsoft.com.tw/ARM-10/ARM10.htm  
## :eight_pointed_black_star: Electrical design and wiring: (group A and B collaboration)
In this sector, students learn how to illustrate the wiring diagrams for the I/O box and HMI and conduct the wiring and assembly to the I/O Bus of the EPSON robot.
- #### I/O box:
1. Illustrate wiring diagram (.pdf)
   - Cable to button(6): Red, Orange, Green (latch type); Blue, White (unlatch type); buzzer. 
   - I/O box to Robot I/O terminal
2. Wiring and Assembling
3. Github: save drawing and files (.pdf)
4. Reference:
   - Pushbutton Switch:[[reference link](https://www.amazon.com/Latching-Button-Switch-Waterproof-K16-371/dp/B0975WXFTB/ref=sr_1_17_sspa?crid=DO62EE9HW0YB&keywords=16mm%2BPush%2BButton%2BSwitch&qid=1694827804&sprefix=16mm%2Bpush%2Bbutton%2Bswitch%2Caps%2C303&sr=8-17-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1)]
   - Wiring (suggested: No.1, Button On/ LED on)   
      ![image](https://github.com/iiotntust/1121robot/assets/56021651/d3f10f6d-82cf-433b-a58e-2134b93983ee)
- #### HMI:
1. Illustrate wiring diagram
   - Cable to button(6): Red, Orange, Green (latch type); Blue, White (unlatch type); buzzer. 
   - I/O box to Robot I/O terminal
2. Wiring and Assembling
3. Github: save drawing and files (.pdf)
4. Reference
   - HMI (Weintek MT8072ip): software EasyBuilder Pro V6.02.02.248 (2019/06/28) https://www.weintek.com/globalw/Download/Download.aspx
   - WEINTEK forum (EPSON): https://forum.weintekusa.com/t/epson/669
   - WEINTEK forum (EPSON)https://forum.weintekusa.com/t/epson-robot/665
   - WEINTEK HMI full course: [https://youtu.be/9YaUIj5ODLw?si=S0883oPlBQHvz60B](https://www.youtube.com/watch?v=PaFW0P7mkN8&list=PLAol9q3JCKsGbLue6MNgywZ9IXAbHMF4O)
## :eight_pointed_black_star: Machine vision 
In this sector, ................
1. Illustrate wiring diagram (.pdf)
   - Cable to button(6): Red, Orange, Green (latch type); Blue, White (unlatch type); buzzer. 
   - I/O box to Robot I/O terminal
2. Wiring and Assembling
3. Github: save drawing and files (.pdf)
4. Reference:
   
## 📈  Final exam tasks (competition):
1. Designated Task 1: Pick-n-Place
   Criterion 
   - Completed the movement of three tokens and three blocks from the Feeder to Fixture, then to the Tray by order.   
   - Conduct the movement reversely, from Tray to Feeder directly. (Skip the fixture cell)
   Score
   - Totoal Time (the team with shortest time win)
2. Designated Task 2: Stack-up
   Criterion 
   - Stack up tokens and blocks alternatively. (5 token and 5 blocks)  
   Score
   - Totoal Time (the team with shortest time win)
3. Option task:
   Criterion:
   - Adding the challenge tasks in the tasks. 

## 📈  Level of achievement:

To measure the capability of implementation of a robotic project.

|     **Level**    |   **Capbility**  |**To achieve assignments** |
|:------------------:|:--------------:|:-----:|
| 01      | Can set coordinates (world, local, tools) and align tool to work cell.| Complete basic tasks, like the six pieces pick-n-place task (one feeder, one fixture, one tray)
| 02   |Can communicate with a robot to perform selection or make some judgment via I/O or network | manually conduct select feeder, sort token and block via HMI. (in practice, the robot can communicate to the end effectors ( like a screwdriver, soldering gun, glue nozzle, welding torch, etc.; or machine vision to get the location or OCR information|
| 03   |Can plan process to handle expected changes|when one feeder is empty, automatically changes to the other. |
| 04   |Can handle unexpected changes|when lost power, lost pneumatic, E-Stop, can restore system by interference.|
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
### :small_blue_diamond: demo video
1. Basic exercise: pick and place (feeder-->fixture-->tray) https://youtu.be/XQcib0vzzIk
2. Calibration exericise: local/tool coordinates calibration https://youtu.be/TOrHTE-4aC4
