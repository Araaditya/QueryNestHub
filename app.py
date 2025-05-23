from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

# Set login page as home
@app.route('/')
def login():
    return render_template('login.html')

# Register route
@app.route('/register')
def register():
    return render_template('register.html')

# Forgot password route
@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)