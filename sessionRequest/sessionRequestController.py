from flask import request,session,render_template
from app import app
from sessionRequest.sessionRequestLogic import sessionRequestLogic



@app.route("/sessionaccepted",methods = ["GET","POST"])
def sessionRequestAcceptedControllerFunc():
    #get request to get the /sessionaccepted
    if(request.method == "GET"):
        return render_template("session/accept.html")
    else:
        sessionRequestLogicObj = sessionRequestLogic()
        data = request.json
        reqid = data.get("sessionrequestid")
        sessionlink = data.get('sessionlink')
        return sessionRequestLogicObj.sessionRequestAcceptFunction(reqid,sessionlink)

@app.route("/sessionrejected",methods=["DELETE"])
def sessionRequestRejectedControllerFunc():
    sessionRequestLogicObj = sessionRequestLogic()
    data = request.json
    reqid = data.get("sessionrequestid")
    return sessionRequestLogicObj.sessionRequestRejectFunction(reqid)

@app.route("/requestsession",methods=["GET","POST"])
def requestSessionControllerFunction():
       #get request to get the /sessionaccepted
    if(request.method == "GET"):
        return render_template("session/request.html")
    else:
        sessionRequestLogicObj = sessionRequestLogic()
        data = request.json
        mentorIdname = data.get("mentorUserIdName")
    # print(mentorIdname)
        sessionDate = data.get("sessionDate")
        sessionTime = data.get("sessionTime")
        sessionTopic = data.get("sessionTopic")
        sessionMessage = data.get("sessionMessage")
        return sessionRequestLogicObj.requestSessionFunction(mentorIdname,sessionDate,sessionTime,sessionTopic,sessionMessage)