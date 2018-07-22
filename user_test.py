from user import User
from unittest import TestCase
import unittest

class UserTest(TestCase):

    def setUp(self):
        with open("users.txt", "w") as users_file:
            users_file.write("")

    def test_save_user(self):

        tadeo = User("Tadeo", "toto")
        tadeo.save()

        with open("users.txt", "r") as users_file:
            lines = users_file.readlines()
            first_line = lines[0]
            self.assertEqual("Tadeo, toto", first_line)

    def test_save_two_users(self):

        tadeo = User("Tadeo", "toto")
        tadeo.save()

        cyrille = User("Cyrille", "titi")
        cyrille.save()

        with open("users.txt", "r") as users_file:
            lines = users_file.read().splitlines()
            first_line = lines[0]
            self.assertEqual("Tadeo, toto", first_line)
            second_line = lines[1]
            self.assertEqual("Cyrille, titi", second_line)

    def test_exists(self):
        tadeo = User("Tadeo", "toto")
        tadeo.save()

        self.assertTrue(User.exists("Tadeo"))
        self.assertFalse(User.exists("Cyrille"))


if __name__ == "__main__":

    unittest.main(UserTest, "test_exists")



