import utime
from machine import Pin, SPI, I2C
from LS027B4DH01 import LS027B4DH01
from joystick import Joystick
from home import Home
from record import Record
from settings import Settings
from mpu9250 import MPU9250

class CycleComputer():
    def __init__(self):
        self.lcd = LS027B4DH01(
            SPI(
                2, baudrate=2_000_000, polarity=0, phase=0, bits=8, 
                firstbit=SPI.LSB, sck=Pin(18), 
                mosi=Pin(23), miso=Pin(19)
            ),
            Pin(32, Pin.OUT), Pin(33, Pin.OUT), Pin(25, Pin.OUT)
        )

        self.button = Joystick( Pin(34), Pin(35), Pin(26, Pin.IN) )

        self.mpu9250 = MPU9250( I2C(scl=Pin(21), sda=Pin(22), freq=100000) )
        self.mpu9250.setting(self.mpu9250.GFS_1000, self.mpu9250.AFS_16G)

        self.states = {
            'home':Home(self), 
            'record':Record(self), 
            'settings':Settings(self)
        }

        self.state = 'home'

    def run(self):
        obj = self.states[self.state]
        obj.control( self.button.read() )
        obj.draw()

def main():

    cycle_computer = CycleComputer()
    
    utime.sleep(1)

    while True:
        cycle_computer.run()

if __name__ == "__main__":
    main()
