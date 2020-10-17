import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system("sudo killall pigpiod")
os.system ("sudo pigpiod") #Launching GPIO library
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
    max_esc_val = 2500 #vesc max val
    min_esc_val = 500  #vesc min val
    esc_step = (max_esc_val - min_esc_val) / 20 # there will be 20 speeds
    max_controller_val = 32767
    min_controller_val = 0
    # there will be 4 speeds plus a dead zone
    controller_step = max_controller_val / 20
    
    
    def Controllmotor(self, direc, value):
        if direc == "release":                 #if release stop
            MyController.pi.set_servo_pulsewidth(MyController.lESC, 0)
        elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 0) #if within deadzone
            elif value <= (MyController.controller_step * 5):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 500) #fifth speed
            elif value <= (MyController.controller_step * 6):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 510) #sixth speed
            elif value <= (MyController.controller_step * 7):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 530) #seventh speed
            elif value <= (MyController.controller_step * 8):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 550) #eighth speed
            elif value <= (MyController.controller_step * 9):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 600) #ninth speed
            elif value <= (MyController.controller_step * 10):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 780) #tenth speed
            elif value <= (MyController.controller_step * 11):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 900) #eleventh speed
            elif value <= (MyController.controller_step * 12):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, 1100) #twelfth speed
            elif value <= (MyController.controller_step * 13):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 13) #thortheen speed
            elif value <= (MyController.controller_step * 14):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 14) #fourtrhne speed
            elif value <= (MyController.controller_step * 15):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 15) #fifteen speed
            elif value <= (MyController.controller_step * 16):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 16) #sixteen speed
            elif value <= (MyController.controller_step * 17):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 17) #seventeen speed
            elif value <= (MyController.controller_step * 18):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 18) #eigthen speed
            elif value <= (MyController.controller_step * 19):
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 19) #ninteen speed
            else:
                MyController.pi.set_servo_pulsewidth(MyController.lESC, MyController.esc_step * 20) #twemty / fastet speed 


    def Controlrmotor(self, direc, value):
        if direc == "release":                 #if release stop
            MyController.pi.set_servo_pulsewidth(MyController.rESC, 0)
        elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi.set_servo_pulsewidth(MyController.rESC, 0) #if within deadzone
            elif value <= (MyController.controller_step * 2):
                MyController.pi.set_servo_pulsewidth(MyController.rESC, MyController.esc_step) #first speed
            elif value <= (MyController.controller_step * 3):
                MyController.pi.set_servo_pulsewidth(MyController.rESC, (MyController.esc_step * 2)) #second speed
            elif value <= (MyController.controller_step * 4):
                MyController.pi.set_servo_pulsewidth(MyController.rESC, (MyController.esc_step * 3)) #third speed  
            else:
                MyController.pi.set_servo_pulsewidth(MyController.rESC, (MyController.esc_step * 4)) #fourth/fastet speed
       
       
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

  
