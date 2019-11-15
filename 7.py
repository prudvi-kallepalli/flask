#import Flask class from flask module
from flask import Flask,render_template
#Flask constructor takes name of current module as an argument(i.e __name__)
app = Flask(__name__)
#route function of Flask class is a decorator which associated with hello_world() function
@app.route('/<name>')
def hello_world(name):  	
   return render_template("hello2.html",user=name)

if __name__ == '__main__':
   app.run()