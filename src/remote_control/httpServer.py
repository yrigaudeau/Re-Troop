from re import I
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from threading import Thread

_interface = None

class PlayerController(Resource):
    def get(self):
        raise RuntimeError("Server going down")
        return "hello"

    def post(self):
        global _interface

        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('attr', type=str, required=True)
        parser.add_argument('value', type=str, required=True)
        args = parser.parse_args()

        try:
            _interface.playerBuilder.editPlayer(args['name'], args['attr'], args['value'])
            _interface.single_line_evaluate()
        except Exception as e:
            return str(e)

        return


class HttpServer():
    def __init__(self, interface, port=5000):
        global _interface
        _interface = interface
        self.port = port
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(PlayerController, '/player')
        self.server = Thread(target=lambda: self.app.run(debug=False, port=self.port))
        #print(self.api.resources)

    def start(self):
        self.server.start()
        return

    def stop(self):
        pass
