logged_in = False
def login_required(func):
    def wrapper():
        global logged_in
        if not logged_in:
            username = input("Username: ")
            password = input("Password: ")
            if username == "Hazel" and password == "1234":
                logged_in = True
                print("Login successful")
                func()
            else:
                print("Invalid credentials")
    return wrapper

@login_required
def greet():
    print("Hello, welcome!")

greet()
