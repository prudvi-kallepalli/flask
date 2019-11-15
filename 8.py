#import Flask class from flask module
from flask import Flask,render_template
#Flask constructor takes name of current module as an argument(i.e __name__)
app = Flask(__name__)
#route function of Flask class is a decorator which associated with hello_world() function
@app.route('/')
def hello_world():  	
   return render_template("panel.html")

@app.route('/bulb/<control>')
def bulb_ctrl(control):  	
   return "bulb"+control;
if __name__ == '__main__':
   app.run()