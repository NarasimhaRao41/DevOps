from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        username = request.form['username']
        email = request.form['email']
        phone_number = request.form['phoneNumber']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        gender = request.form['gender']

        # Here you could save the data, but for now, we just print it
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Phone Number: {phone_number}")
        print(f"Gender: {gender}")

        # Redirect after successful registration
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
