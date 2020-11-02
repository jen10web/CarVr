import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
from pyPS4Controller.controller import Controller



class MyController(Controller):
    #set up PS4 controller
    
    #connect the ESC for each motor to gpio pins
    rESC = 4  #Connect the ESC in this GPIO pin
    lESC = 4

    #get the raspberry pi and initialize duty cycle to 0
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(rESC, 0)
    pi.set_servo_pulsewidth(lESC, 0)
    
    #set up some speed constants
    max_controller_val = 32767
    min_controller_val = 0 #Is this 0 or negatie?
    controller_step = max_controller_val / 3 # Three speeds
    
    
    def Controllmotor(self, direc, value):
        if direc == "release":  #if release stop
            MyController.pi.set_servo_pulsewidth(MyController.lESC, 0)
        elif direc == "up":
            if value >= (MyController.controller_step * 2) + 1: # Max throttle if in third half
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 2000) 
            elif (value >= MyController.controller_step + 1 and value < MyController.controller_step * 2): # Slightly open throttle in middle
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 1100) 
            else:
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 1000) # Min throttle otherwise


    def Controlrmotor(self, direc, value):
        if direc == "release":  #if release stop
            MyController.pi.set_servo_pulsewidth(MyController.lESC, 0)
        elif direc == "up":
            if value >= (MyController.controller_step * 2) + 1: # Max throttle if in third half
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 2000) 
            elif (value >= MyController.controller_step + 1 and value < MyController.controller_step * 2): # Slightly open throttle in middle
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 1100) 
            else:
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 1000) # Min throttle otherwise
       
       
        #controller input events
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
                
    def on_L3_up(self, value):
        self.Controllmotor("up", -1 * value)
                
    def on_L3_down(self, value):
        self.Controllmotor("down", value)

    def on_L3_release(self, value):
        self.Controllmotor("release", value)

    def on_R3_up(self, value):
        self.Controlrmotor("up", -1 * value)
              
    def on_R3_down(self, value):
        self.Controlrmotor("down", value)

    def on_R3_release(self, value):
        self.Controlrmotor("release",  value)
 
 
 
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

  
