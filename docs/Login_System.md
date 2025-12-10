# Login System

This document outlines the login process for the N-Queen Visualizer application, including the requirements for creating a secure password and understanding user feedback messages.

## Accessing the Login Page

The login page is the entry point for accessing user-specific functionalities within the application. You will typically be redirected to this page if you attempt to access protected resources without being authenticated.

## Login Process

To log in, you will need to provide your registered username and password.

### Input Fields

*   **Username**: Enter your registered username.
*   **Password**: Enter your corresponding password.

After entering your credentials, click the 'Login' button.

## Password Validation Requirements

For security purposes, all passwords must adhere to the following strict validation rules:

*   **Minimum Length**: Your password must be at least 8 characters long.
*   **Uppercase Letter**: Must contain at least one uppercase letter (A-Z).
*   **Lowercase Letter**: Must contain at least one lowercase letter (a-z).
*   **Number**: Must contain at least one digit (0-9).
*   **Special Character**: Must contain at least one special character (e.g., !, @, #, $, %, ^, &, *).

If your password does not meet these criteria during registration or a password change, you will receive an error message.

## User Feedback

The application provides clear user feedback through toast messages at the top of the screen:

*   **Successful Login**: A success message will appear, confirming that you have been successfully logged in.
*   **Login Failure**: If there is an issue with your credentials (e.g., incorrect username or password, or if your account does not exist), an error message will be displayed, indicating the reason for the failure. Please review your input and try again.
*   **Validation Errors**: If your password input does not meet the validation requirements during registration or other password-related operations, specific error messages will guide you on what needs to be corrected.

## Example User Flow

1.  Navigate to the login page.
2.  Enter your username.
3.  Enter your password (e.g., `SecureP@ss1`).
4.  Click 'Login'.
5.  Receive a 'Login successful!' toast message if credentials are correct.
6.  If credentials are incorrect or password validation fails, an appropriate error toast message will appear.
