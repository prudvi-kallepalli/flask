#import Flask class from flask module
from flask import Flask
#Flask constructor takes name of current module as an argument(i.e __name__)
app = Flask(__name__)
#route function of Flask class is a decorator which associated with hello_world() function
@app.route('/')
def hello_world():  	
   return "<html><body><h1>This is good</h1></body></html>"

if __name__ == '__main__':
   app.run()