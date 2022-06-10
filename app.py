from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'web-app-2: /'

@app.route('/developer', strict_slashes=False) # matches with trailing /
def developer():
    return 'web-app-2: /developer'

@app.route('/developer/sub/path', strict_slashes=False) # matches with trailing /
def developer_sub_path():
    return 'web-app-2: /developer/sub/path'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
