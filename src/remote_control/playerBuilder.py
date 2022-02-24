from .fakeInput import FakeInput
from ..message import *

class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return "{}={},".format(self.name, self.value)

    def __len__(self):
        return len(str(self))


class Player:
    def __init__(self, name, instrument):
        self.attributes = {}
        self.name = name
        self.instrument = instrument

    def __str__(self):
        attrStr = ""
        for attribute in self.attributes:
            attrStr += str(self.attributes[attribute])
        attrStr = attrStr[:-1]
        return "{} >> {}({})\n".format(self.name, self.instrument, attrStr)

    def __len__(self):
        return len(str(self))

    def editAttribute(self, attributeName, value):
        if attributeName in self.attributes:
            self.attributes[attributeName].value = value
        else:
            self.attributes[attributeName] = Attribute(attributeName, value)
        return

    def attributeExists(self, attributeName):
        return not attributeName in self.attributes

    def getAttribute(self, attributeName):
        return self.attributes[attributeName]

    def removeAttribute(self, attributeName):
        self.attributes.pop[attributeName]
        return

    def getAttributeIndex(self, attributeName):
        # end index of attribute
        totalLen = len(self.name)+6+len(self.instrument)
        for a in self.attributes:
            totalLen += len(self.attributes[a])
            if a == attributeName:
                break
        return totalLen


class PlayerBuilder:
    def __init__(self, interface):
        self.players = {}
        self.fakeInput = FakeInput(interface)
        self.interface = interface
        self.init = False
        self.indexStart = 0
        self.commentary = "### Auto-generated do not touch ###\n"

    def __str__(self):
        comm = "### Auto-generated do not touch ###\n"
        playerStr = ""
        for player in self.players:
            playerStr += str(self.players[player]) + '\n'

        return comm + playerStr

    def __len__(self):
        return len(str(self))

    def addPlayer(self, playerName, instrument):
        if not self.init:
            self.fakeInput.writeString(self.commentary, self.indexStart)
            self.init = True

        if playerName in self.players:
            raise Exception("Le player {} existe déjà".format(playerName))

        player = Player(playerName, instrument)
        self.players[playerName] = player
        self.fakeInput.writeString(str(player), len(self))

    def editPlayer(self, playerName, attributeName, value):
        if not playerName in playerName:
            raise Exception("Le player {} n'existe pas".format(playerName))

        player = self.players[playerName]
        newAttr = player.attributeExists(attributeName)

        if not newAttr:
            oldAttrLen = len(player.getAttribute(attributeName))
            oldAttrIndex = player.getAttributeIndex(attributeName)

        player.editAttribute(attributeName, value)
        attribute = player.getAttribute(attributeName)

        #if newAttr:
        #    # Write new player
        #    self.fakeInput.writeString(str(attribute), self.getPlayerIndex(playerName)-len(attribute)-2)
        #else:
        #    # Write modifications only don't rewrite all
        #    self.fakeInput.backSpace(oldAttrLen, self.getPlayerIndex(playerName)-len(player)+oldAttrIndex-2)
        #    self.fakeInput.writeString(str(attribute), self.getPlayerIndex(playerName)-len(player)+oldAttrIndex-oldAttrLen-2)

        self.interface.add_to_send_queue(MSG_EVALUATE_STRING(self.interface.text.marker.id, str(player)))
        return

    def removePlayer(self, playerName):
        self.players.pop[playerName]
        return

    def getPlayerIndex(self, playerName):
        totalLen = len(self.commentary)
        for p in self.players:
            totalLen += len(self.players[p]) + 1
            if p == playerName:
                break
        return totalLen
