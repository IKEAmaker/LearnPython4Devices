# Learn to Code Python For a Device
Hej!

We have put together a few kits of a tiny microcontroller, a small LED matrix and a joystick.
There is also a [step by step guide on how to get started with coding](https://github.com/IKEAmaker/LearnPython4Devices/raw/master/Docs/LearnToCode-CompleteGuide.pdf) with this kit.
The target audience for this kit is 100% analog humans with zero coding experience.
We hope this is a fun way to get into digital creativity.

If you want to get an idea how this kit can be used to teach coding,
you can check [this 6 minute video.](https://youtu.be/odnBymFynmI)

One of the projects in the guide includes a scrolling text display:

![The Kit](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/Scroll.gif)

# Build This kit
If you can come to Maker Friday at the Co-Create lab and we'll help you out.

| How to build |               | 
| ------------- |:-------------:|
|This is what the kit looks like when it is built|  ![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/WholeKit.JPG)|
| The first step is to collect all the parts |![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/WiringUp_1.jpg)|
| The next step is to solder the rows of pins and the LED matrix to the PCBs. There are a few videos showing how it's done: [1 Solder the microcontroller to it's rows of pins (and some general soldering tips)](https://www.youtube.com/watch?v=GbWMCBHOKaM). [2 Solder the LED matrix to it's own PCB](https://www.youtube.com/watch?v=Tg6XQbmof4U). [3 Solder a row of pins to the LED matrix PCB](https://www.youtube.com/watch?v=a5eWrJ8vEno)  |[![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/Solder.png)](https://www.youtube.com/watch?v=GbWMCBHOKaM)|
| When all the soldering is done, we insert the components into the breadboard and then its time to wire things up. The image to the right is a schematic showing how to connect the different signals.|![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/TinkerKit_v1_bb.png)|
| The first wires to connect are the power wires to both the LED matrix and the Joystick. The red wire connects "3V" pin on the microcontroller with "+" pin on the LED matrix and "+5V" pin on the joystick. The black wire connects "Gnd" pin on the microcontroller with "-" pin on the LED matrix and "GND" pin on the joystick.  |![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/WiringUp_2.jpg)|
| Next we connect the "C" pin on the LED matrix to pin "2" on the microcontroller. And the "D" pin on the LED matrix is connected to "0" pin on the microcontroller.  |![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/WiringUp_3.jpg)|
| Lastly we connect three signals between the microcontroller and the joystick. The "VRx" pin on the joystick should be connected to the "4" pin on the microcontroller, The "VRy" pin on the joystick should be connected to the "3" pin on the microcontroller and lastly, the "SW" pin on the joystick should be connected to the "~1" pin on the microcontroller.  |![Soldering](https://raw.githubusercontent.com/IKEAmaker/LearnPython4Devices/master/Media/WiringUp_4.jpg)|
