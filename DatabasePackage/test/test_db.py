try:
    from DatabasePackage.src.DatabaseSetingsModule import Database
    import unittest
    import json
    import requests
    import os
    import subprocess
except Exception as e:
    print(e)


class FlaskTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # code that is executed before all tests in one test run
        pass

    @classmethod
    def tearDownClass(cls):
        # code that is executed after all tests in one test run
        pass


    def test_class(self):
        """
        Ceck the response
        :return:
        """

        helper = Database()
        response = helper.connect()

        self.assertEqual(response, True)

if __name__ == "__main__":
    unittest.main()


