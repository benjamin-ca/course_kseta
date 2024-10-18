import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("Running the test.")

    def test_fit(self):
        exec(open("main.py").read())

    def tearDown(self):
        print("Donee")
