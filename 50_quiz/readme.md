# [1121] Robot class 50-QUIZ Bank

:bulb: This is the Quiz-bank for midterm examination preparation and homework. 

:white_check_mark:**Rule:** 2 points for each quiz, 100 points.   
:white_check_mark:**Quiz type:** single or multi-selection.   
:white_check_mark:**Scope:** handouts in class and EPSON robot manual RC+5.0, RC+7.0, RC180 manuals (available on Moodle system). 

:bulb: All quiz answers should be found in the handout and manuals; only a few quiz answers are mentioned in class by the TA or Teacher. The answers would not be announced until mid-term exams finish. 

 
1121 Robot tutorial course – quiz bank
[Selection type] – 50 quizzes. 

## :pencil: Part I: General 
Introduction and robotic general concept. 

### 1. Which EPSON robot model series is not in the EPSON 6-AxisPro. 
- [ ] A. C series
- [ ] B. VT series 
- [ ] C. S5 series
- [ ] D. G series

### 2. Which robot has the longest arm? 
- [ ] A. S-901S
- [ ] B. S-A600S 
- [ ] C. S-700S
- [ ] D. C12XL 6-Axis Robot

### 3. Which company does not make industrial robot arm? 
- [ ] A. ABB Ltd.
- [ ] B. Fanuc Corp. 
- [ ] C. iRobot
- [ ] D. Epson Robots

### 4. What components included in the workcell of robotic exercies platform?
- [ ] A. Feeder cell
- [ ] B. Tray
- [ ] C. Fixture
- [ ] D. Reference pole (rod)
- [ ] F. All above

### 5. Which end-effectors are excluded in the exercises? (Multi-selectrion)
- [ ] A. Gripper
- [ ] B. Vacuum nozzle
- [ ] C. Screwdriver
- [ ] D. Torch
- [ ] E. Soldering gun
- [ ] F. Glue gun 

### 6. What protocol is not for connecting PC to EPSON robot? 
- [ ] A. Fieldbus
- [ ] B. USB port
- [ ] C. Ethernet
- [ ] D. WiFi 

### 7. Which desciption below is not true regarding RC180 controller? 
- [ ] A. RC180 possessed embedded 50-pin i/o bus 
- [ ] B. RC180 does not have any external ports.
- [ ] C. Emergency Stop I/O cannot be used for general purpose
- [ ] D. Can connect either npn or pnp sensors

### 8. In peneumatic system, which component connects to I/O port and driven by electric? (multi-selection)
- [ ] A. Solenod
- [ ] B. Vacuum filter
- [ ] C. Cylinder
- [ ] D. Gripper
- [ ] F. Pressure gauge 
- [ ] G. Silencer
- [ ] H. Vacuum generator 

### 9. Which pneumatic component does not include in the workcell of our class? 
- [ ] A. Pressure gauge
- [ ] B. Solenoid
- [ ] C. Vacuum Filter 
- [ ] D. Rotary cylinder

### 10. What tasks should I complete in the class? 
- [ ] A. Exercise #1: Calibration and Alignment
- [ ] B. Exercise #2: I/O and port communication
- [ ] C. Final exercise: with challenging tasks
- [ ] D. Create a repository at Github as the collaborative platform for the team to keep all data in the class
- [ ] E. Design mechnial parts and print them with 3D printer
- [ ] F. Illustrate the wiring diagram for connecting I/O box to the Robot I/O port.  

## :pencil: Part II: Hardware and coordinates (20 quizzes)   
Manipulator, controller, work cell, fixtures, schematic, wiring, etc. (EPSON installation and maintenance manuals)

1.	Which components/sockets/connector name below is not correct?  
 
-	[ ] A. Power Switch (On/Off)
-	[ ] B. 50-pin I/O connector
-	[ ] C. Emergency Stop  
-	[ ] D. Expansion I/O terminal

2.	About the EPSON Robot model numbering – C4-A901S, which statement is not correct. 
-	[ ] A. A – Series.
-	[ ] B. 9 – load. 
-	[ ] C. 0 – arm length.
-	[ ] D. 1 – Axis brake. 
-	[ ] E. S – SLAM  

3.	In a floor-mounted robot’s configuration, the “right-hand rule” is an easy way to recognize the World frame orientation in space. What statement below is incorrect?
-	[ ] A. Pointer finger (or index finger) – X axis.
-	[ ] B. Middle finger – Y axis. 
-	[ ] C. Thuub – Z axis. 
-	[ ] D. @Local frame – Axis brake. 
-	[ ] E. @Tool fram – J6 Tool mount   

4.	What description below is incorrect?
-	[ ] A. Local 0 is also called World coordinate to a robot
-	[ ] B. Tool 0 can not be changed 
-	[ ] C. With RC-180, 24 local coordinates and 16 tool coordinates are available. 
-	[ ] D. Release the E-Stop before turning on the robot controller.

