# API Automation Framework

## Overview

This project is a Python-based API Automation Framework developed using Pytest and Requests. The framework follows a clean and maintainable structure with separate layers for API operations, test data, assertions, logging, and test cases.

The main objective of this project is to automate REST API testing, validate responses, verify business scenarios, and generate execution reports.

---

## Features

* API Automation using Python
* Pytest Framework
* Requests Library
* CRUD API Testing
* Reusable BaseAPI Design
* Custom Assertions
* Logging Support
* Test Data Management
* Pytest Fixtures
* Negative Test Scenarios
* Allure Reporting
* Jenkins CI/CD Integration
* Git and GitHub Version Control

---

## Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Programming Language   |
| Pytest     | Test Framework         |
| Requests   | API Testing            |
| Allure     | Test Reporting         |
| Jenkins    | Continuous Integration |
| Git        | Version Control        |
| GitHub     | Repository Management  |

---

## Project Structure

```text
API_Automation_Framework/
│
├── api/
│   ├── base_api.py
│   └── user_api.py
│
├── data/
│   └── test_data.py
│
├── tests/
│   ├── test_create_user.py
│   ├── test_get_user.py
│   ├── test_update_user.py
│   ├── test_delete_user.py
│   └── test_negative_scenarios.py
│
├── utils/
│   ├── assertions.py
│   ├── config.py
│   └── logger.py
│
├── reports/
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

## Framework Design

The framework follows a layered architecture.

### API Layer

Responsible for handling API requests and responses.

Files:

* base_api.py
* user_api.py

### Test Layer

Contains all test scenarios and validations.

Files:

* test_create_user.py
* test_get_user.py
* test_update_user.py
* test_delete_user.py
* test_negative_scenarios.py

### Data Layer

Stores reusable test data.

Files:

* test_data.py

### Utility Layer

Contains reusable utilities.

Files:

* logger.py
* assertions.py
* config.py

---

## Test Scenarios Covered

### Positive Scenarios

* Get User Details
* Create User
* Update User
* Delete User

### Negative Scenarios

* Invalid User Request
* Response Validation
* Status Code Validation

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd API_Automation_Framework
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Execute Test Suite

Run all tests:

```bash
pytest -v
```

Run specific test file:

```bash
pytest tests/test_get_user.py -v
```

---

## Generate Allure Reports

Generate report data:

```bash
pytest --alluredir=reports
```

Open report:

```bash
allure serve reports
```

---

## Jenkins Integration

This framework supports Jenkins CI/CD execution.

Pipeline Activities:

1. Pull latest code from GitHub
2. Install dependencies
3. Execute API test suite
4. Generate Allure Reports
5. Publish execution results

---

## Logging

Execution logs are captured during test execution for easier debugging and analysis.

Examples:

```text
INFO - Fetching User
INFO - User Created Successfully
INFO - Response Code: 200
INFO - Test Execution Completed
```

---

## Future Enhancements

* Environment Configuration (QA/UAT/PROD)
* Dynamic Test Data using Faker
* HTML Reporting
* API Schema Validation
* Docker Integration
* Scheduled Jenkins Execution

---

## Learning Outcomes

Through this project I gained hands-on experience in:

* API Automation Testing
* Python Programming
* Pytest Framework
* Requests Library
* Test Framework Design
* CI/CD Concepts
* Jenkins Integration
* Allure Reporting
* Git and GitHub

---

## Author

**Rakesh Jupally**

QA Automation Engineer

**Skills:**
- Python
- Selenium
- API Testing
- Pytest
- Jenkins
- Git & GitHub
