from flask import Flask, render_template, request, redirect
import os
import mysql.connector

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a WSGI-compatible Flask app!"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhagath@11",
    database="candidate_registration"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        resume = request.files['resume']

        # Save resume
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
        resume.save(resume_path)

        # Insert data into database
        query = "INSERT INTO candidates (name, email, phone, dob, resume_path) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, dob, resume_path))
        db.commit()

        return redirect('/success')
    return render_template('index.html')

@app.route('/success')
def success():
    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)
