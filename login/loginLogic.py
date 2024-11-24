import mysql.connector 
from flask import jsonify,session , render_template,redirect
class loginLogic():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user = "root",password="12345",database = "mentorconnect")
            self.cur = self.con.cursor(dictionary=True)
        except:
            return jsonify({'status': 'fail', 'message': 'database connection failed'}), 401
        
    def loginLogicFunction(self,email,password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.cur.execute(query, (email, password))
        user_info = self.cur.fetchone()

        if user_info:
        # Exclude the password from the response
            user_info.pop('password')
            session['userInfo'] = user_info
            print(session['userInfo'],"from loginlogic")
            # if email and password is correct go to home page
            return render_template("components/home.html")

        else:
            #if incorrect email or password then email or password is incorrect
            return render_template("Authentication/login.html" , message="Email or password incorect please try again")