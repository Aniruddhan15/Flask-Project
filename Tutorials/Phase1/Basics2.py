from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello sir"


@app.route('/next')
def next():
    return "Sir this is my 2ndry page in portfolio"

@app.route('/printer/<name>')
def printer(name):
    return f"This is the 3rd page of portfolio {name}"


@app.route('/resume/<work>')
def resume(work):
    return f"This is his resume {work}"
    # return "this is his work {work}".format{}
    
@app.route('/htmlpage')
def htmlpage():
    return render_template('about.html')

@app.route('/research')
def research():
    return render_template('researchProfile.html')

@app.route('/intern')
def intern():
    return render_template('internpdf.html')


    

    

if __name__ == '__main__':
    app.run(debug=True)
    
