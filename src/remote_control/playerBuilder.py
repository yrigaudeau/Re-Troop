
class Method():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return ".{}({})".format(self.name, self.value)


class Attribute():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "{}={}".format(self.name, self.value)


class Player():
    def __init__(self, name, instrument, attribute=None, method=None, otherAttributes=None):
        self.name = name
        self.instrument = instrument
        self.attribute = attribute
        self.otherAttributes = otherAttributes
        self.method = method

    def setAttribute(self, attribute):
        self.attribute = attribute

    def setMethod(self, method):
        self.method = method

    def setOtherAttributes(self, attributes):
        self.otherAttributes = attributes

    def __str__(self):
        return "{} >> {}({},{}){}".format(self.name, self.instrument, self.otherAttributes, self.attribute if self.attribute != None else "", self.method if self.method != None else "")


class PlayerBuilder():
    def __init__(self, interface):
        self.interface = interface
        self.player: Player = None

    def createPlayer(self, name, instrument):
        self.player = Player(name, instrument)

    def setAttribute(self, name, value):
        self.player.setAttribute(Attribute(name, value))

    def setOtherAttributes(self, attributes):
        self.player.setOtherAttributes(attributes)

    def setMethod(self, name, value):
        self.player.setMethod(Method(name, value))
