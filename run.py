from app import create_app, socketio,models, db
from flask_migrate import Migrate

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)