import sys, os, time
from user import User

print "Welcome !"
time.sleep(0.3)
print "Do you want to login or register ? [l/r]\n\n"

user_input = raw_input(">")

if user_input == "r":
    #Register

    start_again = True

    while start_again:
        start_again = False

        print "Enter you name\n\n"
        user_input = raw_input(">")
        username = user_input

        print "Enter your password\n\n"
        user_input = raw_input(">")
        password = user_input

        if User.exists(username):
            print "Username is already took :(\n"
            start_again = True
        else:
            user = User(username, password)
            user.save()


if user_input == "l":
    #Login

    start_again = True

    while start_again:
        start_again = False
        print "Enter your account name\n\n"
        user_input = raw_input(">")
        username = user_input

        print "Enter your password\n\n"
        user_input = raw_input(">")
        password = user_input

        if User.password_correct(username, password):
            print "Connected as %s !" % (username)
        else:
            print "Username or Password incorrect :("
            
            start_again = True
