import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
from pyPS4Controller.controller import Controller



class MyController(Controller):
    #set up PS4 controller
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
    
    #connect the ESC for each motor to gpio pins
    rESC = 4  #Connect the ESC in this GPIO pin 
    lESC = 2

    #get the raspberry pi and initialize duty cycle to 0
    pi = pigpio.pi();
    pi.set_servo_pulsewidth(rESC, 0) 
    pi.set_servo_pulsewidth(lESC, 0) 
    

    #set up some speed constants
    max_esc_value = 99 #vesc max val
    min_esc_value = 0  #vesc min val
    esc_step = max_esc_value / 4 # there will be 4 speeds
    max_controller_val = 32767
    min_controller_val = 0
        # there will be 4 speeds plus a dead zone
    controller_step = max_controller_val / 5 


    #controller input events
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def on_L3_up(self, value):
        Controllmotor("up", value)
        
    def on_L3_down(self, value):
        Controllmotor("down", value)

    def on_L3_release(self, value):
        Controllmotor("release", value)

    def on_R3_up(self, value):
        Controlrmotor("up", value)
        
    def on_R3_down(self, value):
        Controlrmotor("down", value)

    def on_R3_release(self, value):
        Controlrmoto("release",  value)



    def Controllmotor(direc, value):
        if direc == "release":                 #if release stop
            pi.set_servo_pulsewidth(lESC, 0)
        elif direc == "up":
            if: value <= controller_step
                pi.set_servo_pulsewidth(lESC, 0) #if within deadzone
            elif: value <= (controller_step * 2)
                pi.set_servo_pulsewidth(lESC, esc_step) #first speed
            elif: value <= (controller_step * 3)
                pi.set_servo_pulsewidth(lESC, (esc_step * 2)) #second speed
            elif: value <= (controller_step * 4)
                pi.set_servo_pulsewidth(lESC, (esc_step * 3)) #third speed  
            else:
                pi.set_servo_pulsewidth(lESC, (esc_step * max_esc_val)) #fourth/fastet speed 
        else: #direction is down
            #TO DO




    def Controlrmotor(direc, value):
        if direc == "release":                 #if release stop
            pi.set_servo_pulsewidth(rESC, 0)
        elif: direc == "up"
            if: value <= controller_step
                pi.set_servo_pulsewidth(rESC, 0) #if within deadzone
            elif: value <= (controller_step * 2)
                pi.set_servo_pulsewidth(rESC, esc_step) #first speed
            elif: value <= (controller_step * 3)
                pi.set_servo_pulsewidth(rESC, (esc_step * 2)) #second speed
            elif: value <= (controller_step * 4)
                pi.set_servo_pulsewidth(rESC, (esc_step * 3)) #third speed  
            else:
                pi.set_servo_pulsewidth(rESC, (esc_step * max_esc_val)) #fourth/fastet speed 
        else: #direction is down
            #TO DO

