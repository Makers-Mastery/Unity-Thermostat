# Unity-Thermostat
## Wireless Unity VR Thermostat Translated to Physical Tempurature Changes Via a Custom Raspberry Pi Thermostat and HTTP Server

Created by Elijah Hansen, in collaboration with Professor Jianli Chen, the University of Utah College of Engineering, and Professor Yangming Shi of the University of Alabama. 
<br>
Special thanks to Miguel Oyarzun for helping set up the Raspberry Pi and debugging the python script.
<br>
In collaboration with Professor Jianli Chen and the University of Utah College of Engineering, I was able to successfully create a Unity
environment incorporating both SteamVR integration, including snapturning and teleportation, and a VR thermostat which communicated with a Raspberry Pi
over a HTTP connection. The Raspberry Pi ran a python script which created an HTTP server to handle put requests from the client, Unity, resulting in the
active wireless updating of a virtualTemp value and upon receiving a request or every 15 seconds, use a connected digital temperature module to read the
room temp and either increase or decrease a stepper motor connected to a space heater in my to increase or decrease the physical temperature in real
life. In short, I created a VR thermostat and connected it a real thermostat of my design using a Raspberry Pi to turn virtual input into real world
temperature changes.
<br>
The project was very challenging at first as I encountered MANY roadblocks on my way to getting the environment to a usable state. I originally
found out my gaming laptop I was planning on using to run the HTC Vive off of was fundementally incompatible with VR. I ended up solving this by
borrowing a GTX 2080 graphics card from Professor Chen and sticking it in an old Dell workstation and upgrading the power supply. Once I was able to get
the VR setup, it turns out movement within the VR environment I was creating the thermostat in didn’t have any kind of movement implemented, so I had to
do that myself. I was provided with a tutorial on implementing movement in the VR environment, which after a long time, lots of coding and trial and
error, turned out to not work at all. I ended up just scrapping all my progress and installing a clean version of the environment to try and implement
the SteamVR Unity plug-in as opposed to try to write my own. I got everything working in under 10 minutes. Finally I was able to move onto the more
complex parts of the project. With the help of my friend Miguel Oyarzun, we set up the Raspberry Pi with Raspbian and installed all the dependencies we’d
need to make it run an HTTP server. I purchased an HTTP client plug-in from the Unity store which allowed me to very easily send and receive HTTP
requests through Unity scripting. I need to get the IP address of the Raspberry Pi to send packets to it, and after being unable to access the admin page
on my router to retrieve that number, I ended up circumventing the issue by creating a mobile hotspot on my computer and connecting the Raspberry Pi to
that. Eventually, I was able to get two unity buttons (representing tempUp and tempDown) to send unhandled HTTP requests to the Raspberry Pi. Everything
was working on the Unity side, so all that was left to do was write a python script to handle PUT requests. After mixing and matching Youtube tutorials
and lots of google, I was able to get the server to a point where it was able to handle put requests and update and send back console information. All
that was left to do was the motor module. My background is in electrical engineering, so in under 15 minutes I had the temperature sensor and stepper
motor wired perfectly to the Raspberry Pi and set to writing code for it. I structured the code to run a moveMotor() function, which takes the
temperature and adjusts the stepper motor accordingly by comparing virtualTemp to realTemp, every time it handles a PUT request and every 15 seconds.
With some debugging, that concluded the project as I’d accomplished the full scope of the assignment.
<br>
The source code, unity environment, and python script can all be found on box and on my github 
@ https://github.com/The-EAR-Foundation/Unity-Thermostat (my github name may change to “Makers-Mastery” in the near future so look out for that). The
“events.cs” script, found under the assets folder, is the script that control the sending of HTTP requests as well as updating the virtualTemp display
within unity. “unity server.py” is the python script that handles put requests and updates the room temp via a stepper motor. The nice part about HTTP
requests is this server can be written in basically any language, if python doesn't work for any reason, and it’ll handle PUT requests the same with no
changes to Unity. Video demonstrations of the project, source code, and wiring diagrams can all be found on my github. 

