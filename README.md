# Vibrating Ultrasonic Glove
Eric Zhu, Kate Saxen, and Katya Osipova

## Table of Contents
1. [Introduction](#Introduction)
2. [Initial Circuit](#Initial-Circuit)
3. [Initial Tests](#Initial-Tests)
4. [Adding Sensors](#Sensor-Mounting)
5. [Sensor Mounting](#Adding-Sensors)
6. [Mount Tests](#Mount-Tests)
7. [Final Design](#Final-Design)
8. [Hoodie Tests](#Hoodie-Tests)
9. [Conclusion](#Conclusion)

## Introduction 
For our project, we aim to create a vibrotactile tool that will provide feedback based on the distance to the nearest obstacle, serving as an ancillary device for people with low or no vision in addition to a white cane. The device could be used at home or in busier areas, such as a grocery store. In such environments, white canes could take up too much space or may simply be unnecessary due to familiarity of the environment. By using this device as a replacement, or a supplement, precise distance information is gained, which is critical in mobility.

![wewalk-2-768x512](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/f6ac35c7-57af-4ce6-a94a-858ef3ee81a0)

We will demonstrate the use of this glove with ultrasonic sensing technology, which uses sound waves to measure distance; these waves are emitted at a frequency range too high for humans to hear. Ultrasonic waves do not interfere with radio and electromagnetic waves, used in other day-to-day devices, allowing for comfortable use in daily life.

Our device lies in a wide field of sensing technologies that have a plethora of applications in motion detection, distance measurement, and level gauge. For example, sonar technology is used in water with its high-frequency sound waves allowing for sound propagation. There are also depth-sensing technologies, like laser scanning or stereo cameras, which create a 3-D image of the surrounding environment. Laser scanning projects an infrared laser point/line onto an object and captures its reflection via a sensor. Stereo cameras operate with the use of multiple lenses that contain image sensors, creating a vision disparity. Both these devices utilize trigonometric triangulation and reflection angles to calculate distance and map a 3-D surface. Our project may have applications outside of its niche, contributing to the whole field of ultrasonic sensing technology.

## Initial Circuit
For our project's circuitry, we have two main circuits: one for the ultrasonic sensor and one for the vibrational motor. We can start with focusing on the ultrasonic sensor. The ultrasonic sensor works by emitting and receiving an ultrasonic sound wave via a transducer. When the emitted sound wave hits an object, it is reflected back to the sensor which converts it into an electrical signal, with the aid of an Arduino, Fig. 4. 

![Figure-2](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/01e430d8-ef99-4e64-acea-c268178e8dec)
*Fig. 1: The figure shows the use of the trigger and echo in an ultrasonic sensor. A pulse is sent out and returned and can vary depending on the distance of the nearest object. It is important to note that there is a needed delay between the pulses that are sent out for the sensor to work appropriately.*

For our initial circuit setup, we connected an ultrasonic sensor (HC-SR04) was connected to a breadboard. Using four wires, we connected the sensor to the Arduino. In order to run the code and power the Arduino, we connected it to a USB Type A to B port connected to a PC. The ultrasonic sensor has four pins: VCC, TRIG, ECHO, and GND. TRIG is the trigger input pin, ECHO is the echo output pin, VCC powers the sensor, and GND is the common ground. Because VCC is the terminal that powers the sensor, it will be connected to the 5V terminal of the Arduino which will supply it with direct power. TRIG will be connected to Pin D11, and ECHO will be connected to Pin D10 on the Arduino. Finally,  GND will be connected to a GND channel on the Arduino. Our circuit works by utilizing Pulse Width Modulation, PWM, to send out and receive pulse signals. For that reason, the TRIG and ECHO pins on the ultrasonic sensors are connected to Pins 10 and 11, which are both digital I/O channels where PWM output is possible (Fig ?). The sensor works by emitting a sound wave from the ultrasound transmitter (TRIG pin) at a high-frequency, inaudible to human ears. If there is an object within the sensor's range, the sound wave will hit it and return to the module. This time, the sound wave is being read by the ultrasonic receiver 
The ultrasonic sensor (HC-SR04) was connected to a breadboard. Using four wires, we connected the sensor to the Arduino. (ECHO pin) which receives the reflected sound, the echo. The image of the ultrasonic sensor illustrates how the sound wave travels when it hits an object. Distance can be found using the equation:
$$d=(v_s t)/2$$
$d$ is the distance to the object, $v_s$ is the speed of sound, and $t$ is the time between transmission and reception of the sound wave. In this way, the sensor, along with code, can calculate distance, which will be converted to electrical signal, causing the motor to vibrate. We are able to test using just one sensor and printing out the distance of the closest object repeatedly using the code written in `initial-1sensor-distance.ino`.

The second circuit is the vibrational motor circuit. This circuit has more components. One end of the vibration motor 
(polarity can be disregarded) will get a direct power supply from the 3.3V pin of the Arduino, this will allow it to vibrate 
strongly. In parallel with the motor will be a diode that is reverse-biased. This serves to act as a surge protector for 
the arduino as the motor produces voltage spikes as it rotates. Without the diode, the voltage surges could damage the Arduino. 
The capacitor, also in parallel with the motor, absorbs these voltage spikes. A transistor is placed in series with the motor, 
which provides it with current amplification as the Arduino provides a relatively weak power supply. Then, the motor is able 
to run more powerfully, allowing for more range of vibration depending on how close to an object the sensor is. A 1 K ohm 
resistor is placed in series with the transistor so not too much current is being supplied to the motor. This end of the 
circuit is connected to the D3 pin of the Arduino, which is a channel that allows PWM. This digital pin will be set to output

## Initial Tests
With our full circuit setup, we can conduct our first initial test with the code writen in `initial-1sensor-1buzzer1motor.ino`. From this, we can calculate the working range of a single sensor as a starting point for how our final setup will operate. We create a mount setup to sweep a rod both up and down and side to side while looking for a jump in the distance reported to locate the outer boundaries of the sensor in both the directly up and down direction and side to side direction. Since we are given the supposed working range of the sensors, we can compare our results to the datasheet. With each of the distances we use, we can create a plot to visualize the working range in both directions.

![Figure_1](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/6cbcc4c7-78c5-4956-bea1-70cfe85b2433)

As we see in Fig ?, there is a clear outward fanning shape for the vertical working range. This makes sense due to the shape of the sensors likely blocking some nearby waves while being able to accept a larger range from farther away. This works well for our project as we are focused on detecting objects farther away in order to alert the user of an incoming obstacle rather than detecting it too late. However, this makes it harder to compare our results to the values in the datasheet. We can calculate our working range in two ways. The first, we can use a linearization from the plot to map the working range. This yields an approximate value of 18 degrees. We can alternatively calculate it using the end points of our plot as we are more focused on the working range farther away from our sensor. This yields an approximate value of 25 degrees.

## Sensor Mounting

In order for the ultrasonic sensor circuit to work well, it must have a stable mount. Because our project is geared towards serving those with visibility impairments, it is of paramount importance that our design cover as much surface area in front of the user as possible. Therefore, the main design feature of our mount is the three angled faces, meant to be occupied by three HC-SR04 sensors, which reduces the apparatus's vertical blindspots to a minimum. The mount itself was made using a 3-D printer and a design program called (x-ask Katya about this part).

(insert image of mount design)

Our early designs included a flat faced mount with space for three sensors, but this design was omitted because there was too much overlap in the transmitter's wave emission and not enough dimension in measuring distance to an object. The design that we agreed upon increased the ability of the sensors to detect objects on the ground and near the user, as well as at waist, torso, and head heights.

As an aside, we know that the sensors lack measuring capabilities in front of the transducer. Because we want the vibrational motor to stop before the user hits an object, we are not concerned about this blindspot. Rather, it helps us in cutting off the vibrational motor, alerting the user that they are directly in front of an obstacle.

Initially we had planned on attaching the sensors by sticking velcro to the back sides of them and the faces of the mount. This did not provide much stability as the velcro was not very strong and the sensors were not pointing outwards perpendicular to the face of the mount. Instead, we drilled the sensors into the mount with (insert screw type and describe how they were screwed in, melted). This provided a sturdy base as the sensors could not be shaken off the mount, and the emitted waves would be sent straight outward rather than at an offset angle.

Another main feature of the mount is the hollow interior and an open strips on the top and middle face; we do not need one of the bottom face as it has direct access to the hoodie's pcoket. This provides us with the ability to feed the sensors wires through the mount and out the bottom. When attaching the mount to the hoodie, this makes it more convenient to connect the sensors to the microcontroller and thus, the vibration circuit, which will both be kept in the hoodie's pocket. 

need to add in images of the mounting process
-ask katya what the angles on the mount were and well as how she drilled the sensors into the mount.

## Adding Sensors

not done editing
In attaching the sensors to the mount, they had to be prepped. We began by sodering off the ECHO, TRIG, GND, and VCC pins as they would not allow the sensors to lay flat on the mount's face as well as taking up unnecesary space in a small volume. In place of the pins, four long wires were sodered through the holes that the  pins previously occupied. Each VCC, TRIG, and GND wire from

The electrical signals that will be controlling the vibrational motor will be receiving its input from data from the ultrasonic sensor


## Mount Tests

## Final Design

## Hoodie Tests

## Conclusion


