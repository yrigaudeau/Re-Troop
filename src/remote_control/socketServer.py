from ..message import MSG_EVALUATE_STRING
import socket
from threading import Thread, Lock
import json

class SocketServer():
    def __init__(self, interface, port=42123):
        self.interface = interface
        self.mutex = Lock()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', port))

    def start(self):
        self.server.listen()
        Thread(target=self.wait_for_connection).start()

    def wait_for_connection(self):
        while 1:
            client, address = self.server.accept()
            print(client, address)
            Thread(target=self.wait_for_message, args=[client]).start()

        self.server.close()

    def wait_for_message(self, client):
        while 1:
            data = client.recv(512).decode()
            #print(data)
            try:
                args = json.loads(data)
            except:
                continue
            instru, otherAttr = self.interface.playerReader.getInstrument(args["name"])
            if instru is None:
                continue
            self.mutex.acquire()
            self.interface.playerBuilder.createPlayer(args["name"], instru)
            self.interface.playerBuilder.setAttribute(args["attr"], args["value"])
            self.interface.playerBuilder.setOtherAttributes(otherAttr)
            self.interface.add_to_send_queue(MSG_EVALUATE_STRING(self.interface.text.marker.id, self.interface.playerBuilder.player))
            self.mutex.release()

        client.close()
