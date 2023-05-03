# Vibrating Ultrasonic Glove
## Table of Contents
1. [Introduction](##Introduction)
2. [Methods](#Methods)
## Introduction
(From Project Proposal)

For our project, we aim to create a vibrotactile tool that will provide feedback based on the distance to the nearest obstacle, serving as an ancillary device for people with low or no vision in addition to a white cane. The device could be used at home or in busier areas, such as a grocery store. In such environments, white canes could take up too much space or may simply be unnecessary due to familiarity of the environment. By using this device as a replacement, or a supplement, precise distance information is gained, which is critical in mobility. 

We will demonstrate the use of this glove with ultrasonic sensing technology, which uses sound waves to measure distance; these waves are emitted at a frequency range too high for humans to hear. Ultrasonic waves do not interfere with radio and electromagnetic waves, used in other day-to-day devices, allowing for comfortable use in daily life.

Our device lies in a wide field of sensing technologies that have a plethora of applications in motion detection, distance measurement, and level gauge. For example, sonar technology is used in water with its high-frequency sound waves allowing for sound propagation.​​ There are also depth-sensing technologies, like laser scanning or stereo cameras, which create a 3-D image of the surrounding environment. Laser scanning projects an infrared laser point/line onto an object and captures its reflection via a sensor. Stereo cameras operate with the use of multiple lenses that contain image sensors, creating a vision disparity. Both these devices utilize trigonometric triangulation and reflection angles to calculate distance and map a 3-D surface. Our project may have applications outside of its niche, contributing to the whole field of ultrasonic sensing technology.

## Methods
We began testing by separately assembling our circuits, one for the ultrasonic sensor and one for the vibrational motor. 
The ultrasonic sensor (HC-SR04) was connected to a breadboard. Using four wires, we connected the sensor to the Arduino. 
For initial tests, the Arduino’s power supply came from a USB Type A/B port connected to a PC. The ultrasonic sensor has 
four pins: VCC, TRIG, ECHO, and GND. TRIG is the trigger input pin, ECHO is the echo output pin, VCC powers the sensor, 
and GND is the common ground. Because VCC is the terminal that powers the sensor, it will be connected to the 5V terminal 
of the Arduino which will supply it with direct power. TRIG will be connected to Pin D11, and ECHO will be connected to 
Pin D10 on the Arduino. Finally,  GND will be connected to a GND channel on the Arduino. Our circuit works by utilizing 
Pulse Width Modulation, PWM, to send out and receive pulse signals. For that reason, the TRIG and ECHO pins on the 
ultrasonic sensors are connected to Pins 10 and 11, which are both digital I/O channels where PWM output is possible. The 
image of the circuit diagram illustrates the pin setup (Fig ?).The sensor works by emitting a sound wave from the ultrasound 
transmitter (TRIG pin) at a high-frequency, inaudible to human ears. If there is an object within the sensor's range, the 
sound wave will hit it and return to the module. This time, the sound wave is being read by the ultrasonic receiver 
(ECHO pin) which receives the reflected sound, the echo. The image of the ultrasonic sensor illustrates how the sound wave 
travels when it hits an object. Distance can be found using the equation:
$$d=(v_s t)/2$$
$d$ is the distance to the object, $v_s$ is the speed of sound, and $t$ is the time between transmission and reception of the 
sound wave. In this way, the sensor, along with code, can calculate distance, which will be converted to electrical signal, 
causing the motor to vibrate. We are able to test using just one sensor and printing out the distance of the closest object repeatedly using the code written in `initial-1sensor-distance.ino`.
