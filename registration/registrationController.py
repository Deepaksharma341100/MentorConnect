from flask import request, render_template
from app import app
from registration.registrationLogic import registerLogic

@app.route("/registration",methods = ['GET','POST'])
def registerationControllerFunction():
    #two methods if get request then go to /register page 
    if(request.method == "POST"):

        registerLogicObj = registerLogic()

        def convertNone(value):
            return value if value else None
        
        data = request.form
        print(data)
        firstName = data.get("firstName")
        middleName = convertNone(data.get("middleName"))
        lastName = convertNone(data.get("lastName"))
        email = data.get("email")
        phone = data.get("phone")
        userIdName = data.get("userIdname")
        password = data.get("password")
        return registerLogicObj.register(firstName,middleName,lastName,email,phone,userIdName,password)
    return render_template("Authentication/register.html")