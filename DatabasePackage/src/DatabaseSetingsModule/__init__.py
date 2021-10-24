"""
DatabaseSetingsModule
----------------------
This is a Module which has Class for Database and database Settings

"""


class Database(object):

    """Database Class which is responsile for connecting to databse """

    def __init__(self, connection_string):
        """
        This is connection string o connect to sql server
        :param connection_string: str
        """
        self.connection_string = connection_string

    def connect(self) -> True:
        """
        This method is used to connect to database
        :return: Bool
        """
        print("connected to database")
        return True
