from machine import ADC

class Joystick():
    def __init__(self, x, y, s=None):
        self.x_pin = ADC(x)
        self.y_pin = ADC(y)
        self.switch_pin = s

        self.x_pin.atten(ADC.ATTN_11DB)
        self.y_pin.atten(ADC.ATTN_11DB)
        self.threshold = 1000
        self.center = 2048
        self.x_data = [0, 0]
        self.y_data = [0, 0]
        self.__dict__ = {
            'up'    : False,
            'down'  : False,
            'left'  : False,
            'right' : False,
            'switch': False
        }

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def read(self):
        self.x_data[0] = self.x_data[1]
        self.y_data[0] = self.y_data[1]
        self.x_data[1] = self.x_pin.read() - self.center
        self.y_data[1] = self.y_pin.read() - self.center

        self.__dict__['up']     = self.up()
        self.__dict__['down']   = self.down()
        self.__dict__['left']   = self.left()
        self.__dict__['right']  = self.right()
        self.__dict__['switch'] = self.switch()

        return self

    def up(self):
        return ( self.x_data[1] > self.threshold ) \
            and ( self.x_data[0] < self.threshold )

    def down(self):
        return ( self.x_data[1] < (-1 * self.threshold) ) \
            and ( self.x_data[0] > (-1 * self.threshold) )
    
    def right(self):
        return ( self.y_data[1] > self.threshold ) \
            and ( self.y_data[0] < self.threshold )

    def left(self):
        return ( self.y_data[1] < (-1 * self.threshold) ) \
            and ( self.y_data[0] > (-1 * self.threshold) )

    def switch(self):
        return bool(self.switch_pin.value)
