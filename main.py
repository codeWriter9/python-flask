from flask import Flask
from flask import redirect
from flask import url_for
app = Flask('app')

@app.route('/user/<name>', methods = ['GET'])  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  

@app.route('/admin', methods = ['GET'])  
def admin():  
    return 'admin'  
  
@app.route('/librarion', methods = ['GET'])  
def librarion():  
    return 'librarion'  
  
@app.route('/student', methods = ['GET'])  
def student():  
    return 'student'  

def about():  
    return "This is about page";     

@app.route('/home/<int:age>', methods = ['GET'])  
def home(age):  
    return "Age = %d"%age; 

@app.route('/', methods = ['GET'])
def hello_world():
  return 'Hello, World, Here I come!'

app.add_url_rule("/about","about",about)
app.run(host='0.0.0.0', port=8080, debug = True)
