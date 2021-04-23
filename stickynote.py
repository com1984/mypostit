from flask import Flask, render_template, request, url_for, redirect
from models import loadJSONDB, saveJSONDB
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    notes = loadJSONDB()
    return render_template("stickynote.html", notes=notes)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    db = loadJSONDB()
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        aNote = {'name': name, 'date': date, 'content': content}
        db.append(aNote)
        saveJSONDB(db)
        return redirect(url_for('home'))
    else: 
        return render_template('stickyform.html')

if __name__ == "__main__":
    app.run(debug=True)