from flask import Flask, render_template, send_from_directory, redirect, request

app = Flask(__name__)

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
    return"I like the gym, computers, and music"

@app.route("/login")
#uses a auth and then if its a account lets u enter the victory screen
def Login():
    return"Dogs are pretty fire though"

@app.route("/victory!!!!")
#a Screen that says VICTORY!
def victory():
    return "Victory!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True);