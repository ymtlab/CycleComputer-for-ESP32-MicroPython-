from ui import UI

class Settings():
    def __init__(self, parent):
        self.parent = parent
        self.ui = UI(self.parent.lcd)
        self.ui.add_text('title', 10, 10, 'Settings')
        self.ui.add_button('button1', 20, 50, 'Bluetooth')
        self.ui.add_button('button2', 20, 90, 'Tire size')
        self.ui.add_button('button3', 20, 130, 'Time')

        self.ui.buttons['button1'].selected = True

    def control(self, button):
        if button['left']:
            self.parent.state = 'record'

        if button['right']:
            self.parent.state = 'home'

        if button['up']:
            self.button_select(1)

        if button['down']:
            self.button_select(-1)

    def draw(self):
        self.ui.draw()

    def button_select(self, direction):
        keys = list( self.ui.buttons.keys() )

        for n, key in enumerate(keys):
            if self.ui.buttons[key].selected:
                self.ui.buttons[key].selected = False
                break
        
        if direction > 0:
            if n == len(keys):
                self.ui.buttons[ keys[0] ].selected = True
                return

        if direction < 0:
            if n == 0:
                self.ui.buttons[ keys[-1] ].selected = True
                return

        self.ui.buttons[ keys[n + direction] ].selected = True
        return
