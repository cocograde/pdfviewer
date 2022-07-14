import webbrowser
from wsgiref.simple_server import make_server
from app import app

if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    webbrowser.open("http://127.0.0.1:5000")
    server.serve_forever()
    app.run()