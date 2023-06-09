# Vibrating Ultrasonic Glove
Eric Zhu, Kate Saxen, and Katya Osipova

## Table of Contents
1. [Introduction](#Introduction)
2. [Initial Circuit](#Initial-Circuit)
3. [Final Design](#Final-Design)
4. [Testing Apparatus](#Testing-Apparatus)
5. [Sensor Mounting](#Sensor-Mounting)
6. [Adding Sensors](#Adding-Sensors)
7. [Initial Tests](#Initial-Tests)
8. [Mount Tests](#Mount-Tests)
9. [Hoodie Tests](#Hoodie-Tests)
10. [Conclusion](#Conclusion)

## Introduction 
For our project, we aim to create a vibrotactile tool that will provide feedback based on the distance to the nearest obstacle, serving as an ancillary device for people with low or no vision in addition to a white cane. The device could be used at home or in busier areas, such as a grocery store. We hope to expand usage to bustling streets. In such environments, white canes could take up too much space or may simply be unnecessary due to familiarity of the environment. Overall, the size of a white cane is the main disadvantage, as it can be a safety hazard to the user or the surrounding people. Additionally, the stigmatization of mobility aids such as the white cane makes those with disabilities less inclined to adopt it. By using this device as a replacement, or a supplement, precise distance information is gained, which is critical in mobility. Our goal is to be able to work as well as a white cane, while making our device more compact and seamless to use in comparison.

<img src= "https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/0ba0eedf-cd50-439e-876d-bdeef5013623" width="700" >

We will demonstrate the use of this device with ultrasonic sensing technology, which uses sound waves to measure distance; these waves are emitted at a frequency range too high for humans to hear. Ultrasonic waves do not interfere with radio and electromagnetic waves, used in other day-to-day devices, allowing for comfortable use in daily life.

Our device lies in a wide field of sensing technologies that have a plethora of applications in motion detection, distance measurement, and level gauge. For example, sonar technology is used in water with its high-frequency sound waves allowing for sound propagation. There are also depth-sensing technologies, like laser scanning or stereo cameras, which create a 3-D image of the surrounding environment. Laser scanning projects an infrared laser point/line onto an object and captures its reflection via a sensor. Stereo cameras operate with the use of multiple lenses that contain image sensors, creating a vision disparity. Both these devices utilize trigonometric triangulation and reflection angles to calculate distance and map a 3-D surface. Our project may have applications outside of its niche, contributing to the whole field of ultrasonic sensing technology.


## Initial Circuit
For our project's circuitry, we have two main circuits: one for the ultrasonic sensor and one for the vibrational motor. 

Ultrasonic sensors use ultrasonic sound waves which are waves of high amplitude, above the approximate upper limit of audible human range at 20 kHz. An ultrasonic sensor works by emitting sound waves from a transmitter module. When an emitted sound wave hits an object within the sensor's range, it is reflected back to the receiver module (Fig. 1). For our initial circuit setup, we connected an ultrasonic sensor (HC-SR04) to a breadboard. Using four wires, we connected the sensor to the Arduino. In order to run the code and power the Arduino, we connected it to a USB Type A to B port connected to a PC. The ultrasonic sensor has four pins: VCC, TRIG, ECHO, and GND. In addition, there is a transmitter module as well as a receiver module on either side of the sensor and a crystal oscillator as illustrated in (Fig. 2):

<img width="534" alt="Screen Shot 2023-06-09 at 9 02 31 PM" src="https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/48030b35-e187-407f-812a-6214244ba87f">

***Fig. 1:** The figure shows how sound waves travel between the transmitter and receiver modules of the ultrasonic sensor and how the waves are reflected off of an object back*

<img width="759" alt="Screen Shot 2023-06-09 at 9 02 20 PM" src="https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/a6afde2e-d798-4168-8b5b-bdc756a3d8ce">

***Fig. 2:** The figure shows the ultrasonic sensor set up. It has four pins: VCC, Trig, Echo, and GND, which are located on the bottom of the diagram. On either side there is a transmitter module and a receiver module, and on the top of the diagram there is a transducer/crystal oscillator.*

Our circuit works by utilizing Pulse Width Modulation, PWM, to send out and receive pulse signals. The VCC pin (or Voltage Common Connector) supplies a 5 DC voltage from the 5 volt Arduino pin. The Trig pin (initially connected to Pin D11 on the Arduino) receives this pulse of voltage thus initiating the sensor to transmit 8 cycles of ultrasonic burst at 40 kHz for at least 10 microseconds. If there is an object within the sensor's range of 2 cm to 400 cm and measuring angle of 30 degrees, the waves will bounce back to the sensor. It is then  the receiver that detects the returned burst. The Echo pin (connected to Pin D10 on the Arduino) gets set to 5 volts and a delay for the period (width) is measured. When the width is measured, the distance can be calculated as they are proportional. Pins D10 and D11 are both digital I/O channels where PWM output is possible. We will later expand to use more pins as we add additional sensors. The GND pin works to ground the overall system. This process can be visualized in (Fig. 3), as it converts one large pulse into an acoustic burst, which is returned to the sensor. The gap between the Trigger and Echo allows us to convert that into a distance eventually. Distance can be found using the equation:

$$d=(v_s t)/2$$

$d$ is the distance to the object, $v_s$ is the speed of sound at approximately 343 m/s, and $t$ is the time between transmission and reception of the sound wave. In this way, the sensor, along with code, can calculate distance, which will be converted to electrical signal, causing the motor to vibrate. We are able to test using just one sensor and printing out the distance of the closest object repeatedly using the code written in `initial-1sensor-distance.ino`. This completes the initial ultrasonic sensor half of our circuit.

<img src= "https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/50758177/15cd5b4a-3950-4b60-be05-80288f37246a" width="600">

***Fig. 3:** The figure shows the use of the trigger and echo in an ultrasonic sensor. A pulse is sent out from the PWM pin, which is converted from a trigger into an acoustic burst that is sent out and returned and can vary depending on the distance of the nearest object. The gap between the outgoing and returning acoustic bursts is the PWM output from the echo pin, which can be converted into a distance. It is important to note that there is a needed delay between the pulses that are sent out for the sensor to work appropriately.*

The second circuit is the vibrational motor circuit. This circuit has more components. One end of the vibration motor (polarity can be disregarded) will get a direct power supply from the 3.3V pin of the Arduino, this will allow it to vibrate strongly. In parallel with the motor will be a diode that is reverse-biased. This serves to act as a surge protector for the Arduino as the motor produces voltage spikes as it rotates. Without the diode, the voltage surges could damage the Arduino. The capacitor, also in parallel with the motor, absorbs these voltage spikes. A transistor is placed in series with the motor, which provides it with current amplification as the Arduino provides a relatively weak power supply. Then, the motor is able to run more powerfully, allowing for more range of vibration depending on how close to an object the sensor is. Specifically, we used a N-channel MOSFET transistor that works with PWM in its saturated mode, which is when PWM enters its widest width (100% duty cycle), to drive the motor. A 1K ohm resistor is placed in series with the transistor so not too much current is being supplied to the motor. This end of the circuit is connected to the D3 pin of the Arduino, which is a channel that allows PWM. This digital pin will be set to output. Now, we have our motor circuitry completed In (Fig. 4), we can see the completed circuit with all three ultrasonic sensors:

<img width="537" alt="Screen Shot 2023-06-09 at 9 31 51 PM" src="https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/fb3b2b38-1a89-4254-992e-b4ee39c82c56">

***Fig. 4:** The figure shows the completed circuitry with both the ultrasonic sensors and vibrational motor circuit represented*

We are using PWM coupled with a low pass filter to create an analog output instead of digital to analog converter because Arduino doesn’t have a DAC. The low pass filter can be seen in (Fig. 5) where a resistor is placed in series with the capacitor. The low pass filter works to sequester harmonic frequencies that arise as the sound waves are traveling. The only signal we want to input into our motor is that of the carrier frequency, which is 40 kHz. The harmonic frequencies create a dominant force of uncertainty, which the low pass filter mitigates.

<img width="502" alt="Screen Shot 2023-06-09 at 9 02 41 PM" src="https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/42e9995a-8b3c-46e7-a365-4885de906e53">

***Fig. 5:** The figure shows the vibrational motor circuit and emphasizes the low pass filter used. Overall, the motor circuit consists of a resistor, transistor, diode, and capacitor connected in the following way above.*

To work in tandem with the motor circuit we can connect either a buzzer or a LED to the D6 pin to allow for an alternative method of testing our circuit, which is much easier to tell a difference than vibration for data collection. We started initially with a buzzer, which eventually we switched to a LED due to the squeaky noise the buzzer produced.

## Final Design

With all of our physical components completed, we can begin to consider how we are going to put it all together. We came up with two possibilities; we could either mount or sensor to a belt or to our chest. We ruled out using the belt as it would likely place the sensor too low to sense anything at around eye-level, while it also may be blocked by an oversized tee or longer jacket. Thus, this leaves us with mounting on our chest. An easy way to mount our sensor onto the user is by using velcro. To do this, we mounted it directly onto a hoodie, using the hoodie as the housing system for our device. We are able to velcro our sensors onto our hoodie and then able to directly attach our motor onto each of the sleeves of our hoodie. The rest of the arduino circuitry was soldered together and kept in the hoodie pouch. The vibrational motor wire is fed through the hoodie’s body and arm to its sleeve where the motor itself  will vibrate.This enables us to compact our entire device to be within the hoodie, while also keeping it relatively lightweight of a system, placing it in areas that are able to carry the weight easier. Alternatively, we could have mounted the motor to a glove or a bracelet, but both of those solutions would have added weight to our system. The final design can be seen in the figure below:

![Screen Shot 2023-06-09 at 9 02 55 PM](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/bde2dfa4-acc3-4ccb-ab74-ec626ece235e)

***Fig. 6:** The figure shows the final design of our circuits as we implement it into our hoodie.*


## Testing Apparatus
In order to precisely measure our device’s detection range we created a stable apparatus where our mount was placed onto a wall with velcro. We set up two vertical mounting rods that each had a horizontal rod attached, which allowed us to secure our test object at a specific y axis for the vertical limit. The depth of the measurement is varied along the third axis, the z axis. During each test, the rod is slowly moved from the outside of the sensor’s range and brought to a position that is detectable by the sensor at a given z value. Similarly, we were able to test for left and right boundaries by turning the test object vertically and slowly moving it along the x axis in front of the sensor. All of our measurements were made relative to the mount’s center surface along multiple distances.

![Mount test diagram](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/0c83c7e9-3a11-4f3c-9ab1-3cd55eb15200)

***Fig. 7:** The figure shows the mounting apparatus used to take all data for our project. It is important to note that we define (0,0) to be the center of the middle sensor for the mount. We move a thick meter stick ruler for the most effective test results.*

## Sensor Mounting
In order for the ultrasonic sensor circuit to work well, it must have a stable 3D printed PLA mount. Because our project is geared towards serving those with visibility impairments, it is of paramount importance that our design cover as much surface area in front of the user as possible. Therefore, the main design feature of our mount is the three angled faces each of about 15 degrees, meant to be occupied by three HC-SR04 sensors held strongly in place with four screws, which reduces the apparatus's vertical blindspots to a minimum. Another main feature of the mount is the hollow interior and an open strips on the top and middle face; we do not need one of the bottom face as it has direct access to the hoodie's pcoket. This provides us with the ability to feed the sensors wires through the mount and out the bottom. When attaching the mount to the hoodie, this makes it more convenient to connect the sensors to the microcontroller and thus, the vibration circuit, which will both be kept in the hoodie's pocket. The mount itself was made using a 3-D printer and a design program called Fusion 360. The mount design can be viewed in (Fig. 8):

<img width="781" alt="Screen Shot 2023-06-09 at 9 02 50 PM" src="https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/7b7860da-059c-44e8-ba1a-f6ad89d65f55">

***Fig. 8** The figure shows the mount that the ultrasonic sensors were placed on. The mounts faces are at angles of 15 degrees with respect to each other.*

Because of this new design, we had to edit our distance caluclation to include the tilt angle of the sensor. $$d=\frac{v_s t}{2\cos{\theta}}$$

This approach focuses on the horizontal distance that the nearest object is from our sensor, which equates to how close it is from hitting any part of our body. In essence, something 1 m away that's on the ground may actually be 0.5 m from tripping the user, rather than a wall 1 m away in front.

Our early designs included a flat faced mount with space for three sensors, but this design was omitted because there was too much overlap in the transmitter's wave emission and not enough dimension in measuring distance to an object. The design that we agreed upon increased the ability of the sensors to detect objects on the ground and near the user, as well as at waist, torso, and head heights.

As an aside, we know that the sensors lack measuring capabilities in front of the transducer. Because we want the vibrational motor to stop before the user hits an object, we are not concerned about this blindspot. Rather, it helps us in cutting off the vibrational motor, alerting the user that they are directly in front of an obstacle.

Initially, we had planned on attaching the sensors by sticking velcro to the back sides of them and the faces of the mount. This did not provide much stability as the velcro was not very strong and the sensors were not pointing outwards perpendicular to the face of the mount. Instead, we drilled the sensors into the mount with tiny screws. This provided a sturdy base as the sensors could not be shaken off the mount, and the emitted waves would be sent straight outward rather than at an offset angle.

## Adding Sensors

In attaching the sensors to the mount, they had to be prepped. We began by sodering off the ECHO, TRIG, GND, and VCC pins as they would not allow the sensors to lay flat on the mount's face as well as taking up unnecesary space in a small volume. In place of the pins, four long wires were sodered through the holes that the pins previously occupied.  

![IMG_4967 2](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/ff61ec7d-6461-4307-b591-d73b93058893)

***Fig. 9:** The figure shows the pins with long wires sodered through them.*

Each VCC, TRIG, and GND wire from the three sensors are then threaded through the mount and respectively soldered together and placed in the same parts of the arduino as before with 1 sensor.

![IMG_4966 2](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/132398869/fa819106-0cba-4990-ba96-5ca51765444e)

***Fig. 10:** The figure shows the various wires connecting all VCC, TRIG, and GND wires. All ECHO wires are free from one another.*

Each of the ECHO wires are then connected to independent digital I/O ports, the bottom is plugged into 5, the middle into 9, and the top into 10. By plugging in the three triggers into the same port to be triggered together, that allows the sensors to each send out a wave simultaneously, even though we only loop through one echo at a time. This process can be seen through the code in `initial-3sensor-1buzzer1motor.ino`, which works with the 3 sensors in tandem. It is important to note the delays within the code. If the delay is removed, the sensors take data too fast and will begin outputting strange values that are not representative of what is in front.

The electrical signals that will be controlling the vibrational motor will be receiving its input from data from the ultrasonic sensor


## Initial Tests
With our full circuit setup, we conduct our first initial test with the code writen in `initial-1sensor-1buzzer1motor.ino`. For this, we first begin tweaking the function we use to vibrate the motor. We use a piecewise function where under some given distance, $d_{min}$, the motor output is constant. Thus, we allow $f(x)=V_{max}$ for $x\lt d_{min}$. Now for larger $x$ values, we use an exponential decay function of the form $f(x)=V_{max}e^{-(x-d_{min})/c}$. For the Arduino, the full power of the system would have $V_{max} = 255$. We start off with $d_{min}=30$ and the constant $c$ determines how fast the power function decays. 

![Voltage Output and Reported Distance vs  Physical Distance](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/e4584dad-eb24-43ed-bfc7-dd7bfd240381)

***Fig. 11:** The plot is shown gives us a distance vs. distance plot for the sensor's reported value and the physical distance on the left axis. Wee can then convert that into a voltage based on our piecewise function, which is shown on the right axis. We set our minimum distance for the voltage maximum to be set within 30cm, with the farther distances following an exponential decay.*

We start with a test that is important for understanding how our sensors work, that is data for the physical distance against the sensor reported distance. To do this, we move our thick meter stick forwards and backwards across 5cm intervals, taking an average of the reported values from the Serial Monitor. This process yields a plot as shown in (Fig. 11) with the left axis. From it, we see that it follows the expected value at low distances, but begins to deviate somewhat significantly towards the ends. However, at far distances, this deviation is caused by the naturally higher variability in the distance calculation the farther the ultrasonic waves have to travel. At farther distances, the effects of a slight shift in the calculation are much more minimal compared to at closer distances.

We do the same test, but wire the LED/buzzer circuitry to an oscilloscope to see how the physical distances are converted to a PWM percentage. From our code, we have our expected function that converts the distances exponentially. We see that in (Fig. 11) on the right axis that our data aligns with the expected output well, so the motor and LED circuit are working as we expect it to at any given distance.

Next, based off of our testing apparatus, we create a setup to sweep a squared thick meter stick both up and down and side to side while looking for a jump in the distance reported to locate the outer boundaries of the sensor in both the directly up and down direction and side to side direction. We will do this process for a set of distances: 20cm, 40cm, 57cm, and 77cm. We added tape to our setup to ensure reproducibility of our data.  Since we are given the supposed working range of the sensors, we can compare our results to the datasheet. With each of the distances we use, we can create a plot to visualize the working range in both directions.

![Vertical working range of a single sensor](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/8d5049d7-55f8-4fb3-9596-33d78233ad06)

***Fig. 12:** The plot is shown for the working range of a single sensor in the up and down direction. The red points show the raw data and a linear regression is applied to both sides to estimate the working range up and down.*

As we see in (Fig. 12), there is a clear outward fanning shape for the vertical working range. This makes sense due to the shape of the sensors likely blocking some nearby waves while being able to accept a larger range from farther away. This works well for our project as we are focused on detecting objects farther away in order to alert the user of an incoming obstacle rather than detecting it too late. However, this makes it harder to compare our results to the values in the datasheet. We can calculate our working range in two ways. The first, we can use a linearization from the plot to map the working range. This yields an approximate value of 18 degrees. We alternatively calculate it using the end points of our plot as we are more focused on the working range farther away from our sensor. This yields an approximate value of 25 degrees. The datasheet provides that the working range should be 30 degrees, or 15 degrees in each direction. Thus, our calculation at a farther distance matches closer to the expected datasheet value, as there is some fall off in performance of the sensor from close distances. Additionally, it is important to note that there is a slightly uneven effectual range on the two sides of the sensor; it is able to detect more above the sensor than below.

![Horizontal working range of a single sensor](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/a04f1936-6101-4937-bc0d-e1b7747c5272)

***Fig. 13:** The plot is shown for the working range of a single sensor in the left and right direction. The red points show the raw data and a linear regression is applied to both sides to estimate the working range left and right.*

We do a similar plot for the horizontal working range shown in (Fig. 13), as we see a similar outward fanning shape, likely for the same reason as stated earlier. Again, we calulate the working range with the two methods. This first method yields a value of 14 degrees and the second method yields a value of 13 degrees. The working angle in this direction appears to be much smaller than the expected datasheet value and compared to the other direction. Looking at how we took our data, this may be atttributed to the orientation of the rod. Since we lay the rod vertically in front of the sensor, some of the waves may hit the rod but get reflected in a way that that does not allow for it to return to the sensor. Thus, if the rod were slightly turned, the distance it could be tracked may increase. It is likely because of this that the datasheet reports the effectual angle to be less than 15 degrees in every direction. This assumes that if the object is placed in the ideal orientation, it can be detected at an angle of up to 15 degrees, otherwise it is likely less.


## Mount Tests

To start off, we want to test how our mount actually works at comparing each of the sensors individually with the working range of the entire sensor. To do this, we can run our `initial-1sensor-distance.ino` code for each of the sensors, running the same initial test we did on 1 sensor, to map each of the sensors working ranges. We can make a plot of all of the independent ranges together, shown in (Fig. 14) and (Fig. 15).

![Vertical working range of each sensor overlapped](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/46969ad3-1f68-4dbe-9265-9af15ddce9ef)

***Fig. 14:** The figure shows the three sensors measured individually in the up and down direction relative to the middle of the respective sensor. The upper points are the maximum height and the bottom points are the minimum heights.*

![Horizontal working range of each sensor](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/3e85dfc8-3bc4-49d3-b969-8be106baa3de)

***Fig. 15:** The figure shows the three sensors measured individually in the left and right direction. The upper points are the maximum leftwards from the sensor and the bottom points are the maximum rightwards from the sensor.*

We notice that in the vertical direction in (Fig. 14), the sensors that tilt downwards have a slightly smaller working range, which may be due to the fact of the bouncing angle of the waves on a flat rod. Meanwhile, in the horizontal direction in (Fig. 15), there is the similar struggle of side to side wave deflection that the three working ranges mostly overlap. To better visualize the compounding of the three sensors, we can plot them relative to each other rather than relative to the appropriate sensor. When we test all three of our sensors together, we mark the middle to be the middle sensor, so we can set that to be the relative 0 for our plots in the vertical direction.

![Vertical working range of each sensor overlapped](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/3855ef92-e8de-47d8-881f-668da865c3a3)

***Fig. 16:** The figure shows the three sensors measured individually in the up and down direction, each relative to the (0,0) set at the middle sensor. The upper points are the maximum height and the bottom points are the minimum heights.*

From (Fig. 16), we note that there is significant overlap between the sensors at a distance outside of 20cm. Because of this, we likely do not need to worry too much about physical blind spots, focusing more on the problem of waves being reflected away. The bottom sensor appears to add a minimal working range, likely due to the angles making it harder for it to allow for waves to reflect back for it to detect.

After testing each sensor individually, which was representative of a control group, we took measurements of all three sensors working together. We start off by doing the same test we did for the single sensor with the three sensor system, moving the rod side to side and up and down. Since this is our final mount, we measure at more data points to get a better picture of the shape of the working range. We once again can shade in the estimated working range of each, using a linear regression fit, to see that the working range of our three sensor system is greater in both the horizontal and vertical directions and left and right directions. This is seen in (Fig. 17) and (Fig. 18):

![whole device vs single sensor vertical sensing ranges](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/72c3de93-5d4d-4c72-93b7-dcb066098688)

***Fig. 17:** The figure shows the three sensors measured together in the up and down direction relative to the middle of the respective sensor. We then compare this to the single sensor data. We can once again sweep out an estimated working range for each of the sets of data.*

![whole device vs single sensor horizontal sensing ranges](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/4b814715-6b13-4123-bd22-81981e633a80)

***Fig. 18:** The figure shows the three sensors measured together in the left and right direction relative to the middle of the respective sensor. We then compare this to the single sensor data. We can once again sweep out an estimated working range for each of the sets of data.*

From our previous tests, we notice that the orientation of the rod is very important. If the rod is angled in the right direction, it'll more likely reflect waves to hit the sensor. Thus, we can do the same side to side, up and down test, while being able to rotate the rod at a given location. This gives us the maximum working range with tilt, meaning any object within the working range with tilt has a possibility to be measured by the sensor. We can see from (Fig. 19) and (Fig. 20), the working ranges are much larger in both the horizontal and vertical directions. The tilt test helps clearly represent the increased working range for the vertical direction, greatly expanding our working range downwards, representing the mount that we use that has sensors angled downwards.

![Vertical working range tilted vs not tilted](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/c004fd6a-34aa-464d-b496-209f28369160)

***Fig. 19:** The figure shows the three sensors measured together in the up and down direction while tilting and without tilting the rod. We can once again sweep out an estimated working range for each of the sets of data.*

![Horizontal working range tilted vs not tilted](https://github.com/stephsplash30/Vibrating-Ultrasonic-Glove/assets/110078529/e0012b2e-cb1b-4e8c-971e-23e8209097f1)

***Fig. 20:** The figure shows the three sensors measured together in the left and right direction while tilting and without tilting the rod. We can once again sweep out an estimated working range for each of the sets of data.*


## Hoodie Tests

Once we have our final design set up, we have to make some final tests with our hoodie in order to confirm that it works as expected for a user. For this, we implemented `final-3sensor-1motor.ino` as the onboard code that is run independent of plugging into a computer. Thus, at this stage we could test the hoodie on complete battery power. Here, we take a more qualitative approach and see if there are any bugs or issues with our setup. For this, the main issues we would need to test here, is tuning the parameters of our vibration power to best help the user stop before reaching an obstacle. Additionally, we need to test the effectiveness of the sensor being unobstructed by the human body and the feeling of the motor attached to the hoodie. 

In qualitative tests of our final design, we found that it did not always detect objects below waist level, such as bushes. When the waves hit a leaf that was tilted in a particular way, it was sometimes detectable. In addition, in order to precisely understand the boundaries the user is walking in, they must walk slower than a normal pace. Overall, our device works in the range that we want, but one has to move slowly in order to make the most use of the vibrational motor’s gradient. We notice that with practice, the user is able to quickly begin acclimating to our system, feeling differences in vibrations better, which may be difficult to differentiate initially.

## Conclusion

Overall, our hoodie works well to solve the problem we set out to conquer. However, in the future, we can test using different ultrasonic sensors, since we are limited by the ability of the sensors working range and the impact of the orientation of the object. From this, we would want to test out using an ultrasonic sensor with one transmitter and receiver channel combined. We would also want to use alternative ways of sensing such as infared or depth sensing cameras. We would also want to continue to integrate into our hoodie, to make the wiring and system more compact. For the vibration output circuit, we want to test integration into a bracelet or glove to provide the user with more feedback, or alternatively, using audio output in ears. Our project lays down the framework to one day replace the use of white canes, making it a more accessible mobility aid to those with low to no vision.


