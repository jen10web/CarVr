import RPi.GPIO as GPIO #importing library for gpio control
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
#os.system("sudo killall pigpiod")
#os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
#import pigpio #importing GPIO library
from pyPS4Controller.controller import Controller




class MyController(Controller):
    
    #connect the ESC for each motor to gpio pins
    rESC = 11  #Actual pin number
    lESC = 13
    
    #set up gpio
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lESC, GPIO.OUT)
    GPIO.setup(rESC, GPIO.OUT)
    pi_pwml = GPIO.PWM(lESC, 1000)
    pi_pwmr = GPIO.PWM(rESC, 1000)
    pi_pwml.start(0)
    pi_pwmr.start(0)
    
    #set up some speed constants
    max_esc_val = 100 #vesc max val
    min_esc_val = 0  #vesc min val
    esc_step = (max_esc_val - min_esc_val) / 10
    max_controller_val = 32767
    min_controller_val = 0
    controller_step = max_controller_val / 10
    
    
    def Controllmotor(self, direc, value):
        if direc == "release":                 #if release stop
            MyController.pi_pwml.ChangeDutyCycle(0)
        elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step)
            elif value <= (MyController.controller_step*2):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*2)
            elif value <= (MyController.controller_step*3):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*3)
            elif value <= (MyController.controller_step*4):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*4)
            elif value <= (MyController.controller_step*5):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*5)
            elif value <= (MyController.controller_step*6):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*6)
            elif value <= (MyController.controller_step*7):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*7)
            elif value <= (MyController.controller_step*8):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*8)
            elif value <= (MyController.controller_step*9):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*9)
            elif value <= (MyController.controller_step*10):
                MyController.pi_pwml.ChangeDutyCycle(MyController.esc_step*10)
                
    def Controlrmotor(self, direc, value):
       if direc == "release":                 #if release stop
            MyController.pi_pwmr.ChangeDutyCycle(0)
       elif direc == "up":
            if value <= MyController.controller_step:
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step)
            elif value <= (MyController.controller_step*2):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*2)
            elif value <= (MyController.controller_step*3):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*3)
            elif value <= (MyController.controller_step*4):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*4)
            elif value <= (MyController.controller_step*5):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*5)
            elif value <= (MyController.controller_step*6):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*6)
            elif value <= (MyController.controller_step*7):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*7)
            elif value <= (MyController.controller_step*8):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*8)
            elif value <= (MyController.controller_step*9):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*9)
            elif value <= (MyController.controller_step*10):
                MyController.pi_pwmr.ChangeDutyCycle(MyController.esc_step*10)
       
       
        #controller input events
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
                
    def on_L3_up(self, value):
        self.Controllmotor("up", -1 * value)
                
    def on_L3_down(self, value):
        self.Controllmotor("down", value)

    def on_L3_y_at_rest(self):
        self.Controllmotor("release", 0)

    def on_R3_up(self, value):
        self.Controlrmotor("up", -1 * value)
              
    def on_R3_down(self, value):
        self.Controlrmotor("down", value)

    def on_R3_y_at_rest(self):
        self.Controlrmotor("release",  0)
 
 
 
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()

  
