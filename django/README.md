# Django / Python

## Installation

### Requirements

* `pipenv`

If you encounter issues like `django` missing, verify that your `pipenv` is properly installed and there are no stray packages, environments or configurations

### Instructions

1. Install the dependencies:  
    ```bash
    pipenv install
    ```
2. Run the migrations:  
    ```bash
    python manage.py migrate
    ```
3. Load base data:  
    ```bash
    python manage.py loaddata initial_data.json
    ```
4. Run the server:  
    ```bash
    python manage.py runserver
    ```
5. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser

## Tests

> _TODO: Better test coverage_

```bash
python manage.py test
```

## Generating a hashed password

`python manage.py shell`

```python
from django.contrib.auth.hashers import make_password

make_password('test')
```