5.	The “J” in the “JTran” command represents __________. 
-	[ ] A. Joint 
-	[ ] B. Jump
-	[ ] C. Jogging 
-	[ ] D. J-Type connector

6.	Choice the correct description for “TGo” and “BGo”  
-	[ ] A. T means Tool coordinate.
-	[ ] B. B means Base coordinate. 
-	[ ] C. The answers in A and B both are correct. 
-	[ ] D. No correct answer.

7.	What’s the meaning of “Here”
-	[ ] A. Current Flange-End to World coordinate
-	[ ] B. The last executed point of the local
-	[ ] C. Point of Home
-	[ ] D. Original point of current coordinate

8.	Which description is correct about standard I/O? 
-	[ ] A. The output voltage is 110 volts.
-	[ ] B. There are 24 input signals (DI). 
-	[ ] C. There are 24 output signals (DO).  
-	[ ] D. The I/O connector is a D-sub 25-pin. 

9.	What message is not included in the LED display of the I/O controller (RC180)? 
-	[ ] A. Error 
-	[ ] B. Warning 
-	[ ] C. Emergency Stop
-	[ ] D. Start
-	[ ] F. Sleep mode

10.	The following description of local/tool coordinates is correct?  
-	[ ] A. World coordinate is not local 0
-	[ ] B. The Z-axis of tool 1 should align and parallel to the J6 axis. 
-	[ ] C. Tool 0 is the center of the J6 mount. 
-	[ ] D. The maximum number of local coordinates is 10. 

11.	What environmental status is not appropriate for the EPSON robot controller installation?
-	[ ] A. Ambient temperature: 5 to 40 deg.C (with minimal variation)
-	[ ] B. Ambient relative humidity: 20% to 80% (with no condensation)
-	[ ] C. Electrostatic noise: 4KV or higher 
-	[ ] D. Base table: Use a base table that is at least 100 mm off the floor.

12.	Which specification of the Power Supply is not correct?   
-	[ ] A. Voltage: 200 VAC to 240 VAC
-	[ ] B. Phase: three phase
-	[ ] C. Frequency: 50/60 Hz 
-	[ ] D. Momentary Power Interrupt: 10 ms Or less
-	[ ] E. Power consumption: Max. 2.5 KVA
-	[ ] F. Peak current: Power ON, approx. 150 A (2 ms); Motor ON, approx. 60 A (5 ms). 

13.	Which description of the operation mode is correct? 
-	[ ] A. In TEACH mode, the Robot operates in Low power status. 
-	[ ] B. Auto mode does not include program mode. 
-	[ ] C. AUTO mode includes TEACH mode, Program mode, and Auto mode.  
-	[ ] D. AUTO mode can not enable automatic operation (program execution).


14.	Which step in the procedure to save the status of the Controller to USB memory is not correct?
-	[ ] A. Insert the USB memory into the memory port, then wait approx. 10 seconds for USB memory recognition. 
-	[ ] B. Press the trigger button on the Controller. 
-	[ ] C. When the storage has been completed, -00- is displayed on the seven-segment for two seconds. 
-	[ ] D. When the storage has failed, -EE- is displayed on the seven-segment for two seconds.
-	[ ] F. When storage is executed during Motor ON status, it won’t cause any problem.

15.	Which description of the Emergency connector is not correct? 
-	[ ] A. Two Emergency Stop circuits (ESTOP1 and ESTOP2)
-	[ ] B. Two Safety Door Latch Release (SDLATCH1 and SDLATCH2)
-	[ ] C. Four Safety Door Input (SD11, SD12, SD21, SD22)
-	[ ] D. D-sub 30 male pin Mounting style #4 – 40

16.	About robot maintenance, which statement below is not correct? 
-	[ ] A. In the controller, the “General” dialog box can display the installation date of the battery and consumption ratio. 
-	[ ] B. An alarm occurs when the consumption rate of parts reaches 100%
-	[ ] C. “Change Alarm” does not include the purchase or replacement date of the reduction gear unit.  
-	[ ] D. The alarm notifying method can be configured by the output bit of the Remote I/O.
-	[ ] E. The alarm cannot be canceled by executing the Reset command or restarting the controller but by the [Maintenance] dialog box.

17.	About Maintenance Inspection, which statement is not correct? 
-	[ ] A. Inspection points are divided into five stages: daily, monthly, quarterly, biannual and
annual.
-	[ ] B. If the robot system is operated for 250 hours or more per month, inspection points must be added every 250 hours, 750 hours, 1500 hours, and 3000 hours of operation.
-	[ ] C. Clean the fan filter on the side of the controller only performed Quarterly.   
-	[ ] D. Battery front side check every 5 years. 

