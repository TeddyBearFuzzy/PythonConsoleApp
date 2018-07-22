import sys, os, time
from user import User

print "Welcome !"
time.sleep(1)
print "Do you want to login or register ? [l/r]\n\n"

user_input = raw_input(">")

if user_input == "r":

    start_again = True

    while start_again:
        start_again = False

        print "Enter you name\n\n"
        user_input = raw_input(">")
        username = user_input

        print "Enter your password\n\n"
        user_input = raw_input(">")
        password = user_input

        user = User(username, password)

        if user.exists(username):
            print "Username is already took :(\n"
        start_again = True


if user_input == "l":

    print "Enter your account name\n\n"
    user_input = raw_input(">")
    username = user_input

    print "Enter your password\n\n"
    user_input = raw_input(">")
    password = user_input

    user = User(username, password)

    if user.exists(username):
        user.password_correct(password)
