import mysql.connector
from flask import jsonify

class registerLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="Deepak@13402",database = "users")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def register(self,firstName,middleName,lastName,email,phone,password):
        query = "INSERT INTO  users (FirstName, MiddleName, LastName, email, phone, password) VALUES (%s,%s,%s,%s,%s,%s)"
        try:
            self.cur.execute(query, (firstName,middleName,lastName,email,phone, password))
            self.con.commit()
            return jsonify({'status': 'success'}), 200
        except:
            return jsonify({'status': 'fail', 'message': 'failed while commiting query'}), 401