18.	Which Option Unit is not listed in the RC180 controller? 
-	[ ] A. Expansion I/O Board
-	[ ] B. Fieldbus I/O Board
-	[ ] C. RS-232C Board 
-	[ ] D. BACnet board

19.	The Fieldbus I/O option can add the Fieldbus slave functions to the robot controller, which one does not include? 
-	[ ] A. DeviceNet
-	[ ] B. PROFIBUS-DP
-	[ ] C. PROFINET 
-	[ ] D. CC-Link
-	[ ] E. EtherNet/IP
-	[ ] F. All the above are included. 

20.	Please find the description of the Errors code table is not correct in the maintenance chapter.  
-	[ ] A. There are 18 types of errors in error codes. 
-	[ ] B. Event code: from 1 to 426.  
-	[ ] C. Warnings code: start from 501.  
-	[ ] D. Controller Main: 1001 ~ 
-	[ ] E: Motor Control: 4001 ~
-	[ ] F: all above are not correct

## :pencil: Part III: Programming   
SPEL+ Language, GUI,...... 

1.	In the Function Test of “Do….While” which description below is not correct? 
Function Test
	Integer i
	i = 1
	Do While i < 4
		Print i
		i = i + 1
	Loop
Fend

-	[ ] A. Add While after Do, and only perform the Do loop when the discriminant is established.
-	[ ] B. Add Until after Do, and stop the Do loop when the discriminant is established.
-	[ ] C. Terminating the loop when i= 4.
-	[ ] D. Debug mode cannot be used to verify the program. 

2.	What description is not correct regarding the following code?  
Function Test
	Motor On
	Home
	P1 = XY(200, 450, 300, 0, 180, 0)
	P2 = XY(0, 450, 300, 0, 180, 0)
	P3 = XY(-200, 450, 300, 0, 180, 0)
	Integer i
	i = 1
	Do While i < 4
		Go P(i) +Z(50)
		Go P(i)
		Go P(i) +Z(50)
		i = i + 1
	Loop
	Home
Fend
-	[ ] A. If we remove i = i + 1, it becomes an infinite loop. 
-	[ ] B. The robot arm goes P1, P2, P3, and Home in sequence four times. 
-	[ ] C. Stop at Home in the end. 
-	[ ] D. Z(50) means Z axiz = 50 mm. 

3.	In the following code, which description is not correct?
Function Test
	Integer feed5Ready
	feed5Ready = Sw(5)
	'Check if feeder5 is ready
	If feed5Ready = On Then
		Call PP
	Else
		Print " Input 5 switch is not ON"
		Print " Press Start "
	EndIf
	On(5)
Fend
Function PP
	Print "Input 5 switch is ON"
Fend

-	[ ] A. When Sw(5) = 0, enter “Else” and print "Input No. 5 switch is not ON" and "Press Start".  
-	[ ] B. When Sw(5) = 1, enter “Then” and print "Input No. 5 switch is ON", and then activate Output 5.
-	[ ] C. The name of the calle Function is PP. 
-	[ ] D. Pressed No. 5 button to enter the called Function during debugging.

4.	Which statement (or claim) about “Time” is not correct?  
-	[ ] A. Time$, covert number to text format.
-	[ ] B. Integer hr, hr = Time(0), set time unit = hour. 
-	[ ] C. Integer min, min = Time(1), set time unit = minute.  
-	[ ] D. Integer sec, sec = Time(2), set time unit = sec. 


5.	In the Pallet command - Pallet palletNumber, Pi, Pj, Pk [,Pm ], columns, rows.; what statement is not correct?  
-	[ ] A. palletNumber Pallet number represented by an integer number from 0 to 15
-	[ ] B. Pi, Pj, Pk Point variables which define standard 3-point pallet position
-	[ ] C. Pm Optional. Point variable which is used with Pi, Pj, and Pk to define 3 point pallet.
-	[ ] D. columns Integer expression representing the number of points on the Pi-to-Pj side of the pallet. The range is from 1 to 32767.
-	[ ] F. rows Integer expression representing the number of points on the Pi-to-Pk side of the
-	pallet. The range is from 1 to 32767.

6.	Which description of EPSON RC+5.0 features is not correct?
-	[ ] A. Runs on Microsoft Windows XP, Windows Vista, and Windows 7, but not Windows 10. 
-	[ ] B. One PC can be used to manage several controllers.
-	[ ] C. SPEL+ programming language. A powerful, easy-to-use BASIC-like programming language that supports multi-tasking, robot motion control, I/O control, and networking. 
-	[ ] D. Have “Wizards” for robot tools, local coordinate systems, robot calibration


