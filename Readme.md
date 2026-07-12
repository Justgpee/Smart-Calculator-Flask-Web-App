# Smart Calculator — Flask Web App

A multi-page web application built with Flask that performs arithmetic calculations, area calculations, and solves quadratic equations. Built as part of a Python Web Development with Flask course.



# Project Structure

```
project_1/
├── app.py                  # Flask application — routes and request
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── calculator/             # Python package — core math logic
│   ├── __init__.py
│   ├── arithmetic.py       # add, subtract, multiply, divide
│   ├── area.py             # rectangle, square, triangle, circle
│   └── quadratic.py        # quadratic equation solver
├── templates/              # Jinja2 HTML templates
│   ├── index.html          # Arithmetic calculator page
│   ├── area.html           # Area calculator page
│   └── quadratic.html      # Quadratic solver page
├── static/                 # Static assets
│   └── style.css           # Application styling
└── tests/                  # Unit tests
    ├── test_arithmetic.py
    ├── test_area.py
    └── test_quadratic.py


---

# Features

*Arithmetic Calculator — addition, subtraction, multiplication, division
*Area Calculator — rectangle, square, triangle, circle
*Quadratic Solver — solves ax² + bx + c = 0, returns two roots or "No solution"
*Unit Tests — 28 tests covering all math functions across three modules

---

# Tech Stack

*Python 3.11
*Flask 3.1.3 — micro web framework
*Jinja2 3.1.6 — HTML templating engine
*Werkzeug 3.1.8 — WSGI utility library
*unittest — Python built-in testing framework

---

# How to run

*1. Clone the repository
```bash
git clone https://github.com/dominic531/project_1.git
cd project_1
```

*2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# Mac/Linux
source venv/bin/activate
```

*3. Install dependencies
```bash
pip install -r requirements.txt
```

*4. Run the application
```bash
python app.py
```

*5. Open in browser
http://127.0.0.1:5000/

---

# Running Tests

```bash
python -m unittest discover tests
```

Expected output: 
Ran 28 tests in 0.003s
OK


---

# Pages

| Page | Route | Description |
|---|---|---|
| Arithmetic Calculator | `/` | add, subtract, multiply or divide two numbers |
| Area Calculator | `/area` | calculate area of rectangle, square, triangle or circle |
| Quadratic Solver | `/quadratic` | solve ax² + bx + c = 0 |

---

# How It Works

Flask connects HTML and Python through three handshakes:

1. *Names — every `name=` attribute in the HTML form becomes a key
   in `request.form{}` in `app.py`
2. *Route — the form POSTs to an address and `@app.route` in `app.py`
   decides which function handles it
3. *Template — `render_template()` passes the result back into
   `{{ result }}` in the HTML page

---

# Key Concepts Covered

- Flask routing with `@app.route` and `methods=["GET", "POST"]`
- Reading form data with `request.form{}`
- Jinja2 templating with `{{ }}` and `{% %}`
- Python package structure with `__init__.py`
- Unit testing with `unittest` and `assertEqual`
- Virtual environments and dependency management

---

# Author

Dave Nduka — AI Engineering Student
