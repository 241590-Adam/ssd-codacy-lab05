import os
import sqlite3
import secrets

# Fetching the password from environment variables to keep it secure and hidden
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    # Fixed indentation and established database connection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Using '?' placeholder to safely handle input and prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    results = cursor.fetchall()
    conn.close()
    return results

def generate_token():
    # Switched to 'secrets' module for generating cryptographically strong tokens
    return str(secrets.randbelow(900000) + 100000)

# Removed the 'unused_count' variable to keep the code clean and efficient

# Example usage (Safe versions)
print(get_user('admin'))
print(generate_token())
