#!usr/bin/python3

from flask import Flask

app = Flask(__name__)# Always do this in your F;ASK  script

@app.route("/")# when you go to the root of your server.. do the following 
def endoftheday():#function to trigger at ROOT
    return "Class is nearing the end of wednesday" #REturn this if you goto ROOT


if __name__ == "__main__":
    app.run(port=5006) #run on port 5006

