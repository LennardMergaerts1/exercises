import re

users = {}

def validate_password(password):
    return re.match(r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(.{8})",password)


def register():
    username = input("Geef username: ")
    wachtwoord = input("Geef wachtwoord: ")

    if validate_password(wachtwoord):
        users[username] = wachtwoord
        print("Success!")

    else: 
        print("er ging iets mis")

register()
print(users)