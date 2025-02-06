User Management API with Flask

Project Overview

This project is a RESTful API developed using the Flask framework. It enables users to perform various operations such as creating, retrieving, updating, and deleting user information from a database. The API is structured for ease of maintenance and scalability, with robust error handling to ensure smooth operation.

Key Features
Create User: Add new users to the database.
Fetch All Users: Retrieve all user records stored in the database.
Fetch a Single User: Get detailed information about a specific user by their unique ID.
Update User: Modify user information based on provided data.
Delete User: Remove user data from the database.

Project Structure
Main Application: The central file that runs the application and handles route definitions.
Repository Layer: Manages all database operations for user data.
Database Configuration: Handles database connection and setup.
Data Models: Defines the structure for user creation and update requests.
Templates: HTML files used for rendering the user interface.

Setup Instructions
1. Clone the Project: Download the project files to your local machine.
2. Create a Virtual Environment: Set up an isolated environment for the project dependencies.
3. Install Dependencies: Download and install the required packages listed in the project.
Running the Application
To run the application, start the development server and access it through the provided URL. Ensure that all necessary configurations are complete before launching the server
API Endpoints
Home: The main page that renders a survey form.
Create User: Allows the creation of new user records.
Fetch All Users: Retrieves all users from the database.
Fetch a Single User: Fetches data for a specific user using their unique identifier.
Update User: Updates the information of an existing user.
Delete User: Deletes a user record from the database.

Sample API Usage
Creating a User: Provide necessary details such as name, email, and age to add a new user successfully.
Fetching Users: Retrieve either all users or a single user's details.
Updating User Data: Modify existing user information by sending updated details.
Deleting a User: Remove a user's information from the database when no longer needed.

Error Handling
The application is designed to handle common errors gracefully, such as:
Bad Request: Occurs when required data is missing or invalid.
Database Errors: Triggered when there are issues with database interactions.

Dependencies
The project uses essential libraries and frameworks, including:
Flask: For handling web requests and responses.
Werkzeug: A utility for managing HTTP and WSGI interactions.
Markupsafe: Provides string escaping for enhanced security.
License
This project is open-source and available under the MIT License.
