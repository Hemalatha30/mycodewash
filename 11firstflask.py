#!usr/bin/python3

from flask import Flask

app = Flask(__name__)# Always do this in your F;ASK  script

@app.route("/")# when you go to the root of your server.. do the following 
def endoftheday():#function to trigger at ROOT
    return "Class is nearing the end of wednesday" #REturn this if you goto ROOT

@app.route("/hello/<name>", defaults={'position': 'Admin Assistant'})
#@app.route("/hello/<name>/<position>")
def hellostudents(name, position):
    return "Hello {1} {0}. I am pleased to meet you {0}".format(name, position)   
    # return "Welcome to class" + name
  

if __name__ == "__main__":
    app.run(port=5006) #run on port 5006

