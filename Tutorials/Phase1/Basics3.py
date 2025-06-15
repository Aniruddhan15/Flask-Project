from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Welcome to Aniruddhan's profile"

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/youremail/<email>')
def youremail(email):
    return f"Please enter your {email}"

@app.route('/photos/<photo1>')
def photos(photo1):
    return render_template('photography.html', photo1=photo1)

## getting user input using request form


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume/<email>')
def resume(email):
    return render_template('resume.html',email)

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/predict', method=['GET','POST'])
def predict():
    if request.method == 'POST':
        name = request.form['name']
        return 'your name is {}'.format(name)
    
    
@app.route('/greet',methood=['GET','POST'])
def greet():
    if request.method == 'POST':
        age = request.form['age']
        name = request.form['name']
        email = request.form['email']
        sal = request.form['salary']
        
        return f"Hi {name}. Here is Aniruddhan's {age} and {email}. He is expecting a salary of {sal}"
    
@app.route('/getmethod', method=['GET'])
def getmethod():
    if request.method == 'GET':
        name = request.args.get('name')
        
        return f"hi {name}"
    
    
@app.route('/check', method=['GET'])
def check():
    if request.method =='GET':
        a = int(request.args.get('a',0))
        b = int(request.args.get('b',0))
        
        if ((a % 2==0) & (b%2==0)):
            return "It is even"
        else:
            return "odd! Sorry"
    else:
        return 'sorry guys, it is post method'
             
@app.route('/sumof2')
def sumof2():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    sum = a+b
    return f'The sum of 2 numbers is {sum}'

@app.route('/login', method=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['password']
        
        if user=='secret' & pwd =='Nothin':
            return f"Succesfully logged in through {user}"
        else:
            breakpoint
    


             
if __name__ == '__main__':
    app.run(debug=True)
    