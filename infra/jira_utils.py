from infra.jira_handler import JiraHandler


class JiraUtils:
    def __init__(self):
        self.jira_handler = JiraHandler()

    def create_issue(self, test_case_name, error_message):
        """
        Creates a JIRA issue when a test case fails.

        :param test_case_name: The name of the test case that failed.
        :param error_message: The error message from the test failure.
        """
        summary = f"{test_case_name} failed"
        description = f"Test case: {test_case_name}\nError: {error_message}"
        self.jira_handler.create_issue('AT', summary, description)
