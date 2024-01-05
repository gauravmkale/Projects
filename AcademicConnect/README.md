# ACADEMIC CONNECT #
#### Video Demo:  https://youtu.be/g5OxXsHdWvU

Academic Connect is a web application that allows users to buy and sell academic resources such as books within a university community.We aim to make the students hard college life a breeze to go through. With academic connect you can get rid of your old books with ease and as a junior you can find all the books you will need in your course right at the convenience of your college.

## Features

- **Buy Resources:** Browse and buy academic resources listed by other users.
- **Sell Resources:** Sell your academic resources by providing details and uploading photos.
- **User Account:** Register, log in, and manage your user account.
- **Feedback:** Submit feedback and contact the administrators.
- **My Books:** View a list of resources you have listed for sale.
- **Password Management:** Change your password securely.

## Technologies Used

- Flask (Python web framework)
- SQLite (Database)
- Bootstrap (Front-end framework)
- werkzeug

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/academic-connect.git
    ```

2. Navigate to the project directory:

    ```bash
    cd academic-connect
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    flask run
    ```

5. Access the application in your web browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

1. Register for an account or log in if you already have one.
2. Browse available resources or list your own for sale.
3. Provide necessary details and upload photos when selling a resource.
4. View your listed resources on the "My Books" page.
5. Change your password or log out as needed.

## Contributing

If you would like to contribute to the project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

## Pages:

### 1. Home Page (index.html)
- **Description:** Welcome page providing a quick guide for users to navigate the platform.
- **URL:** `/`

### 2. About Us Page (about.html)
- **Description:** Information about Academic Connect's mission, vision, and the team behind the platform.
- **URL:** `/about`

### 3. Contact Us Page (contact.html)
- **Description:** Allows users to submit questions or provide feedback through a contact form.
- **URL:** `/contact`

### 4. Login Page (login.html)
- **Description:** User login form for accessing their accounts on Academic Connect.
- **URL:** `/login`

### 5. Register Page (register.html)
- **Description:** User registration form for creating a new account on Academic Connect.
- **URL:** `/register`

### 6. Account Page (account.html)
- **Description:** Displays user credentials, including username, year, and branch, with an option to change the password.
- **URL:** `/account`

### 7. Buy Page (buy.html)
- **Description:** Displays user credentials, including username, year, and branch, with an option to change the password.
- **URL:** `/buy`

### 8. Sell Page (sell.html)
- **Description:** Form for users to share their academic resources, including details like year, branch, resource type, book name, price, phone number, and a photo.
- **URL:** `/sell`

### 9. My Books Page (my.html)
- **Description:** Displays the books associated with the user's account, including details such as book name, photo, year, branch, resource type, price, and number of copies.
- **URL:** `/my`

### 10. Change Password Page (password.html)
- **Description:** Form for users to change their account password by providing the current password and entering a new one.
- **URL:** `/password`

## MySQL Database

### Overview

The MySQL database used in the Academic Connect project is designed to store essential information related to users and book listings. This document provides an overview of the database schema, including key tables, their fields, and relationships.

### Tables

### `users` Table

The `users` table stores information about registered users on Academic Connect.

**Fields:**

- `id` (Primary Key): Unique identifier for each user.
- `username`: User's username.
- `password`: Hashed password for secure storage.
- `year`: User's academic year.
- `branch`: User's academic branch.

### `books` Table

The `books` table contains details about academic resources listed by users for buying and selling.

**Fields:**

- `id` (Primary Key): Unique identifier for each book.
- `user_id` (Foreign Key): References the `id` field in the `users` table to establish a relationship.
- `bookname`: Name of the book or academic resource.
- `year`: Year of the book or resource.
- `branch`: Branch related to the book or resource.
- `resourcetype`: Type of resource (e.g., textbook, notes).
- `price`: Price of the book or resource.
- `number`: Number of copies available.
- `photo`: Path to the photo of the book.

# Academic Connect MySQL Database

## Overview

The MySQL database used in the Academic Connect project is designed to store essential information related to users and book listings. This document provides an overview of the database schema, including key tables, their fields, and relationships.

## Tables

### `Users` Table

The `users` table stores information about registered users on Academic Connect.

**Fields:**

- `id` (Primary Key): Unique identifier for each user.
- `username`: User's username.
- `password`: Hashed password for secure storage.
- `year`: User's academic year.
- `branch`: User's academic branch.

### `Books` Table

The `books` table contains details about academic resources listed by users for buying and selling.

**Fields:**

- `id` (Primary Key): Unique identifier for each book.
- `user_id` (Foreign Key): References the `id` field in the `users` table to establish a relationship.
- `bookname`: Name of the book or academic resource.
- `year`: Year of the book or resource.
- `branch`: Branch related to the book or resource.
- `resourcetype`: Type of resource (e.g., textbook, notes).
- `price`: Price of the book or resource.
- `number`: Number of copies available.
- `photo`: Path to the photo of the book.

### `Feedback` Table

The `Feedback` table stores user feedback on the Academic Connect platform.

**Fields:**

- `id` (Primary Key): Unique identifier for each feedback entry.
- `user_id` (Foreign Key): References the `id` field in the `users` table to identify the user providing feedback.
- `message`: User's feedback message.
- `rating`: Numeric rating given by the user.

## Relationships

- The `user_id` field in the `books` table establishes a relationship with the `id` field in the `users` table, linking each book entry to a specific user.

## Database Setup

To set up the Academic Connect MySQL database, follow these steps:

1. **Create a new MySQL database:**
   ```sql
   CREATE DATABASE academic_connect;

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- CS50 Team
- Flask Documentation
- Bootstrap Documentation
