class Utils:
    @staticmethod
    def get_tasks_name(elements):
        """
        Extracts the text from a list of web elements and returns it as a list of strings.

        :param elements: A list of web elements from which to extract text.
        :return: A list of strings, each representing the text of a corresponding web element.
        """
        # Extract and return the text from each element using map
        return list(map(lambda element: element.text, elements))
