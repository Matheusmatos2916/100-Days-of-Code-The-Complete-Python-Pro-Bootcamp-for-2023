from flask import Flask, render_template, request
import sqlite3
 
app = Flask(__name__)
import os.path
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")
with sqlite3.connect(db_path) as db:
 
 
 
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
 
 
def get_cafes():
    conn = get_db_connection()
    cafes = conn.execute('SELECT * FROM cafes').fetchall()
    conn.close()
    return cafes
 
 
def add_cafe(name, wifi_strength, coffee_rating):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO cafes (name, wifi_strength, coffee_rating) VALUES (?, ?, ?)',
        (name, wifi_strength, coffee_rating)
    )
    conn.commit()
    conn.close()
 
 
def delete_cafe(cafe_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM cafes WHERE id = ?', (cafe_id,))
    conn.commit()
    conn.close()
 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        wifi_strength = request.form['wifi_strength']
        coffee_rating = request.form['coffee_rating']
        add_cafe(name, wifi_strength, coffee_rating)
 
    cafes = get_cafes()
    return render_template('index.html', cafes=cafes)
 
 
@app.route('/delete/<int:cafe_id>', methods=['GET'])
def delete(cafe_id):
    delete_cafe(cafe_id)
    return "Cafe deleted!"
 
 
if __name__ == '__main__':
    app.run(debug=True)