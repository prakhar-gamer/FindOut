from flask import Flask, render_template, send_from_directory, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
 
#makes the database so we cna implemt CRUD into the Phrase
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class Phrase(db.Model):
    phrase = db.Column(db.Text, nullable=False)
    pid = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(30), nullable=False)

with app.app_context():
    db.create_all()
    


@app.route("/check1", methods=['POST'])
def check1():
    data = request.form.get('pass1')
    if data == "guy":
        return redirect("/DudeYourAGenius")
    
    return "try again :()"

@app.route("/")
#play a audio clip -> unscramble it and have a button gives u the link to the seocund part
def index():
    return render_template('index.html')

@app.route("/audio/speech.mp3")
def getAudio():
    return send_from_directory("audio", "speech.mp3")

@app.route("/DudeYourAGenius")
#Allows you to make a account and update it to crude
def Hobbies():
    return render_template('accountcreation.html')

@app.route("/addPhrase", methods=['POST'])
def addTask():
    phrase = request.form.get('phrase')
    password = request.form.get('phrasePassword')
    id = request.form.get('phraseId')
    return "funny"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True);