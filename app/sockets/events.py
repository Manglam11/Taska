from flask_socketio import SocketIO, emit

def register_socket_events(socketio):
    @socketio.on("connect")
    def handle_connect():
        print("A browser connected to WebSocket")