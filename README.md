# todo-guru

Website project by Oscar Sabet

## Table of Contents

- [todo-guru](#todo-guru)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Agile Planning](#agile-planning)
    - [UI Design](#ui-design)
      - [Wireframe](#wireframe)
    - [User Stories](#user-stories)
    - [Project board](#project-board)
  - [Database](#database)
    - [Interaction with Models](#interaction-with-models)
    - [Interaction with Templates](#interaction-with-templates)
    - [Explanation](#explanation)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Relationships](#relationships)
  - [Development](#development)
  - [Deployment](#deployment)
  - [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Features](#features)
  - [Key Features](#key-features)
  - [Site Contents](#site-contents)
    - [Templates](#templates)
  - [Repository](#repository)
  - [Sources](#sources)
  - [Full Screenshots](#full-screenshots)
    - [Home](#home)
    - [Task List](#task-list)
    - [Kanban Board](#kanban-board)
    - [Profile](#profile)
  - [Validation](#validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Python](#python)
    - [Create New Task](#create-new-task)

## Introduction

ToDo|Guru is task management application coded in html/css, utilising the bootstrap framework, and python using the django framework.

The application provides a scalable & modern interface which allows users to manage their tasks easily and contains advanced features which allow users to organise & filter tasks.

![ToDo|Guru Site](readme/demo.png)

## Agile Planning

This project utilised an agile methodoligy for the project. making use of user stories, wireframes and a kanban board.

### UI Design

The application provides a scalable & modern interface which uses pastel colours and rounded corners.

#### Wireframe

Wireframes are a crucial part of the UI/UX design process. They are simple, low-fidelity sketches or digital illustrations that outline the basic structure and layout of a web page or application. Wireframes help to visualize the placement of elements on the page and provide a clear blueprint for the design and development process.

![ToDo|Guru Wireframe](readme/wireframe-desktop-list.png)

This wireframe provides a visual representation of the layout for the ToDo|Guru task list page. It outlines the placement of elements such as the sidebar, task list, and task details.

By using wireframes, the ToDo|Guru application ensures that the design and development process is well-planned and focused on delivering a user-friendly interface.

### User Stories

User stories are a key component of agile development methodologies. They are short, simple descriptions of a feature or functionality told from the perspective of the end user. User stories help to capture the requirements of the application in a way that is easy to understand and communicate. They focus on the value that the feature will bring to the user and provide a basis for planning, development, and testing.

```text
As a user, I want to create a new task so that I can keep track of my to-dos.
```

This user story captures the requirement for the task creation feature. It describes what the user wants to do (create a new task) and why it is important (to keep track of to-do items).

By using user stories, the ToDo|Guru application ensures that the development process is user-centered and focused on delivering value to the end user.

### Project board

A Kanban board is a visual tool used in Agile project management to visualize the flow of work and manage tasks efficiently. It consists of columns representing different stages of the workflow, and cards representing individual tasks. The Kanban board helps teams to track the progress of tasks, identify bottlenecks, and ensure a smooth flow of work.

![ToDo|Guru Kanban Board](readme/kanban.png)
[Github Project Board](https://github.com/users/oscar-sabet/projects/4)

This Kanban board provides a visual representation of the workflow for the ToDo|Guru application. 

It includes columns for different stages, `To Do` `In Progress` and `Done`. It also uses the labels `could-have`, `should-have` and `must-have` to prioritise tasks. The cards representing individual tasks.

By using a Kanban board, the ToDo|Guru application ensures that the development process is well-organized and focused on delivering value to the end user.

The Kanban board is closely related to Agile methodologies, which emphasize iterative development, continuous improvement, and collaboration. In Agile, the Kanban board is used to manage tasks and ensure a smooth flow of work. It helps teams to visualize the workflow, manage work in progress, and track progress, all of which are key principles of Agile.

## Database

ToDo|Guru uses PostgreSQL as its primary database. PostgreSQL is a powerful, open-source relational database management system that provides robust data storage and retrieval capabilities.

### Interaction with Models

In Django, models are Python classes that define the structure of your database tables. Each model maps to a single table in the database. For example, the `Task` model defines the structure of the `tasks` table, including fields such as `title`, `description`, `status`, `priority`, and `due_date`. When you create, update, or delete a model instance, Django interacts with the PostgreSQL database to perform the corresponding SQL operations.

### Interaction with Templates

Django templates are used to render HTML pages dynamically. When you query the database for model instances (e.g., retrieving a list of tasks), the data is passed to the template context. The template then uses this data to generate the HTML content. For example, the task list page retrieves tasks from the database and displays them in a structured format using the template.



### Explanation

![Task Model](readme/task-model.png)

1. **User Model**:
   - This is the built-in Django `User` model which includes fields like `id`, `username`, `email`, and `password`. 

2. **Profile Model**:
   - `Profile` has a one-to-one relationship with the `User` model.
   - Fields:
     - `user`: A one-to-one field linking to the `User` model.
     - `profile_picture`: A Cloudinary field for storing profile pictures.

3. **Task Model**:
   - `Task` has a many-to-one relationship with the `User` model.
   - Fields:
     - `title`: A character field for the task title.
     - `description`: A text field for the task description.
     - `status`: A character field with choices for task status.
     - `created`: A datetime field for when the task was created.
     - `due_date`: A datetime field for the task's due date.
     - `completed_date`: A datetime field for when the task was completed.
     - `priority`: A character field with choices for task priority.
     - `category`: A character field with choices for task category.
     - `user`: A foreign key linking to the `User` model.

### Entity Relationship Diagram (ERD)

![ToDo|Guru Wireframe](readme/erd.png)

### Relationships

- **User to Profile**: One-to-One relationship.
- **User to Task**: One-to-Many relationship.

This ERD provides a visual representation of the relationships between the models in your Django project.

## Development

## Deployment

Deploying the application to heroku involved several steps.

1. **Preparing my project for heroku**
   - My project was uploaded to a github repository
   - Gunicorn was installed and configured
   - ensure all dependencies are listed in `requirements.txt` and the python version is listed in `.python-version`
   - configure static files and settings.py, paying special attention to disabling debugging and any other settings related to security.
   - set up and configure environmental files eg. `env.py`
   - create a `Procfile`. This file tells Heroku how to run your application.
   - ensure that any files that contain secret keys or other sensitive information eg. `env.py` is added to `.gitignore` and is not present in your github repo
  
2. **Deploying to Heroku**
   - Create heroku app
   - Link github repository & Code Institute PostGres database
   - Add environmental variables to heroku, such as, secret keys.
   - Deploy the application

## Testing

## Manual Testing

| **Feature**               | **Test Case**                                                                                       | **Expected Result**                                                                                       | **Result**                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **User Registration**     | Navigate to the registration page. Fill in the form with valid details and submit.                  | User is registered and redirected to the login page.                                                      |PASS                                                                                                     |
|                           | Attempt to register with an existing username or email.                                             | Appropriate error message is displayed.                                                                   |PASS                                                                                                     |
| **User Login**            | Navigate to the login page. Fill in the form with valid credentials and submit.                     | User is logged in and redirected to the task list page.                                                   |PASS                                                                                                     |
|                           | Attempt to log in with invalid credentials.                                                         | Appropriate error message is displayed.                                                                   |PASS                                                                                                     |
| **User Logout**           | While logged in, click the logout button.                                                           | User is logged out and redirected to the login page.                                                      |PASS                                                                                                     |
| **Create Task**           | Click the "New Task" button. Fill in the form with valid details and submit.                        | Task is created and displayed in the task list.                                                           |PASS                                                                                                     |
| **Update Task**           | Click the "Update" button for an existing task. Modify the details and submit.                      | Task is updated and changes are reflected in the task list.                                               |PASS                                                                                                     |
| **Delete Task**           | Click the "Delete" button for an existing task. Confirm the deletion in the modal.                  | Task is removed from the task list.                                                                       |PASS                                                                                                     |
| **Mark Task as Completed**| Click the checkbox to mark a task as completed.                                                     | Task status is updated to "Completed" and visually distinguished from other tasks.                        |PASS                                                                                                     |
| **Filter Tasks by Status**| Use the status filter to display tasks with a specific status (Pending, In Progress, Completed).    | Only tasks with the selected status are displayed.                                                        |PASS                                                                                                     |
| **Filter Tasks by Category**| Use the category filter to display tasks with a specific category (Work, Personal, Home).         | Only tasks with the selected category are displayed.                                                      |PASS                                                                                                     |
| **Filter Tasks by Priority**| Use the priority filter to display tasks with a specific priority (Low, Medium, High).            | Only tasks with the selected priority are displayed.                                                      |PASS                                                                                                     |
| **Sort Tasks**            | Use the sort options to sort tasks by created date, due date, status, category, and priority.       | Tasks are sorted correctly based on the selected criteria.                                                |PASS                                                                                                     |
| **View Profile**          | Navigate to the profile page.                                                                       | User's profile information (username, email, profile picture) is displayed correctly.                     |PASS                                                                                                     |
| **Update Profile Picture**| On the profile page, upload a new profile picture.                                                  | Profile picture is updated and displayed correctly.                                                       |PASS                                                                                                     |

## Features

## Key Features

1. **User Authentication**:
   - Secure user registration and login.
   - User-specific task management.

2. **Task Management**:
   - Create, update, and delete tasks.
   - Mark tasks as completed.
   - Filter tasks by status, category, and priority.
   - Sort tasks by created date, due date, status, category, and priority.

3. **Task Details**:
   - Add detailed descriptions to tasks.
   - Set due dates for tasks.
   - Track task creation and completion dates.
   - Calculate time taken to complete tasks and time until due.

4. **Task Categories and Priorities**:
   - Categorize tasks as Work, Personal, or Home.
   - Set task priorities as Low, Medium, or High.

5. **User Profile**:
   - Upload and display profile pictures using Cloudinary.
   - View user-specific task statistics.

6. **Responsive Design**:
   - Mobile-friendly and responsive user interface.
   - Use of Bootstrap for styling and layout.

7. **Real-time Updates**:
   - Use of modals for creating and deleting tasks without page reloads.
   - Real-time task status updates.

8. **Custom Filters and Sorting**:
   - Custom filters for task status, category, and priority.
   - Sorting options for better task management.
   - Template tags used to display datetime in more readable format.

9. **Statistics and Insights**:
   - View task statistics such as total tasks, completed tasks, pending tasks, and tasks in progress.
   - Breakdown of tasks by priority.

10. **Django Admin Integration**:
    - Manage tasks and users through the Django admin interface.
  
- Task creation, editing, and deletion
- Task status, priority, and category management
- Due date setting 
- Project board (kanban) view
- User accounts with profile pictures

## Site Contents

### Templates

The site uses multiple templates
apps

toast alerts

## Repository

The Github repo can be found here.

[Github Repo](https://github.com/oscar-sabet/todo-guru)

The project Board can be found here.

[Github Project Board](https://github.com/users/oscar-sabet/projects/4)

The deployed Heroku project link can be found here.

[Deployed Link](https://todo-guru-2-3e966323d05c.herokuapp.com/)

## Sources

Guru logo - https://www.flaticon.com/free-icon/guru_3174915?term=guru&page=1&position=1&origin=tag&related_id=3174915

## Full Screenshots

### Home

![Home Desktop](readme/Screenshots/home-dt.png)
![Home Mobile](readme/Screenshots/todo-guru-2-3e966323d05c.herokuapp.com_.png)

### Task List

![Task List Desktop](readme/Screenshots/task-dt.png)
![Task List Mobile](readme/Screenshots/task-mob.png)

### Kanban Board

![Kanban Board Desktop](readme/Screenshots/board.png)
![Kanban Board Mobile](readme/Screenshots/board-mob.png)

### Profile

![Profile Desktop](readme/Screenshots/account.png)
![Profile Mobile](readme/Screenshots/profil-mob.png)

## Validation

### HTML

### CSS

### Python

### Create New Task

how you used ai for automated tests (using automated tests optional)