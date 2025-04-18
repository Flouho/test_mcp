# Flask Blog Project

A simple blog application built with Python Flask framework.

## Features
- User authentication (login/register)
- Create, edit and delete blog posts
- Responsive design with Bootstrap
- SQLite database

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Flouho/test_mcp.git
cd test_mcp
```

2. Create virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Initialize database:
```bash
python init_db.py
```

4. Run the application:
```bash
flask run --port 5001
```

## Configuration
- Edit `app.py` to change application settings
- Modify `static/style.css` for custom styling

## License
MIT
