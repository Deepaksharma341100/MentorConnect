from flask import Flask, session ,render_template,redirect,request

app = Flask(__name__)
app.secret_key = "secret-key-Mentor-Connect"

import registration.registrationController
import login.loginController
import userProfile.userProfileController
import sessionRequest.sessionRequestController
import sessionRequest.sessionRequestLogic



@app.route('/' , methods=["GET"])
# set user info from session.get("userinfo") if not then set session["userinfo"] == none 
def mentorconnect():
    userInfo = session.get("userInfo")
    if(userInfo==None):
        session['userInfo'] = None

    return render_template("components/home.html" , userInfo=userInfo)


# route for dashboard if user is logged in and want to watch personal information
@app.route("/Dashboard" , methods=["GET"])
def Dashboard():
    user_Info = session.get("userInfo")
    return render_template("user/Dashboard.html" , user_Info = user_Info)


# get and post request for add bio here get request is handle not poat request (need to write the post code)
@app.route("/Bio" , methods=["GET","POST"])

def Bio():
    return render_template("user/bio.html")
