# Recipe Project Setup

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Steps

1. Clone the repository or extract the project files
```bash
git clone <repository-url>
cd recipe_project
```

2. Create and activate virtual environment
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup database
```bash
python manage.py migrate
```

5. Create superuser (optional)
```bash
python manage.py createsuperuser
```

6. Create required directories
```bash
mkdir media
mkdir staticfiles
```

7. Run development server
```bash
python manage.py runserver
```

## Access Points
- Main site: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/
- Recipe list: http://127.0.0.1:8000/recipes/
- Create recipe: http://127.0.0.1:8000/recipes/new/

## Development Tools
This project includes:
- Django Debug Toolbar
- Black (code formatter)
- Flake8 (code linter)
- python-dotenv (environment variables)
