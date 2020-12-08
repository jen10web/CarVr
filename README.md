# CARVR - A Virtual Reality Experiment with a Remote Vehicle

## Virtual reality is becoming more applicable to fields beyond gaming. To test the proficinecy of it as an addition to control systems, our 2020 Senior project team set out to link it to a remote rover:


![alt text](https://github.com/jen10web/CarVr/blob/master/628123290.jpg) [alt text](https://github.com/jen10web/CarVr/blob/master/IMG952845.jpg)


[Demo Video](https://www.youtube.com/watch?v=XLQnoL_HQWo&feature=youtu.be)

### Technologies Used:
Scripting Languages: Unity 2019.4.11.f1, Python 3 or higher. 
Hardware: Oculus Quest/Oculus Rift, wireless controllers, a laptop.
  Raspberry Pi 4: Running Raspberrian. Pi Camera. 
  Misc: 


#### Installation: 
Download all scripts from the GitHub project page. Install the reccomended software, as well as any software requirements for your Virtual Reality Device. Setup the Pi 4 with Raspberrian. Download and update all required libraries for the accompanying python scripts. Setup the picamera interface and accompying Bluetooth modules. 


#### Setup: 
Open the Unity project VR Cockpit, on a desktop connected to the Virtual Reality Headset. Download and run the CarVr.sh script on the Rasbperry Pi. This is assuming the setup for your vehicle is complete, and the camera and necessary driving components are in place. 


#### How To Operate: 
Drive with left and right analog sticks, on controls the left wheel, the other the right wheel. You should see an updating feed in the virtual reality headset.

##### Special Gotchas:
  Be careful of steel vehicle chassis with brushless motors. Virtual Reality streams follow http streaming protocols. Debug everything seperately before tyring to integrate components. 
