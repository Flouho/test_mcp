# Flask Blog Project (Enhanced)

A modern blog application built with Python Flask framework featuring:

## ✨ Key Features
- **User Authentication**: Basic login/register functionality
- **Post Management**: Create, edit and delete blog posts
- **Responsive Design**: Mobile-friendly interface with custom CSS
- **Database**: SQLite with SQLAlchemy ORM
- **Math Support**: KaTeX integration for mathematical expressions
- **Theme Switching**: Light/Dark/System theme options

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
git clone https://github.com/Flouho/test_mcp.git
cd test_mcp
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python init_db.py
flask run --port 5001
```

## ⚙️ Configuration

| File | Purpose |
|------|---------|
| `app.py` | Main application configuration |
| `config.py` | Environment variables |
| `static/style.css` | Custom styling |
| `models.py` | Database models |

## 📝 Writing Math Content
Use LaTeX syntax with `$...$` for inline math and `$$...$$` for display math.

## 🌟 Recent Updates
- Added KaTeX math rendering support
- Improved mobile navigation
- Enhanced theme switching system

## 📜 License
MIT License
