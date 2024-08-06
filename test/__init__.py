class Utils:
    @staticmethod
    def get_tasks_name(elements):
        # Extract and return the text from each element using map
        return list(map(lambda element: element.text, elements))
