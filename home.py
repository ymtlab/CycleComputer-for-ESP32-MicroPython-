from ui import UI

class Home():
    def __init__(self, parent):
        self.parent = parent
        self.ui = UI(self.parent.lcd)
        self.ui.add_text('title', 10, 10, 'Home')
        
        self.ui.add_text('date', 20, 50, '2020/8/22')
        self.ui.add_text('ax', 20, 50+40, '999')
        self.ui.add_text('ay', 20, 50+80, '999')
        self.ui.add_text('az', 20, 50+120, '999')

    def control(self, button):
        if button['left']:
            self.parent.state = 'settings'

        if button['right']:
            self.parent.state = 'record'
        
        self.mpu9250()

    def draw(self):
        self.ui.draw()

    def mpu9250(self):
        accel = self.parent.mpu9250.read_accel()
        #gyro = self.parent.mpu9250.read_gyro()
        #mag = self.parent.mpu9250.read_magnet()

        self.ui.texts['ax'].set_text( str(accel['x']) )
        self.ui.texts['ay'].set_text( str(accel['y']) )
        self.ui.texts['az'].set_text( str(accel['z']) )
