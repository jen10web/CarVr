from pyPS4Controller.controller import Controller


class MyController(Controller):
    
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def on_L3_up(self, value):
        print("on_L3_up", value)
        
    def on_L3_down(self, value):
        print("on_L3_down", value)

    def on_L3_release(self, value):
        print("on_L3_release")

    def on_R3_up(self, value):
        print("on_R3_up", value)
        
    def on_R3_down(self, value):
        print("on_R3_down", value)

    def on_R3_release(self, value):
        print("on_R3_release")
        
        
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()