class User(object):

    USER_FILE = "users.txt"

    def __init__(self, a_username, a_password):
        self.username = a_username
        self.password = a_password

    def save(self):
        with open(self.__class__.USER_FILE, "a") as user_file:
            user_file.write("%s, %s\n" % (self.username, self.password))

    @classmethod
    def exists(kls, username):

        with open(kls.USER_FILE, "r") as user_file:
            lines = user_file.read().splitlines()
            for line in lines:
                strings = line.split(",")
                current_username = strings[0]
                if current_username == username:
                    return True
            return False
    @classmethod
    def password_correct(kls, username, password):

        with open(kls.USER_FILE, "r") as user_file:
            lines = user_file.read().splitlines()
            for line in lines:
                strings = line.split(', ')
                current_username = strings[0]
                current_password = strings[1]
                if current_password == password and current_username == username:
                    return True
            return False
