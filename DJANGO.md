
```bash
$ python -m django --version
```

```bash
$ django-admin startproject web_vending_machine
```

```bash
$ python3 -m venv .venv
```

```bash
$ source .venv/bin/activate
```

```bash
(.venv) $ pip install --upgrade pip
```


```bash
(.venv) $ python -m pip install Django
```

```bash
(.venv) $ python manage.py startapp vending_machine
```


```bash
(.venv) $ python manage.py runserver
```


```bash
(.venv) $ python manage.py migrate
```

```bash
(.venv) $ python manage.py makemigrations vending_machine
```

```bash
Migrations for 'vending_machine':
  vending_machine/migrations/0001_initial.py
    - Create model Payment
```

```bash
(.venv) $ python manage.py sqlmigrate vending_machine 0001
```

```bash
(.venv) $ python manage.py migrate
```

```bash
(.venv) $ python manage.py runserver
```

