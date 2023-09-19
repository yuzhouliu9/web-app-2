from flask import Flask
app = Flask(__name__)

@app.route('/web-app-2')
def index():
    return 'Hello world, this is web-app-2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
