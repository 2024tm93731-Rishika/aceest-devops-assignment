# Aceest Application

This project is a Flask REST API for ACEest Functional Fitness integrated with a complete CI/CD workflow using Jenkins and GitHub Actions. It supports management of fitness programs, client data, workout logs, and progress tracking, and is packaged with Docker for consistent deployment across environments.

### Project Structure:
```
aceest-devops
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_app.py
│
├── .github/workflows/
│   └── main.yml
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── app.py
└── README.md
```

### Prerequisites
1. Python 3.9+ (3.12 recommended)
2. pip
3. Docker (for containerized runs)

### Local Setup Instructions:
1. Clone Repository
    ```bash
    git clone https://github.com/2024tm93731-Rishika/aceest-devops.git
    cd aceest-devops
    ```
2. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
3. Run Application
    ```bash
    python app.py
    ```
4. Open browser:
    ```bash
    http://localhost:5000
    ```

### Running Tests:
1. Run unit tests using Pytest:
    ```bash
    pytest
    ```
2. Expected output:
    12 passed

### Docker Containerization:
1. Build Docker Image
    ```bash
    docker build -t aceest-api .
    ```
2. Run Container
    ```bash
    docker run -p 5000:5000 aceest-api
    ```
3. Application will be accessible at:
    ```bash
    http://localhost:5000
    ```

### API Endpoints
| Endpoint         | Method | Description                                                                                      |
| ---------------- | ------ | ------------------------------------------------------------------------------------------------ |
| `/`              | GET    | Returns a simple message confirming the ACEest Fitness API service is running.                   |
| `/programs`      | GET    | Retrieves the available fitness programs and their associated calculation factors.               |
| `/clients/add`   | POST   | Adds a new client with name, age, height, and weight to the database.                            |
| `/clients`       | GET    | Retrieves the list of all registered clients stored in the system.                               |
| `/progress/add`  | POST   | Records weekly progress adherence data for a specific client.                                    |
| `/progress`      | GET    | Retrieves all recorded progress tracking entries for clients.                                    |
| `/workouts/add`  | POST   | Logs a workout session for a client including date, type, duration, and notes.                   |
| `/workouts`      | GET    | Retrieves all logged workout sessions from the database.                                         |
| `/metrics/add`   | POST   | Stores body metrics for a client such as weight, waist measurement, and body fat percentage.     |
| `/metrics`       | GET    | Retrieves all recorded body metric entries for clients.                                          |
| `/bmi/<name>`    | GET    | Calculates and returns the BMI value for the specified client based on stored height and weight. |
| `/analytics`     | GET    | Calculates and returns overall analytics such as the average client adherence score.             |
| `/report/<name>` | GET    | Generates a downloadable PDF report containing the client’s stored personal information.         |

### Jenkins CI/CD Pipeline:
Jenkins is used as a secondary CI/CD system to validate builds in a controlled environment.
Pipeline stages:
Jenkins CI/CD Pipeline
| Stage                    | Purpose                      |
| ------------------------ | ---------------------------- |
| Checkout SCM             | Pull code from GitHub        |
| Install Dependencies     | Install project dependencies |
| Run Tests                | Execute unit tests           |
| Build Docker Image       | Build application container  |
| Run Docker Container     | Pipeline completion status   |

### Docker Deployment:
Once tests pass, Jenkins builds a Docker image and runs the application container.
    ```bash
    docker build -t aceest-api .
    docker run -p 5000:5000 aceest-api
    ```

### Technologies Used:
| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| Python         | Application development      |
| Flask          | Web framework                |
| Pytest         | Unit testing                 |
| Flake8         | Code linting                 |
| Docker         | Containerization             |
| GitHub Actions | CI automation                |
| Jenkins        | CI/CD pipeline orchestration |
| Git            | Version control              |