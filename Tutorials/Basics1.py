from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello to my portfolio"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    


from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Something happened to my portfloio "


if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home11():
    return "somethingllll"

if __name__ == '__main__':
    app.run(debug=True)
    
    
