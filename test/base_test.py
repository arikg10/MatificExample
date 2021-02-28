from unittest import TestCase


class BaseTest(TestCase):
    @classmethod
    def setup_class(cls):
        print("Opening the app")
        print("Starting driver")

    @classmethod
    def teardown_class(cls):
        print("Closing app")
        print("Closing driver")