# Login System with Password Validation

USERNAME = "admin"
PASSWORD = "Admin@123"

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "@#$%&!" for char in password):
        return False
    return True


print("🔐 Secure Login System 🔐")

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("✅ Login Successful!")
        break

    elif not is_valid_password(password):
        print("❌ Password does not meet security requirements")
        print("Password must have:")
        print("- At least 8 characters")
        print("- One uppercase letter")
        print("- One lowercase letter")
        print("- One digit")
        print("- One special character (@#$%&!)")

    else:
        print("❌ Invalid username or password")

    attempts -= 1
    print(f"Attempts left: {attempts}")

if attempts == 0:
    print("🚫 Account locked due to multiple failed attempts")
