from flask import Flask
from sonos import bp

app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/sonos')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
