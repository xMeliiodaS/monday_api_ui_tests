import random
import string


class Utils:
    """
    Utility class for common helper functions.
    """

    @staticmethod
    def generate_random_string(length=12):
        """
        Generates a random alphanumeric key of a specified length.

        :param length: The length of the random key to be generated (default is 12).
        :return: A random alphanumeric string of the specified length.
        """
        # Define the characters that can be used in the key
        characters = string.ascii_uppercase

        # Generate a random key
        random_key = ''.join(random.choice(characters) for _ in range(length))

        return random_key
