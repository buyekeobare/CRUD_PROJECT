# CRUD PROJECT

This is a CRUD Project on student management system built using **Django 4** and **HTML 5**

## Table of Contents

- [Objectives](#objectives)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)

## Objectives

- Create a Django web application that allows you to perform CRUD (Create, Read, Update, Delete) operations for managing student records.
- No need to style.
- Just create a simple table.

### Prerequisites

Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
   <br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Visual Studio Code](https://code.visualstudio.com/download)

### Installation

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory, run:

On macOS:

```bash
source env/bin/activate
```

On Windows:

```bash
env\scripts\activate
```

#### 3. Install django

From the **root** directory, run:

```bash
pip pip install django
```

#### 4. Start a new Project

From the **root** directory, run:

```bash
django-admin startproject student_records
```

#### 5. Ceate django app

From the **root** directory, run:

```bash
cd student_records
```

```bash
python manage.py startapp students
```

#### 6. Add the App to Installed Apps:

- In students_records/settings.py, add 'students' to the INSTALLED_APPS list.
  ![Apps](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/student_records/settings.py)

#### 7. Define the Student Model

- Edit students/models.py
  ![Apps](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/students/models.py)

#### 8. Run migrations

From the **root** directory, run:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

#### 9. Create an admin user to access the Django Admin interface

From the **root** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.

#### 10. Create CRUD Views

- Edit students/views.py to add views for each CRUD operation

![views](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/students/views.py)

#### 11. Create URLs

- Edit students/urls.py and define URL patterns
  ![Students urls](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/students/urls.py)

- Include the app URLs in the main project urls.py
  ![Main urls](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/student_records/urls.py)

#### 12. Create Templates

- Create simple templates for each view
  ![Templates](https://github.com/buyekeobare/CRUD_PROJECT/tree/main/student_records/students/templates/students)

#### 13. Create a StudentForm

- Create a form for the Student model in students/forms.py
  ![StudentForm](https://github.com/buyekeobare/CRUD_PROJECT/blob/main/student_records/students/forms.py)

### Run the application

From the **root** directory, run:

```bash
python manage.py runserver
```

### View the application

Go to http://127.0.0.1:8000/ to view the application.
