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
    name = request.form['name']
    initial = request.form['initial']
    phone = request.form['phone']
    
    
    # Insert data into MySQL
    query = "INSERT INTO candidates (name, initial, phone) VALUES (%s, %s, %s)"
    values = (name, initial, phone)
    cursor.execute(query, values)
    db.commit()
print(f"name: {name}, initial: {initial}, phone: {phone}")
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
