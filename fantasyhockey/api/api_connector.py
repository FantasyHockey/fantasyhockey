import requests

class APIConnector:
    """
    A class to handle connections to API endpoints.

    This class provides methods to send GET requests to specified API endpoints and includes error handling to manage exceptions that might occur during the request.

    Methods
    -------
    get(endpoint)
        Sends a GET request to the specified API endpoint and returns the response.
    """

    def __init__(self):
        """
        Initializes the APIConnector instance.
        """
        self.base_url = "https://api-web.nhle.com/"
        self.session = requests.Session()

    def __validate_endpoint(self, endpoint):
        """
        Validates the endpoint URL by checking if it starts with the base URL.

        Parameters
        ----------
        endpoint : str
            The URL of the API endpoint to validate.

        Returns
        -------
        bool
            True if the endpoint starts with the base URL, False otherwise.
        """
        return endpoint.startswith(self.base_url)

    def get(self, endpoint):
        """
        Sends a GET request to the specified API endpoint.

        Parameters
        ----------
        endpoint : str
            The URL of the API endpoint to which the GET request is sent.

        Returns
        -------
        dict
            A dictionary containing the response data if the request was successful, or an error message if an error occurred.
        """
        try:
            if not self.__validate_endpoint(endpoint):
                raise ValueError("Invalid endpoint URL, must start with base URL.")
            response = self.session.get(endpoint)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.
            return response.json()  # Returns JSON response as a dictionary.
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Specific HTTP related error
            return {"error": str(http_err)}
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")  # Network problem (DNS failure, refused connection, etc)
            return {"error": str(conn_err)}
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")  # Maybe set up for a retry, or continue in a retry loop
            return {"error": str(timeout_err)}
        except requests.exceptions.RequestException as req_err:
            print(f"Error during request: {req_err}")  # Ambiguous exception
            return {"error": str(req_err)}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"error": str(e)}

    def __del__(self):
        """
        Destructor to close the session when the instance is being destroyed.
        """
        self.session.close()

