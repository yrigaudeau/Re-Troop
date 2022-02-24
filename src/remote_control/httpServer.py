from ..message import MSG_EVALUATE_STRING
from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from threading import Thread, Lock

_interface = None
mutex = Lock()


class PlayerController(Resource):
    def get(self):
        return "Hello World"

    def post(self):
        global _interface, mutex

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('attr', type=str, required=True)
        parser.add_argument('value', type=str, required=True)
        args = parser.parse_args()

        mutex.acquire()
        try:
            instru = _interface.playerReader.getInstrument(args["name"])
            if instru is None:
                raise Exception(args["name"] + " n'est pas un player existant")
            _interface.playerBuilder.createPlayer(args["name"], instru)
            _interface.playerBuilder.setAttribute(args["attr"], args["value"])
            _interface.add_to_send_queue(MSG_EVALUATE_STRING(_interface.text.marker.id, str(_interface.playerBuilder.getPlayer())))
        except Exception as e:
            return make_response(str(e), 400)
        mutex.release()

        return make_response("ok", 200)


class HttpServer():
    def __init__(self, interface, port=5000):
        global _interface
        _interface = interface
        self.port = port
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(PlayerController, '/player')
        self.server = Thread(target=lambda: self.app.run(host="0.0.0.0", debug=False, port=self.port))
        # print(self.api.resources)

    def start(self):
        self.server.start()
        return

    def stop(self):
        pass
