class UI():
    def __init__(self, lcd):
        self.lcd = lcd
        self.buttons = {}
        self.texts = {}

    def add_button(self, name, x, y, text):
        self.buttons[name] = Button(self, x, y, text)

    def add_text(self, name, x, y, text):
        self.texts[name] = Text(self, x, y, text)

    def draw(self):
        self.lcd.data_reset()

        for text in self.texts:
            self.texts[text].draw()
        
        for button in self.buttons:
            self.buttons[button].draw()
        
        self.lcd.data_update_all_line()

    def reset(self):
        self.lcd.data_reset()

class Button():
    def __init__(self, parent, x, y, text):
        self.parent = parent
        self.x = x
        self.y = y
        self.text = text
        self.value = 0
        self.selected = False

    def draw(self):
        self.parent.lcd.string(self.x+10, self.y, self.text)
        if self.selected:
            self.parent.lcd.rect(
                self.x, 
                self.y, 
                self.x + len(self.text) * 16 + 10, 
                self.y + 30
            )

    def set_text(self, text):
        self.text = text

    def set_value(self, value):
        self.value = value

class Text():
    def __init__(self, parent, x, y, text):
        self.parent = parent
        self.x = x
        self.y = y
        self.text = text

    def draw(self):
        self.parent.lcd.string(self.x, self.y, self.text)

    def set_text(self, text):
        self.text = text
