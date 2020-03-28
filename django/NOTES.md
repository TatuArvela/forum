# Notes

## Generating hashed password

`python manage.py shell`

```python
from django.contrib.auth.hashers import make_password
make_password('test')
```
