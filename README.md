# Midterm Project

Before running or starting your project, ensure you have the following installed:

- **Python** (>=3.8)
- **pip** (Python package manager)
- **Virtual environment**
- **Django** (install via pip install django if not already installed)
- **PyMySQL**

## Running the Project

After setting up your Django project (including project creation, startapp, settings configuration, URL routing, migrations, etc.), follow these steps:

### Navigate to your project directory using the terminal:
```sh
cd project_name
```

### Start the development server:
```sh
python manage.py runserver
```

A clickable HTTP server link will appear in the terminal. Hold Ctrl and left-click the link to open it in your browser.
By default, the server runs at:
```sh
http://127.0.0.1:8000/
```
To access a specific app within your project, append the app's URL path. For example:
```sh
http://127.0.0.1:8000/tasks/
```

Press Enter to load your landing page.
You can now debug and test your project as needed.