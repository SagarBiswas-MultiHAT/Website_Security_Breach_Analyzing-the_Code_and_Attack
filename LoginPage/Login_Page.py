# http://localhost:8080/login

from flask import Flask, request, render_template_string

app = Flask(__name__)

# Example regex validation (for demonstration purposes, not secure)
import re

# Regex pattern for username validation (this is where the vulnerability might lie)
USERNAME_PATTERN = r"^[a-zA-Z0-9_]+$"  # Only allows alphanumeric characters and underscores, at least one character long


# In-memory storage for a single user (for demo purposes)
users = {
    "administrator_": "admin_123"  # Example user (username: administrator_, password: admin_123)
}

@app.route('/login', methods=['GET', 'POST'])
# This line creates a route in the Flask application that listens for requests to the URL '/login'.
# The 'methods' argument specifies that this route can handle both GET and POST HTTP requests.
# - GET: Used when the user initially visits the login page. The server responds by rendering the login form.
# - POST: Used when the user submits the login form with their username and password. The server processes this data to authenticate the user.
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate the username against the regex pattern
        if not re.match(USERNAME_PATTERN, username):
            return "Invalid username format!"

        # Check if the username exists and the password matches
        if username in users and users[username] == password:
            return "Welcome, " + username + "!"
        else:
            return "Invalid username or password!"

    # Render a simple login form
    return render_template_string('''
        <style>
            /* Center the form on the page */
            form {
                margin: 100px auto;
                width: 300px;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
            }
            
            /* Style the input fields */
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin: 5px 0 15px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }
            
            /* Style the submit button */
            input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            
            input[type="submit"]:hover {
                background-color: #45a049;
            }
        </style>
        
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username"><br>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br>
            
            <input type="submit" value="Login">
        </form>
    ''')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
