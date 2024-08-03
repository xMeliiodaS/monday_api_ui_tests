class ResponseWrapper:
    def __init__(self, ok, status, data):
        """
        Initializes a ResponseWrapper instance with the given parameters.

        Args:
            ok (bool): Indicates whether the response was successful.
            status (int): The HTTP status code of the response.
            data (dict): The response data in JSON format.
        """
        self._ok = ok
        self._status = status
        self._data = data

    @property
    def ok(self):
        """
        Gets the success indicator of the response.

        Returns:
            bool: The success indicator of the response.
        """
        return self._ok

    @ok.setter
    def ok(self, value):
        """
        Sets the success indicator of the response.

        Args:
            value (bool): The new success indicator of the response.
        """
        self._ok = value

    @property
    def status(self):
        """
        Gets the HTTP status code of the response.

        Returns:
            int: The HTTP status code of the response.
        """
        return self._status

    @status.setter
    def status(self, value):
        """
        Sets the HTTP status code of the response.

        Args:
            value (int): The new HTTP status code of the response.
        """
        self._status = value

    @property
    def data(self):
        """
        Gets the response data in JSON format.

        Returns:
            dict: The response data in JSON format.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the response data in JSON format.

        Args:
            value (dict): The new response data in JSON format.
        """
        self._data = value

    def __str__(self):
        """
        Returns a string representation of the ResponseWrapper instance.

        Returns:
            str: A string representation of the ResponseWrapper instance.
        """
        return f"ResponseWrapper(ok={self._ok}, status={self._status}, data={self._data})"