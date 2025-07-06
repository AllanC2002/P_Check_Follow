# Chechk Follow Microservice

This project is a Python-based backend service built with Flask. It provides an API endpoint to check if two users mutually follow each other. The application interacts with a MySQL database to store and retrieve user and follower information.

## Folder Structure

The project follows a structured layout to separate concerns:

-   **`.github/workflows/`**: Contains GitHub Actions workflow files for CI/CD, specifically for publishing Docker images (`docker-publish.yml`, `docker-publish_qa.yml`).
-   **`infrastructure/`**: Holds code related to external systems and frameworks.
    -   **`infrastructure/db/`**: Manages database interactions.
        -   `mysql_connection.py`: Provides functions to connect to the MySQL database using SQLAlchemy.
        -   `mysql_models.py`: Defines SQLAlchemy ORM models (`Profile`, `Followers`) for database tables.
-   **`interface/`**: Handles interactions with the outside world, primarily API requests.
    -   **`interface/controllers/`**: Contains API route handlers (controllers).
        -   `follow_controller.py`: Defines the `/check-follow` API endpoint.
-   **`tests/`**: Includes test files for the application.
    -   `test.py`: Contains integration tests for the API endpoint, using the `requests` library.
-   **`use_cases/`**: Contains the core business logic of the application, independent of web frameworks or databases.
    -   `check_mutual_follow.py`: Implements the logic to determine if two users have a mutual follow relationship.

**Root Directory Files:**

-   `app.py`: The main Flask application entry point. It initializes the Flask app and registers blueprints.
-   `dockerfile`: Instructions for building a Docker image for the application.
-   `requirements.txt`: Lists the Python dependencies required for the project.
-   `.gitignore`: Specifies intentionally untracked files that Git should ignore.

## Backend Design Pattern

The application is structured following the principles of **Clean Architecture** (also related to Hexagonal or Onion Architecture). This pattern emphasizes a separation of concerns, making the system more testable, maintainable, and flexible.

Key aspects:
-   **Entities (Implicit)**: While not explicitly defined as separate files in this context, the SQLAlchemy models in `infrastructure/db/mysql_models.py` represent the data structures (Entities like `Profile`, `Followers`).
-   **Use Cases**: Located in the `use_cases/` directory (e.g., `check_mutual_follow.py`). These contain the application-specific business rules and are independent of any framework or UI.
-   **Interface Adapters**:
    -   Controllers (`interface/controllers/follow_controller.py`) adapt incoming HTTP requests to calls to the Use Cases.
-   **Frameworks & Drivers (Infrastructure)**:
    -   The Flask framework (`app.py`) for web serving.
    -   Database interaction logic (`infrastructure/db/mysql_connection.py` and `mysql_models.py`) using SQLAlchemy.

The core principle is the **Dependency Rule**: source code dependencies can only point inwards. Use Cases are at the center and have no dependencies on outer layers like Interfaces or Infrastructure. This makes the business logic reusable and independent of delivery mechanisms or data storage details.

## Communication Architecture

The primary communication architecture is a **synchronous RESTful API** over HTTP.

1.  **Client Request**: A client (e.g., a frontend application, testing script) sends an HTTP request to one of the defined API endpoints.
2.  **API Gateway (Flask)**: The Flask application (`app.py`) receives the request.
3.  **Controller**: The request is routed to the appropriate controller in `interface/controllers/` (e.g., `follow_controller.py`). The controller parses the request (e.g., JSON body).
4.  **Use Case Execution**: The controller calls the relevant function in the `use_cases/` directory, passing the necessary data. This is a direct, synchronous function call.
5.  **Data Access**: The use case interacts with the database through the `infrastructure/db/` layer (e.g., calling `get_userprofile_session()` and using SQLAlchemy models). This is also a synchronous operation.
6.  **Response Generation**: The use case returns its result to the controller.
7.  **HTTP Response**: The controller formats the result into an HTTP response (typically JSON) and sends it back to the client.

All interactions within the application stack (Controller -> Use Case -> Database) are synchronous function calls.

## API Endpoints

### Check Mutual Follow

-   **Path**: `/check-follow`
-   **Method**: `POST`
-   **Description**: Checks if two users mutually follow each other.
-   **Request Body (JSON)**:
    ```json
    {
        "id_user_1": "<integer>",
        "id_user_2": "<integer>"
    }
    ```
    -   `id_user_1`: (Integer) The ID of the first user.
    -   `id_user_2`: (Integer) The ID of the second user.

-   **Responses**:
    -   **200 OK (Success)**: Indicates a successful check.
        ```json
        {
            "mutual": true|false
        }
        ```
        -   `mutual`: (Boolean) `true` if the users mutually follow each other, `false` otherwise.

    -   **400 Bad Request (Missing Fields)**: If `id_user_1` or `id_user_2` is not provided in the request body.
        ```json
        {
            "error": "Missing required fields"
        }
        ```

    -   **400 Bad Request (Invalid User IDs)**: If `id_user_1` or `id_user_2` cannot be converted to integers.
        ```json
        {
            "error": "Invalid user IDs"
        }
        ```
