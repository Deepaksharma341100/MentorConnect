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


