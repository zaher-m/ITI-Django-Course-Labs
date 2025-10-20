# ITI Django Course Labs

A collection of Django labs built as part of ITI's Django course.

## Labs

<details>
<summary>Day 01: Introduction to Django</summary>

- Introduction to the Django framework
- Creating a simple "Hello, World!" application
- Understanding Models, Views, and Templates (MVT)
- Setting up a basic project structure with two apps: `course` and `student`
</details>

<details>
<summary>Day 02: Static Files and Templates</summary>

- Managing static files (CSS, JavaScript, images)
- Implementing template inheritance to create a consistent layout
- Exploring Django's template language and tags
- Building a simple application with a base template and static assets
</details>

<details>
<summary>Day 03: ORM and Migrations</summary>

- Working with the Django Object-Relational Mapper (ORM)
- Creating and applying database migrations
- Customizing the Django admin site for better data management
- Building a `Book` model and managing it through the admin interface
</details>

<details>
<summary>Day 04: Forms and User Authentication</summary>

- Creating forms and `ModelForms` for data input
- Handling form submissions and validation
- Implementing basic user authentication and registration
- Building a simple Content Management System (CMS) with forms for `course` and `student` apps
</details>

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/zaher-m/ITI-Django-Course-Labs.git
    cd ITI-Django-Course-Labs
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Navigate to a lab's directory:**
    ```bash
    cd "Day 01"  # Or "Day 02", "Day 03", "Day 04"
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6.  **(Optional) Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
