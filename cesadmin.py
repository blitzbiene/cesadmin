from flask import Flask,render_template,request,redirect,url_for
from flask_login import LoginManager,UserMixin,login_required,current_user,login_user,logout_user

import sys
app = Flask(__name__)

app.config['SECRET_KEY']="!@#@!$%@$%@#$^#@%^#$%GFGSDRFGT#W$%^#@$#@^^%@#$"
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self,id,username,password):
        self.id = id
        self.username=username
        self.password = password

muzammil = User(1,"muzammil","muznawaz@98")
krishna =  User(2,"krishna","@345admin")
abhishek = User(3,"abhishek","@987admin")

@login_manager.user_loader
def load_user(user_id):
    print(user_id,file=sys.stderr)
    if user_id=="1":
        return muzammil
    elif user_id=="2":
        return krishna
    else:
        return abhishek



@app.route('/login',methods=["GET","POST"])
def login():

    if hasattr(current_user,'username'):
        return redirect(url_for('dashboard'))
    if request.method=="POST":
        if request.form["username"]!="muzammil" and request.form["username"]!="abhishek" and request.form["username"]!="krishna":
            return render_template("login.html",error=True)
        user = muzammil
        if request.form["username"]=="krishna":
            user=krishna
        elif request.form["username"]=="abhishek":
            user=abhishek
        if request.form["password"]!=user.password:
            return render_template("login.html",error=True)
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template("login.html",error=False)

#DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',name=current_user.username)

#CERTIFICATES
@app.route('/certificates')
@login_required
def certificates():
    return render_template('certificates.html',name=current_user.username)

#EVENTS
@app.route('/events')
@login_required
def events():
    return render_template('events.html',name=current_user.username)

#NOTIFICATIONS
@app.route('/notifications')
@login_required
def notifications():
    return render_template('notifications.html',name=current_user.username)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__=='__main__':
    app.run(debug=True)
