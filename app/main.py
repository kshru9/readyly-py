from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)