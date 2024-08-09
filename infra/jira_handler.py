from jira import JIRA

from infra.config_provider import ConfigProvider


class JiraHandler:

    def __init__(self):
        """
        Initializes JiraHandler with configuration and JIRA authentication details.
        """
        self.config = ConfigProvider().load_config_json()
        self.config_secret = ConfigProvider().load_secret_json()
        self._jira_url = self.config['jira_url']
        self.auth_jira = JIRA(
            basic_auth=(self.config['jira_email'],
                        self.config_secret['jira_token']),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        """
        Creates a new issue in JIRA with the specified details.

        :param project_key: The key of the project where the issue will be created.
        :param summary: A brief summary of the issue.
        :param description: A detailed description of the issue.
        :param issue_type: The type of the issue (e.g., "Bug", "Task"). Default is "Bug".
        :return: The created JIRA issue.
        """
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        return self.auth_jira.create_issue(fields=issue_dict)
