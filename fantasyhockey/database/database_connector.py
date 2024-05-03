import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    """
    A class used to manage connections to a MySQL database.
    
    This class provides methods to open and close connections to a MySQL database using the `mysql.connector` library. It includes basic error handling to manage connection issues.
    
    Methods
    -------
    open_connection()
        Opens a connection to the MySQL database and returns the connection object or None if an error occurs.
        
    close_connection(connection)
        Closes a given MySQL database connection.
    """

    def __init__(self):
        """
        Initializes the DatabaseConnector instance.
        """
        pass

    def open_connection(self):
        """
        Opens a connection to a MySQL database and handles potential errors during the connection process.
        
        Attempts to establish a connection using predefined parameters (host and user). The database used is hosted locally and connected with the user 'root' without a password.
        
        Returns
        -------
        mysql.connector.connection.MySQLConnection or None
            An instance of MySQLConnection if the connection is successful, None if an error occurs.
        """
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="fantasyhockey"
            )
            return connection
        except Error as e:
            print(f"Error connecting to MySQL Database: {e}")
            return None

    def close_connection(self, connection: mysql.connector.connection.MySQLConnection):
        """
        Closes a MySQL database connection.
        
        Parameters
        ----------
        connection : mysql.connector.connection.MySQLConnection
            The connection to the MySQL database that needs to be closed.
            
        This method closes the provided MySQL database connection. It is important to close connections to release system resources.
        """
        try:
            if connection.is_connected():
                connection.close()
        except Error as e:
            print(f"Error while closing the MySQL connection: {e}")
