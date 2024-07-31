# employee_auth.py

class EmployeeAuth:
    def __init__(self):
        # Initialize a dictionary to store employee credentials
        self.employees = {
            "john_doe": "password123",
            "jane_doe": "password456"
        }

    def authenticate(self, username, password):
        """
        Validate user credentials against stored data.

        Args:
            username (str): Employee username.
            password (str): Employee password.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        if username in self.employees and self.employees[username] == password:
            return True
        return False

    def login(self, username, password):
        """
        Attempt to log in with the provided credentials.

        Args:
            username (str): Employee username.
            password (str): Employee password.

        Returns:
            str: Success message if credentials are valid, error message otherwise.
        """
        if self.authenticate(username, password):
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password. Please try again."

    def register(self, username, password):
        """
        Register a new employee with the provided credentials.

        Args:
            username (str): Employee username.
            password (str): Employee password.

        Returns:
            str: Success message if registration is successful, error message otherwise.
        """
        if username not in self.employees:
            self.employees[username] = password
            return f"Employee '{username}' registered successfully!"
        else:
            return "Username already exists. Please choose a different username."


def main():
    auth = EmployeeAuth()

    while True:
        print("Employee Management System")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print(auth.login(username, password))
        elif choice == "2":
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            print(auth.register(username, password))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()