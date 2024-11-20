from flask import request, render_template
from app import app
from registration.registrationLogic import registerLogic

@app.route("/registration",methods = ['GET','POST'])
def registerationControllerFunction():
    if(request.method == "POST"):

        registerLogicObj = registerLogic()

        def convertNone(value):
            return value if value else None
        
        data = request.form
        print(data)
        firstName = data.get("FirstName")
        middleName = convertNone(data.get("MiddleName"))
        lastName = convertNone(data.get("LastName"))
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")
        return registerLogicObj.register(firstName,middleName,lastName,email,phone,password)
    return render_template('Authentication/register.html')