# Python Programming - Learning Repository

A personal collection of Python scripts covering fundamental programming concepts, data structures, OOP, and early experiments with APIs and data analysis.

## Overview

This repository contains my practice code while learning Python. It includes basic to intermediate level Python concepts, along with some real-world API integration examples using public web services.

The main goal of this repository is to document my learning journey and serve as a reference for core Python programming topics.

## Repository Purpose

- Practice and reinforce Python programming fundamentals
- Understand Python syntax, data structures, and OOP principles
- Experiment with external libraries and API consumption
- Build a foundation for more advanced Python projects

## Key Concepts Covered

### Python Basics
- Variables, data types, and type casting
- String formatting (`f-strings`, `.format()`)
- Conditional statements (`if-elif-else`)
- Loops (`for`, `while`, `break`, `continue`)

### Data Structures
- Lists (operations, methods, sorting, slicing)
- Tuples (immutability)
- Dictionaries (key-value pairs, nesting, methods)
- Sets (unique elements, operations)

### Functions
- Defining and calling functions
- Parameters, return values
- `*args` and `**kwargs`

### Object-Oriented Programming
- Classes and objects
- Constructors (`__init__`)
- Methods
- Inheritance and method overriding

### Modules and Libraries
- Built-in modules (`datetime`, `time`, `json`)
- Custom modules
- External libraries (`requests`, `pandas`)

### API Integration
- Working with JSON data
- Making HTTP requests to public APIs (Binance public endpoint example)
- Parsing and displaying API responses

## Project Structure

```bash
Python-programming/
├── first_program.py           # Hello World, variables, strings, type conversion
├── conditionals.py            # If-else conditions and logical operators
├── loops.py                   # For loops, while loops, break & continue
├── function.py                # Functions with *args and **kwargs
├── List.py                    # List operations (append, remove, sort, etc.)
├── tuple.py                   # Tuple basics and immutability
├── dictionary.py              # Dictionary operations and methods
├── set.py                     # Set operations
├── classes.py                 # OOP - Classes, inheritance, method overriding
├── modules.py                 # Importing modules (built-in + custom)
├── calculator.py              # Example custom module
├── parse_json.py              # JSON handling and public API calls
├── practice.py                # Candlestick data analysis practice
├── practice2.py               # Basic trading logic functions
├── Python_Complete_Notes.pdf  # Scanned handwritten notes (reference)
├── README.md
└── .gitignore
```

**Technologies Used**

- **Language**: Python 3
- **Libraries**:
  - requests - HTTP requests
  - json - JSON parsing
  - pandas - Data manipulation (used in some advanced scripts)
  - python-binance - Binance API client (in select scripts)
  - Built-in: datetime, time

**How to Run**

**1\. Clone the repository**

Bash

git clone <https://github.com/ahmadhassan-prodev/Python-programming.git>

cd Python-programming

**2\. (Optional) Create a virtual environment**

Bash

python -m venv venv

_\# Windows_

venv\\Scripts\\activate

_\# macOS/Linux_

source venv/bin/activate

**3\. Install dependencies (for API and pandas scripts)**

Bash

pip install requests pandas python-binance

**4\. Run any script**

Bash

python first_program.py

python classes.py

python parse_json.py

python List.py

**Note**: Some scripts (like those using Binance API) may require an internet connection.

**Learning Outcomes**

By studying this repository, you can learn:

- Python syntax and programming fundamentals
- Effective use of Python's built-in data structures
- Object-oriented programming concepts
- How to consume public REST APIs and handle JSON data
- Basic data analysis with pandas

**Notes**

- This is a **learning/practice repository**. Many scripts are simple exercises.
- Some files contain experimental code related to cryptocurrency data as part of learning API integration.
- API keys present in a few scripts are for educational purposes only and should not be used in production.
- The repository includes scanned notes (Python_Complete_Notes.pdf) for personal reference.

**Future Improvements**

- Organize code into clearer folders (basics, oop, api, etc.)
- Add comments and docstrings for better readability
- Remove hardcoded credentials and use environment variables
- Add more structured projects and mini-applications
