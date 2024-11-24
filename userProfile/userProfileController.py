from flask import request,session,render_template,jsonify
from app import app
from userProfile.userProfileLogic import userProfileLogic

userProfileObj = userProfileLogic()
@app.route("/user/<idname>" , methods=["GET"])
def userProfileControllerFunc(idname):
  user_info= userProfileObj.userProfileFunction(idname)
  #if user_info is not exist then message will be shown at home page that user not found
  if not user_info or isinstance(user_info, str) and user_info.lower() == "user not found":
          return render_template("error/error.html", message="User not found")
  return render_template('user/Dashboard.html', user_Info=user_info)
 
       