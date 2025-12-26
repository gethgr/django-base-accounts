# django-base-accounts

A reusable Django app providing an **abstract, email-based user model**.  
Designed to be extended in any Django project.

## Features

- Abstract `BaseUser` model (email as username)
- `BaseUserManager` for creating users and superusers
- Fully reusable and extendable in any project
- Ready for installation via `poetry` from GitHub

## Installation

```bash
poetry add git+https://github.com:gethgr/django-base-accounts.git
```

## After Installation

Add your app to INSTALLED_APPS in settings.py:
```bash
INSTALLED_APPS = [
    ...
    "base_accounts",
]
```

2. Create your custom user model inheriting from BaseUser:
```bash
from django.db import models
from base_accounts.models import BaseUser
from base_accounts.managers import BaseUserManager

class CustomUser(BaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    objects = BaseUserManager()
```

3. Set your custom user in settings.py:
```bash
AUTH_USER_MODEL = "yourapp.CustomUser"
```




   
