# Task Manager - Django CRUD

This is a **Task Manager** application built using **Django** that allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks.

## Prerequisites

Ensure you have the following installed before running the project:

- **Python** (>=3.8)
- **pip** (Python package manager)
- **Virtual environment**
- **Django** (install via `pip install django`)
- **PyMySQL** (install via `pip install pymysql`)

## Setting Up the Project

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### 2. Create and Activate a Virtual Environment

#### On Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure Database

Ensure you have MySQL installed and running. Update your `settings.py` to configure the database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "task_manager",
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

Start the Django development server:

```sh
python manage.py runserver
```

By default, the server runs at:

```sh
http://127.0.0.1:8000/
```

## Features

- Create tasks
- Read task details
- Update tasks
- Delete tasks
- Admin panel for task management

## Contributing

Feel free to fork this repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.