7.	What statement is not true about “Commands” and “Statements” in SPEL+ language?
-	[ ] A. A command is executed immediately.
-	[ ] B. Statements can be used only in programs.
-	[ ] C. Statements can include more than one SPEL+ instruction by using a semi-colon (;) to separate instructions. 
-	[ ] D. The maximum length for a statement is 20 characters.

8.	Which naming restriction about Function and variable names is not true? 
-	[ ] A. Function and variable names can include up to 32 alphanumeric characters and the underscore character.
-	[ ] B. Characters can be upper case or lower case.
-	[ ] C. Function and variable names can begin with a numeric digit or underscore. 
-	[ ] D. The strings that are already used as keywords cannot be used. (Example: Go / On)

9.	About the “String” description, which one is not correct? 
-	[ ] A. The strings that are already used as keywords cannot be used. (Example: Go / On)
-	[ ] B. String variables must have an additional dollar sign ('$') suffix.
-	[ ] C. String size is 4 bytes. 
-	[ ] D. String variables should be placed in the front of the sketch. 

10.	Which description of operators for the SPEL+ language is not correct?
-	[ ] A. And - Performs logical and bitwise AND operation
-	[ ] B. Xor - Performs the bitwise Xor operation on the values of the operands.
-	[ ] C. Mod - Returns the remainder obtained by dividing a numeric expression by another numeric expression.
-	[ ] D. ** - Exponentiation
-	[ ] F. All the above are correct. 

11.	There are three different scopes for variables in SPEL+, which one below is not included?  
-	[ ] A. Local variables
-	[ ] B. Module variables
-	[ ] C. Global variables 
-	[ ] D. Special variables


12.	What description of Global variables below is not correct? 
-	[ ] A. Global variables can be shared between all functions in a project.
-	[ ] B. To declare global variables at the beginning of the program before any Function statements.
-	[ ] C. One way to indicate that variables are global is to precede the name with "g_". 
-	[ ] D. Preserved variables are stored in the remote computer.

13.	Which description of string commands available in SPEL+ is not correct?
-	[ ] A. Asc: Returns the decimal ASCII value of the first character in a string.
-	[ ] B. Chr$: Converts a one character string into an ASCII value.
-	[ ] C. InStr: Returns the position of a substring within a string. 
-	[ ] D. Len: Returns the length (number of characters) of a string.

14.	Which statement about Labels is correct?   
-	[ ] A. A program label is an alphanumeric name followed by a colon (":")
-	[ ] B. Label used to mark a location in a program for a GoTo or GoSub statement. (example: MainAbort: )
-	[ ] C. The name may be up to 32 characters long.
-	[ ] D. You cannot use any SPEL+ keywords as labels.
-	[ ] F. All the above are correct.  

15.	What statement about Error handling is not correct? 
-	[ ] A. OnErr: Use the OnErr statement to define the location of the error handling routine.
-	[ ] B. Error: Generate a user defined error which can be caught by an error handler.
-	[ ] C. Err: Generate a user defined error which can be caught by an error handler.  
-	[ ] D. ErrMsg$: Use ErrMsg$ to retrieve the error message associated with a specified error number.

16.	What description of Multi-tasking is not correct?  
-	[ ] A. SPEL+ supports up to 16 tasks running simultaneously.
-	[ ] B. Use the Xqt statement to start another task from within a function.
-	[ ] C. “Resume” is not the Statement in Multi-tasking.   
-	[ ] D. Xqt Conveyor means “Start the conveyor task”. 

17.	Which one coordinate system is not included in the EPSON robot coordinate system? 
-	[ ] A. Robot Coordinate System
-	[ ] B. Local Coordinate System
-	[ ] C. Tool Coordinate System 
-	[ ] D. World Coordinate System

18.	Regarding Tool Coordinate Systems, which statement in the following is not correct?  
-	[ ] A. TOOL 0 of a 6-axis robot is the flange side center of the sixth joint.
-	[ ] B. The position is specified by the position data (X, Y, Z).
-	[ ] C. The orientation is specified by the orientation data (U, V, W). 
-	[ ] D. The default TOOL 0 coordinate systems are defined by the user. 

19.	What description of ECP (external control point) is not correct?   
-	[ ] A. An ECP motion is when the robot arm holding a part follows a specified trajectory (part’s edges, etc.) using an outside fixed tool.
-	[ ] B. ECP definition by ECPSet statement and selection by ECP statement.
-	[ ] C. ECP motion commands cannot execute additional functions of Move, Arc3, Curve, and CVMove commands. 
-	[ ] D. Up to 15 ECP coordinate systems can be defined. 

20.	Which type of I/O is not included in the RC180 controller I/O?  
-	[ ] A. Standard I/O
-	[ ] B. Expansion I/O
-	[ ] C. Fieldbus I/O 
-	[ ] D. Memory I/O 
-	[ ] F. Virtual I/O

 
