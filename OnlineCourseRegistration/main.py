from flask import *
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dhanakode@sql",
   database="exampython"
)

@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template("homepage.html")

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template("register.html")

@app.route('/profiles',methods=['GET','POST'])
def profiles():
    return render_template("profiles.html")

@app.route('/successStories',methods=['GET','POST'])
def successStories():
    return render_template("successStories.html")

@app.route('/testLists',methods=['GET','POST'])
def testLists():
    return render_template("testLists.html")

@app.route('/save_login',methods=['GET','POST'])
def save_login():
    if(request.method=="POST"):
        email=request.form.get("Email")
        password=request.form.get("psw")
        mycursor = mydb.cursor()
        sql="select email,password from signup where email=%s and password=%s"
        data=(email,password,)
        mycursor.execute(sql,data)
        result = mycursor.fetchall()
        if(len(result)==1):
            return render_template("login.html")

        else:
            result = -1
            if result == -1:
                m = "check your email and password"
                l = "/login"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("login.html")


@app.route('/save_signup',methods=['GET','POST'])
def save_signup():
    if(request.method=="POST"):
        Name = request.form.get("Name")
        email=request.form.get("email")
        password=request.form.get("psw")
        psw_repeat = request.form.get("psw_repeat")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT email from signup where email='" + email + "'")
        result=mycursor.fetchall()
        if(len(result)==0):
            mycursor.execute("INSERT INTO signup VALUES(%s,%s,%s,%s)", (Name, email, password, psw_repeat))
            mydb.commit()
            return render_template("login.html")
        else:
            result=-1
            if result == -1:
                m = "This email has already exists"
                l = "/signup"
                ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
                return ms
            return render_template("signup.html")

# @app.route('/save_register',methods=['GET','POST'])
# def save_register():
#     if(request.method=="POST"):
#         firstname=request.form.get("firstname")
#         Middlename=request.form.get("Middlename")
#
#     lastname = request.form.get("lastname")
#         mycursor = mydb.cursor()
#         sql="select firstname,Middlename,lastname from signup where firstname=%s and Middlename=%s"
#         data=(firstname,Middlename,lastname)
#         mycursor.execute(sql,data)
#         result = mycursor.fetchall()
#         if(len(result)==1):
#             return render_template("register.html")
#
#         else:
#             result = -1
#             if result == -1:
#                 m = "check your details"
#                 l = "/login"
#                 ms = '<script type="text/javascript">alert("' + m + '");location="' + l + '";</script>'
#                 return ms
#             return render_template("register.html")




if __name__ == "__main__":
    app.run(debug=True)