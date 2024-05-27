# Test-Amadeus🚀
Practical QA engineering test for Amadeus company 

Part 1: Test Planning and Test Case Design

Scenario: You are assigned to test a new feature in a software application. The feature involves an API endpoint ( https://api.restful-api.dev/objects ) that allows users to list their registered phones. The endpoint returns data in JSON format and supports GET requests.

Task:

1. Test Plan Creation: Write a brief test plan for validating this new feature. Your test plan should include:

· Scope

· Objectives

· Test strategy

2. Test Case Design: Design 5 test cases for this API endpoint. Each test case should include:

· Test case ID

· Test description

· Pre-conditions

· Test steps

· Expected results

Deliverable: Submit the test plan and the 5 test cases.

Part 2: API Testing and Scripting

Scenario: You need to verify the functionality of the given API endpoint using Python. The endpoint URL is https://api.restful-api.dev/objects

Task:

1. Write a Python script that:

· Sends a GET request to the API endpoint.

· Validates the response status code is 200.

· Checks that the response body contains the expected keys

2. Modify the script to handle a scenario where the API returns a 404 status code and log an appropriate error message.

Deliverable: Submit the Python script.

Part 3: Defect Tracking

Scenario: During testing, you discover that the API endpoint occasionally returns a 500 status code when the user data is not found, instead of the expected 404 status code.

Task:

1. Defect Report: Write a defect report for this issue. Your report should include:

· Defect ID

· Title

· Description

· Steps to reproduce

· Expected result

· Actual result

· Severity

· Priority

Deliverable: Submit the defect report.

HOW TO RUN:

This project contains a Python script that performs unit tests to validate the responses of a RESTful API. Below are the steps to run the script, along with an explanation of the libraries used and the script's functionality.

## Requirements

- Python 3.x
- `requests` library
- 'unittest' library

## Execution

1. **Clone the repository or download the script**: Ensure you have the script file on your system.

2. **Navigate to the script directory**: Open a terminal and navigate to the directory where the script is located. For example:
    ```sh
    cd /C:\Users\lisda\Desktop\Python\main.py/to/directory
    ```

3. **Run the script**: Execute the following command to run the unit tests:
    ```sh
    python script_main.py
    ```

## Libraries Used

- `unittest`: A standard Python library that provides a framework for creating and running unit tests.
- `requests`: A Python library that allows you to send HTTP requests easily.

## Script Description

The script performs unit tests to validate the responses of a RESTful API. 

1. **Importing Libraries**:
    ```python
    import unittest
    import requests
    ```

2. **Defining the Test Class**:
    ```python
    class AmadeusTestChallenge(unittest.TestCase):
    ```

3. **`setUp` Method**: This method runs before each test. It defines the base URL of the API and the expected keys in the response.
    ```python
    def setUp(self):
        self.url = 'https://api.restful-api.dev/objects'
        self.expected_keys = ['id', 'name', 'data']
    ```

4. **`test_validate_response_success` Test**: This test checks that the API response has a status code of 200 and that each object in the response contains the expected keys.
    ```python
    def test_validate_response_success(self):
        self.expected_status_code = 200
        response = requests.get(self.url)
        devices = response.json()
        self.assertEqual(response.status_code, self.expected_status_code, 'Expected status code: 200')
        for device in devices:
            for expected_key in self.expected_keys:
                self.assertIn(expected_key, device, f"Missing expected key '{expected_key}' in response")
    ```

5. **`test_validate_response_not_found` Test**: This test checks that a request to an invalid URL returns a status code of 404.
    ```python
    def test_validate_response_not_found(self):
        self.modified_url = self.url + 'invalid'
        self.expected_status_code = 404
        response = requests.get(self.modified_url)
        self.assertEqual(response.status_code, self.expected_status_code, 'Expected status code: 404')
    ```

6. **Running the Tests**: This block allows the tests to be run when the script is executed directly.
    ```python
    if __name__ == '__main__':
        unittest.main()
    ```
