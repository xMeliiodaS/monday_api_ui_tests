# Monday.com Testing Framework

## Overview

This project involves testing the Monday.com website using a combination of UI and API tests. The framework is designed to ensure the functionality and reliability of various features on the Monday.com platform. It includes setup for testing boards, tasks, and user interactions.

## Features

- **UI and API Testing:** Comprehensive testing of Monday.com functionalities.
- **JIRA Integration:** Automated issue creation for failed test cases.
- **Allure Reporting:** Detailed test results and reports with links to Allure.

## Prerequisites

- Python 3.x
- Selenium WebDriver
- JIRA API access
- Allure framework

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/xMeliiodaS/monday_api_ui_tests.git
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have the required configuration files:**

   - `config.json`: Contains general configuration details.
   - `secret.json`: Contains sensitive information such as JIRA authentication tokens.

## Configuration

1. **Configure JIRA Integration:**

   Update `config.json` with your JIRA URL and email:

   ```json
   {
     "jira_url": "https://your-jira-instance.atlassian.net",
     "jira_email": "your-email@example.com"
   }
   ```

   Update `secret.json` with your JIRA API token:

   ```json
   {
     "jira_token": "your-jira-api-token"
   }
   ```

## Usage
1. **Install Allure:**

   ```bash
   pip pip install allure-pytest

   ```
   
2. **Running Tests:**

   To run all tests, use:

   ```bash
   python -m pytest --alluredir allure-results
   ```

3. **Generating Reports:**

   After running the tests, generate Allure reports:

   ```bash
   allure serve <allure-results-directory>
   ```

## Test Cases

- **Create Task:** Tests creation of new default tasks via API.
- **Delete Task:** Tests the deletion of tasks via API.
- **Sort Tasks:** Verifies sorting functionality for tasks by name.
- **Add/Remove Board Favorites:** Tests adding and removing boards from favorites.
- **Search Tasks:** Tests the search functionality for tasks.

## Error Handling

On test failures, a JIRA issue is created with the following details:

- **Summary:** Descriptive title of the test failure.
- **Description:** Detailed error message with a link to the Allure report.

## Code Structure

- `jira_handler.py`: Handles JIRA issue creation.
- `api_wrapper.py`: Provides API request functionality.
- `default_item_payload.py`: Defines payloads for default item tasks.
- `delete_item_payload.py`: Defines payloads for deleting tasks.
- `create_item.py`: Contains logic for creating tasks.
- `delete_item.py`: Contains logic for deleting tasks.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
