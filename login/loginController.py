from flask import request,render_template
from app import app
from login.loginLogic import loginLogic

loginObj = loginLogic()

@app.route("/login",methods = ['POST','GET'])
def loginControllerFuction():
    # if get requesg then go to /login
    if(request.method == 'POST'):
        data = request.form
        email = data.get('email')
        password = data.get('password')
        return loginObj.loginLogicFunction(email,password)
    return render_template("Authentication/login.html")