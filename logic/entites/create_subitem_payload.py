import json

from infra.utils import Utils


class CreateSubitemPayload:
    def __init__(self, parent_item_id):
        """
        Initializes CreateSubitemPayload with the given parent item ID and a randomly generated item name.

        :param parent_item_id: The ID of the parent item.
        """
        self.parent_item_id = parent_item_id

        self._name = None
        self.set_name()  # Set the name using the setter method

    @property
    def name(self):
        """
        Gets the name of the subitem.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the subitem.
        """
        self._name = value

    def set_name(self):
        """
        Sets the name of the subitem to a randomly generated key.
        """
        self.name = Utils.generate_random_string()

    def to_graphql(self) -> dict:
        """
        Converts the CreateSubitemPayload instance to a GraphQL mutation query.

        :return: A dictionary with the GraphQL mutation query for creating a subitem.
        """
        query = (
            f'mutation {{ create_subitem (parent_item_id: {self.parent_item_id}, '
            f'item_name: "{self.name}") {{ id board {{ id }} }} }}'
        )
        return {"query": query}
