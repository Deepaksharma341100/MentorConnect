from flask import Flask, session ,render_template

app = Flask(__name__)
app.secret_key = "secret-key-Mentor-Connect"

import registration.registrationController
import login.loginController


@app.route('/' , methods=["GET"])
def mentorconnect():
    userInfo = session.get("userInfo")
    if(userInfo==None):
        session['userInfo'] = None

    return render_template("components/home.html")

@app.route("/Dashboard" , methods=["GET"])

def Dashboard():
    return render_template("user/Dashboard.html")
@app.route("/Bio" , methods=["GET","POST"])

def Bio():
    return render_template("user/bio.html")
