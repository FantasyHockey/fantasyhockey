from fantasyhockey.database.database_connector import DatabaseConnector

class DatabaseOperator:
    """
    A class to perform read and write operations on a MySQL database.

    This class uses a DatabaseConnector instance to establish a connection for executing SQL queries.
    
    Attributes
    ----------
    db_connection : DatabaseConnector
        An instance of DatabaseConnector for managing database connections.

    Methods
    -------
    read(query, params=None)
        Executes a SELECT SQL query and returns fetched data.

    write(query, params=None)
        Executes an INSERT, UPDATE, or DELETE SQL query.
    """

    def __init__(self):
        """
        Initializes the DatabaseOperator with a DatabaseConnector instance.

        Parameters
        ----------
        db_connection : DatabaseConnector
            The DatabaseConnector instance used to connect to the database.
        """
        self.db_connection = DatabaseConnector()

    def read(self, query, params=None):
        """
        Executes a SELECT SQL query using the provided query and parameters.

        Parameters
        ----------
        query : str
            The SQL query to execute.
        params : tuple, optional
            A tuple of parameters to use with the SQL query, by default None.

        Returns
        -------
        list
            A list of tuples representing the rows fetched from the database.
        """
        try:
            connection = self.db_connection.open_connection()
            if connection is not None:
                cursor = connection.cursor()
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                self.db_connection.close_connection(connection)

    def write(self, query, params=None):
        """
        Executes an INSERT, UPDATE, or DELETE SQL query using the provided query and parameters.

        Parameters
        ----------
        query : str
            The SQL query to execute.
        params : tuple, optional
            A tuple of parameters to use with the SQL query, by default None.

        Returns
        -------
        int
            The number of rows affected by the query.
        """
        try:
            connection = self.db_connection.open_connection()
            if connection is not None:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            if connection.is_connected():
                cursor.close()
                self.db_connection.close_connection(connection)
