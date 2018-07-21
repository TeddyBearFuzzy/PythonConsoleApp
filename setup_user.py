import time
import sys


password = "no password"
username = "User0"
user_answer = "None"
is_admin = "False"
user_list = open("users.txt", "r+")
user_answer_length = sys.getsizeof(user_answer)


def start(isAdmin, user_answer):
    print ("\n\nMenu(m)\nQuit(q)\nOptions(o)")
    if is_admin == "True":
        print "Admin Commands(admin)"
    else:
        print "\n"

    user_answer = input("Command ?")
    if user_answer == "q":
        #Quit
        sys.exit
    elif user_answer == "o":
        #Options
        options()
    elif user_answer == "admin" and is_admin:
        #Admin commands
        print "\n\nDelete specific user(ds)\nClean whole user list(aah)\nBack to main menu(b)"
        user_answer = input("Command ?")
        if user_answer == "ds":
            user_answer = input("Enter user name and password (*username*, *password*")
            filedata = user_list.read()
            filedata.replace("%s, %s" % (user_answer[0:user_answer_length-7],
                                         user_answer[user_answer_length-7:user_answer_length]), "")
    else:
        menu()



def menu() :
    print "\n\nnew Calculation(n)\nLoad Calculation(l)"
    user_answer = input("Command ?")
    if user_answer == "n":
        print "Coming soon"
    else:
        print "Coming Soon"
def options() :
    print "\n\nDelete account(d)\nUser list(u)\nBack to main(b)"
    user_answer = input("Command ?")
    if user_answer == "d":
        print "Thanks for trying this beta"
        filedata = user_list.read()
        filedata.replace("%s, %s" % (username, password), "")
    elif user_answer == "u":
        print user_list
        user_answer = input("Return to main menu(b)")
        if user_answer == "b":
            start()
    else:
        start()
def quit() :
    exit(10)

def login() :
    login_input = input("Account name and Password (*account_name*, *password (none is you have none set)*")

    if login_input == "Admin":
        print "Initializing interface..."
        is_admin = "True"
        start()
    for login_input in user_list:
        calculate_username = sys.getsizeof(login_input)
        username_position = user_answer_length - 7
        username = login_input[0:username_position]
        print "Welcome back %s !" % (username)
        print "We are initializing interface..."
        time.sleep(1)
        start()
    else:
        print "Sorry, user does not exist (404 not found)"

def register():
    username = input("Enter your name: ")  # type: str
    if username == "Admin":
        print "Welcome back %s !" % (username)
        is_admin = "True"
        print "We are initializing interface..."
        time.sleep(1)
        start(is_admin, user_answer)
    print "Welcome %s" % username
    password = input("Do you want to set a password for %s's account ? (Y[yes] N[no])" % (username))
    if password == "Y":
        password = input("Set %s's password to (6 letters):" % (username))
        user_list.write("%s, %s \n" % (username, password))
        print "Welcome ! Your account has been registered as: %s with password %s !" % (username, password)
        time.sleep(1)
        print "We are initializing interface..."
        time.sleep(1)
        start(is_admin, user_answer)
    else:
        user_list.write("%s, none\n" % (username))
        print "Welcome ! Your account has been registered as: %s with no password !" % (username)
        time.sleep(1)
        print "We are initializing interface..."
        time.sleep(1)
        start(is_admin, user_answer)

print "Initializing..."
login_or_register = input("Login or Register ? (l/r)")
if login_or_register == "r":
    register()

else:
    login()
