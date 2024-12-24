from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",  # Use 'localhost' or '127.0.0.1'
    port=3306,  # Specify port separately
    user="root",
    password="Bhagath@11"
)

cursor = db.cursor()

@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form['పేరు']
    email = request.form['email']
    phone = request.form['phone']
    
    # Save the resume file (optional)
    resume_path = f'uploads/{resume.filename}'
    resume.save(resume_path)

    # Insert data into MySQL
    query = "INSERT INTO candidates (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
