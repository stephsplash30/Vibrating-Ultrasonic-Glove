# Vibrating Ultrasonic Glove
Eric Zhu, Kate Saxen, and Katya Osipova

## Table of Contents
1. [Introduction](##Introduction)
2. [Initial Circuit](##Initial-Circuit)
3. [Initial Tests](##Initial-Tests)
4. [Adding Sensors](##Adding-Sensors)
5. [Sensor Mounting](##Sensor-Mounting)
6. [Mount Tests](##Mount-Tests)
7. [Final Design](##Final-Design)
8. [Hoodie Tests](##Hoodie-Tests)
9. [Conclusion](##Conclusion)

## Introduction 
For our project, we aim to create a vibrotactile tool that will provide feedback based on the distance to the nearest obstacle, serving as an ancillary device for people with low or no vision in addition to a white cane. The device could be used at home or in busier areas, such as a grocery store. In such environments, white canes could take up too much space or may simply be unnecessary due to familiarity of the environment. By using this device as a replacement, or a supplement, precise distance information is gained, which is critical in mobility.

![wewalk-2-768x512](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/f6ac35c7-57af-4ce6-a94a-858ef3ee81a0)

We will demonstrate the use of this glove with ultrasonic sensing technology, which uses sound waves to measure distance; these waves are emitted at a frequency range too high for humans to hear. Ultrasonic waves do not interfere with radio and electromagnetic waves, used in other day-to-day devices, allowing for comfortable use in daily life.

Our device lies in a wide field of sensing technologies that have a plethora of applications in motion detection, distance measurement, and level gauge. For example, sonar technology is used in water with its high-frequency sound waves allowing for sound propagation. There are also depth-sensing technologies, like laser scanning or stereo cameras, which create a 3-D image of the surrounding environment. Laser scanning projects an infrared laser point/line onto an object and captures its reflection via a sensor. Stereo cameras operate with the use of multiple lenses that contain image sensors, creating a vision disparity. Both these devices utilize trigonometric triangulation and reflection angles to calculate distance and map a 3-D surface. Our project may have applications outside of its niche, contributing to the whole field of ultrasonic sensing technology.

## Initial Circuit
For our project's circuitry, we have two main circuits: one for the ultrasonic sensor and one for the vibrational motor. For our initial circuit setup, we connected an ultrasonic sensor (HC-SR04) was connected to a breadboard. Using four wires, we connected the sensor to the Arduino. In order to run the code and power the Arduino, we connected it to a USB Type A to B port connected to a PC. The ultrasonic sensor has four pins: VCC, TRIG, ECHO, and GND. TRIG is the trigger input pin, ECHO is the echo output pin, VCC powers the sensor, and GND is the common ground. Because VCC is the terminal that powers the sensor, it will be connected to the 5V terminal of the Arduino which will supply it with direct power. TRIG will be connected to Pin D11, and ECHO will be connected to Pin D10 on the Arduino. Finally,  GND will be connected to a GND channel on the Arduino. Our circuit works by utilizing Pulse Width Modulation, PWM, to send out and receive pulse signals. For that reason, the TRIG and ECHO pins on the ultrasonic sensors are connected to Pins 10 and 11, which are both digital I/O channels where PWM output is possible (Fig ?). The sensor works by emitting a sound wave from the ultrasound transmitter (TRIG pin) at a high-frequency, inaudible to human ears. If there is an object within the sensor's range, the sound wave will hit it and return to the module. This time, the sound wave is being read by the ultrasonic receiver 
The ultrasonic sensor (HC-SR04) was connected to a breadboard. Using four wires, we connected the sensor to the Arduino. (ECHO pin) which receives the reflected sound, the echo. The image of the ultrasonic sensor illustrates how the sound wave travels when it hits an object. Distance can be found using the equation:
$$d=(v_s t)/2$$
$d$ is the distance to the object, $v_s$ is the speed of sound, and $t$ is the time between transmission and reception of the sound wave. In this way, the sensor, along with code, can calculate distance, which will be converted to electrical signal, causing the motor to vibrate. We are able to test using just one sensor and printing out the distance of the closest object repeatedly using the code written in `initial-1sensor-distance.ino`.

Next, we can attach our motor and buzzer circuit (explain it here @katya @kate)

## Initial Tests
With our full circuit setup, we can conduct our first initial test with the code writen in `initial-1sensor-1buzzer1motor.ino`. From this, we can calculate the working range of a single sensor as a starting point for how our final setup will operate. We create a mount setup to sweep a rod both up and down and side to side while looking for a jump in the distance reported to locate the outer boundaries of the sensor in both the directly up and down direction and side to side direction. Since we are given the supposed working range of the sensors, we can compare our results to the datasheet.

(1 blind spot results here)

## Adding Sensors

## Sensor Mounting

In order for the ultrasonic sensor circuit to work well, it must have a stable mount. The main design feature of our mount is the three angled faces meant to reduce the sensors blindspot as much as possible. Because our project is geared towards serving those with visibility impairments, it is of paramount importance that our design cover as much surface area in front of the user as possible. The degree to which each sensor can detect an object in front of it is about 30 degrees. When coming up with our project design, we knew that the best results would come from having multiple HC-SR04 set up in such a way that vertical blindspots could be reduced as much as possible. With the way our mounts are set up, this goal is achieved. As an aside, we know that the sensors lacks measuring capabilities in front of the sensor's transducer. Because we want the vibrational motor to stop before the user hits an object, we are not concerned about this blindspot. Rather, it helps us in alerting the user that they are approaching an obstacle.

Initially we had planned on attaching the sensors by sticking velcro to the back sides of them and the faces of the mount. This did not provide much stability as the velcro was not very strong and the sensors were not pointing outwards perpendicular to the face of the mount. Instead, we drilled the sensors into the mount with (insert screw type). This provided a sturdy base for the sensors and emitted waves would be pointing straight outard rather than an offset angle.

Another main feature of the mounts is that it has a hollow center and an open strip on the top and middle face; we do not need one of the bottom face as it has direct access to the hoodie's pcoket. This provides us with the ability to feed the sensors wires through the mount and out the bottom. When attaching the mount to the hoodie, this makes it more convenient to connect the sensors to the microcontroller and thus, the vibration circuit, which will both be kept in the hoodie's pocket. 

need to add in images of the mounting process
-ask katya what the angles on the mount were and well as how she drilled the sensors into the mount.

## Mount Tests

## Final Design

## Hoodie Tests

## Conclusion


