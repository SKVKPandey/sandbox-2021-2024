from flask import Flask, request, render_template
from bcrypt import hashpw, gensalt, checkpw
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("users.sqlite", check_same_thread=False)

cursor = conn.cursor()
sql_query = """ CREATE TABLE if not exists users (
    name text NOT NULL,
    cno integer NOT NULL,
    email text PRIMARY KEY,
    pswd blob NOT NULL,
    pcolor text NOT NULL
)"""
cursor.execute(sql_query)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/pswd_auth')
def pswd_auth():
    return render_template("pswd_auth.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/email_verification', methods=['POST'])
def email_verification():
    email_check = request.form.get('email')

    cursor.execute("""SELECT email FROM users""")
    data = cursor.fetchall()

    if (email_check,) in data:
        cursor.execute("""SELECT pcolor FROM users WHERE email=='{}'""".format(email_check))
        pcolor = cursor.fetchall()
        return render_template("pswd_auth.html", data=[email_check,pcolor[0][0].strip()])

    else:
        return render_template("login.html", data='The Email ID Is Not Registered!')

@app.route('/pswd_verification', methods=['POST'])
def pswd_verification():
    email_check = request.form.get('email')
    pswd = request.form.get('pswd').encode("utf-8")

    cursor.execute("""SELECT email FROM users""")
    data = cursor.fetchall()
    
    if (email_check,) in data:
        cursor.execute("""SELECT pswd FROM users WHERE email=='{}'""".format(email_check))
        pswd_check = cursor.fetchall()
        cursor.execute("""SELECT name, cno, email  FROM users WHERE email=='{}'""".format(email_check))
        data_tuple = cursor.fetchall()
        if checkpw(pswd, pswd_check[0][0]):
            return render_template("home.html", data=[x for x in data_tuple[0]])
        else:
            return render_template('login.html', data='Incorrect Password!')

    else:
        return render_template('login.html')


@app.route('/register_validation', methods=['POST'])
def register_validation():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    contact = request.form.get('contact')
    email = request.form.get('email')
    pswd = request.form.get('pswd').encode("utf-8")
    pcolor = request.form.get('pcolor')

    name = fname + ' ' + lname
    
    cursor.execute("""SELECT email FROM users""")
    data = cursor.fetchall()

    if len(fname)<0 or len(email)<0 or pcolor not in ['black', 'grey', 'brown', 'cyan', 'pink', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']:
        return render_template("register.html", data='Please Fill The Required Fields!')

    elif len(contact)!=10:
        return render_template("register.html", data='Please Enter a Valid Contact Number!')

    elif '@' not in email:
        return render_template("register.html", data='Please Enter a Valid Email Address!')

    elif len(pswd) not in range(5,16):
        return render_template("register.html", data='Password Length Must Be Between 5-15 Characters!')

    elif (email,) in data:
        return render_template("login.html", data='Email ID Already Exists, Try Login!')

    else:
        pswd = hashpw(pswd, gensalt())
        insert_blob_query = """INSERT INTO users(name, cno, email, pswd, pcolor) VALUES (?,?,?,?,?)"""
        data_tuple = (name, contact, email, pswd, pcolor)
        cursor.execute(insert_blob_query, data_tuple)
        conn.commit()
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
