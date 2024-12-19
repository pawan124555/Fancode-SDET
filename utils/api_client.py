import requests
from requests.exceptions import RequestException, Timeout, HTTPError

BASE_URL = "http://jsonplaceholder.typicode.com"

class APIClient:
    @staticmethod
    def get(endpoint, retries=3, timeout=5):
        """
        Fetch data from the specified endpoint with retries and error handling.
        Args:
            endpoint (str): API endpoint
            retries (int): Number of retries for failed requests
            timeout (int): Request timeout duration in seconds
        Returns:
            list/dict: JSON response data
        """
        url = f"{BASE_URL}/{endpoint}"
        attempt = 0
        while attempt < retries:
            try:
                response = requests.get(url, timeout=timeout)
                response.raise_for_status()  # Raise HTTP errors
                return response.json()
            except (Timeout, HTTPError, RequestException) as e:
                attempt += 1
                print(f"Attempt {attempt}: Failed to fetch data from {url} - {e}")
        raise Exception(f"Failed to fetch data from {url} after {retries} attempts.")
