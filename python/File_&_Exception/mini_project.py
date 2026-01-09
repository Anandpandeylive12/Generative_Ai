class LoginError(Exception):
    pass

def login(username, password):
    if username != "admin":
        raise LoginError("Username not found.")
    if password != "1234":
        raise LoginError("Incorrect password.")
    return "Login successful!"

try:
    print(login("admin", "1234"))
except LoginError as e:
    print("Login failed:", e)
