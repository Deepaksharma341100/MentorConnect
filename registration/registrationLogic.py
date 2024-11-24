import mysql.connector
from flask import jsonify, render_template

class registerLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def register(self,firstName,middleName,lastName,email,phone,userIdName,password):
        query = "INSERT INTO USERS (FIRSTNAME,MIDDLENAME,LASTNAME,EMAIL,PHONE,USERIDNAME,PASSWORD) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
           self.cur.execute(query, (firstName,middleName,lastName,email,phone,userIdName, password))
           self.con.commit()
           return render_template("Authentication/login.html")
        except mysql.connector.errors.IntegrityError:
            # if intefrity error then redirect to register username already exist
            return render_template("Authentication/register.html" , message="username already exist try another")
        except:
            return jsonify({'status': 'fail', 'message': 'failed while commiting query'}), 401