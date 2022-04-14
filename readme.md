This lab aimed to image with a single photodiode and a projector
This respository is my note for this lab. 

<br/>
This lab use (Launchpad)MSP-EXP430F5529LP, the sensor circuit connected to P6.0

By getting the voltage of P6.0, we can get the lightness of the sensor. The launchpad connects to the computer by a USB line.


<br/>
capture_image.py: 

Output the mask matrix to projector and  communicate with the launchpad to get the sensor input data and store it


single_piexl.py/multi_piexl.py: 

(1) create the Mask and write into files (2) reconstruct image from the result by capture_image.py

helpers.py: some functions for single_piexl.py/multi_piexl.py to call



<br/>

Steps:

1. Install and open the Energia app on windows, and run the program AnalogReadSerial.ino, upload from computer to the launchpad. Click reset button on the launchpad, so then the launchpad can send data to computer.
2. check the port of usb, and then set the baudrate 115200 in SerialMonitor of Energia，send 6 in SerialMonitor, it will respond the voltage of P6.0
3. single_piexl.py/multi_piexl.py (run capture_image.py in terminal in the middle of the program )



Details of this lab instructions: The tutorial folder
