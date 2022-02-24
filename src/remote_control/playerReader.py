import re


class PlayerReader():
    def __init__(self, interface):
        self.interface = interface

    def getInstrument(self, playerName):
        text = self.interface.text.get('1.0', 'end-1c')
        p = re.compile("(?P<player>{})\s*>>\s*(?P<instru>\w+)".format(playerName))
        match = p.match(text)
        if match is not None:
            return match.groupdict()["instru"]
        return None
