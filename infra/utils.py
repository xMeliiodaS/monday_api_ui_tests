import random
import string


class Utils:
    """
    Utility class for common helper functions.
    """

    @staticmethod
    def generate_random_key(length=8):
        # Define the characters that can be used in the key
        characters = string.ascii_letters + string.digits

        # Generate a random key
        random_key = ''.join(random.choice(characters) for _ in range(length))

        return random_key

