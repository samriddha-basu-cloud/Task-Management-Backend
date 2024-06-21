# Task Management Application Back-End

![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0.2-000000?logo=Flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.35.4-003B57?logo=SQLite&logoColor=white)

## Overview

This repository contains the back-end code for a Task Management Application built using Flask. The API supports CRUD operations for managing tasks, including creating, retrieving, updating, and deleting tasks.

## Features

- Retrieve all tasks.
- Create a new task.
- Retrieve a single task by its ID.
- Update an existing task.
- Delete a task.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python](https://www.python.org/) (version 3.7 or later)
- [Flask](https://flask.palletsprojects.com/) (version 2.0 or later)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/samriddha-basu-cloud/Task-Management-Backend.git
    cd Task-Management-Backend
    ```

2. Set up a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```

The API will be available at `hhttps://task-management-backend-89n5.onrender.com:5000`.

## Project Structure

```
backend/
├── app/
│   ├── init.py
│   ├── models.py
│   └── routes.py
└── run.py
```


### Explanation of Files

- **run.py:** Entry point for the Flask application.
- **\_\_init\_\_.py:** Initializes the Flask application and sets up the database.
- **models.py:** Defines the Task model for the SQLite database.
- **routes.py:** Contains the API endpoints for task management.

## API Endpoints

- `GET /api/tasks` - Retrieve all tasks.
- `POST /api/tasks` - Create a new task.
- `GET /api/tasks/:id` - Retrieve a task by ID.
- `PUT /api/tasks/:id` - Update a task by ID.
- `DELETE /api/tasks/:id` - Delete a task by ID.

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

