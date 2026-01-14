import sqlite3


conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")


cursor.execute("INSERT INTO users VALUES ('admin', 'password123')")
conn.commit()


def vulnerable_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchall()


def secure_login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchall()


print("Vulnerable login:", vulnerable_login("admin", "' OR '1'='1"))
print("Secure login:", secure_login("admin", "' OR '1'='1"))
