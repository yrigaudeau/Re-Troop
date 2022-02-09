class FakeKeypress:
    def __init__(self, keysym, char):
        self.keysym = keysym
        self.char = char


class FakeInput:
    def __init__(self, interface):
        self.interface = interface

    def writeString(self, string, index):
        self.interface.text.marker.move(index)
        for c in string:
            self.interface.key_press(FakeKeypress(c, c))
        return

    def backSpace(self, ammount, index):
        self.interface.text.marker.move(index)
        for i in range(ammount):
            self.interface.key_press(FakeKeypress('BackSpace', '\x08'))
