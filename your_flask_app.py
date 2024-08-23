from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy data for demonstration
clients = []
cases = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients')
def list_clients():
    return render_template('clients.html', clients=clients)

@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        client_name = request.form['client_name']
        email = request.form['email']
        phone = request.form['phone']
        clients.append({
            'name': client_name,
            'email': email,
            'phone': phone
        })
        flash('Client added successfully!')
        return redirect(url_for('list_clients'))
    return render_template('add_client.html')

@app.route('/cases')
def list_cases():
    return render_template('cases.html', cases=cases)

@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    if request.method == 'POST':
        case_title = request.form['case_title']
        client_name = request.form['client_name']
        description = request.form['description']
        cases.append({
            'title': case_title,
            'client': client_name,
            'description': description
        })
        flash('Case added successfully!')
        return redirect(url_for('list_cases'))
    return render_template('add_case.html', clients=clients)

@app.route('/upload_document', methods=['GET', 'POST'])
def upload_document():
    if request.method == 'POST':
        if 'document' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['document']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = file.filename
            filepath = os.path.join('documents', filename)
            file.save(filepath)
            flash('Document uploaded successfully!')
            return redirect(url_for('index'))
    return render_template('upload_document.html')

if __name__ == '__main__':
    app.run(debug=True)
