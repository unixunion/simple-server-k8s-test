from flask import Flask

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return "Hello from Simple Server"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)