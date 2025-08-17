from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker! My name is Daniel Stanciu student at UCLL Leuven.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
