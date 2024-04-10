# Web Vending Machine

Web Vending Machine

## Use a virtual environment

NOTE: Django is a third-party library, and you should use a virtual environment and `pip` to install it.
To learn more about using a virtual environment, read this - [Using a Python virtual environment](VIRTUALENV.md)

## Use pip to install pytest

Confirm pip version by running:
```bash
(.venv) $ pip --version
```

Returns:
```bash
pip 24.0 from /Users/ ... /tdd-exercises-python/.venv/lib/python3.11/site-packages/pip (python 3.11)
```

To upgrade, run:
```bash
(.venv) $ pip install --upgrade pip
```

```bash
(.venv) $ python -m pip install Django
```

```bash
(.venv) $ python manage.py migrate
```

```bash
(.venv) $ python manage.py runserver
```

### Manually test the Vending Machine

Now, you can manually Test the Vending Machine at:
http://127.0.0.1:8000/vending_machine/



# Testing Web Vending Machine with Selenium

In this section, we will test the Web Vending Machine with Selenium.

## Selenium Chrome Driver

You will need the Selenium chromedriver

Running:
```bash
(.venv) $ chromedriver --version
```

Returns (something like):
```bash
ChromeDriver 123.0.6312.105 (399174dbe6eff0f59de9a6096129c0c827002b3a-refs/branch-heads/6312@{#761})
```

If `chromedriver` is not install, take a look at this - [Pytest Selenium WebDriver Example](https://github.com/ruthlesshelp/pytest-selenium-example)

## Requirements

You will need Python 3.10+ and `pytest` 8+ 

### Use a virtual environment

NOTE: pytest is a third-party library, and you should use a virtual environment and `pip` to install it.
To learn more about using a virtual environment, read this - [Using a Python virtual environment](VIRTUALENV.md)

## Getting Started

This is an example of how to install and run `pytest-selenium`, a Selenium plugin for the `pytest` runner.

### Install pytest

Install `pytest` by running:
```bash
(.venv) $ pip install pytest
```

Confirm the pytest version by running:
```bash
(.venv) $ pytest --version
```

Returns:
```bash
pytest 8.1.1
```

## Use pip to install pytest-selenium

Install pytest-selenium by running:
```bash
(.venv) $ pip install pytest-selenium
```

# Run the tests

Now, run the Selenium automated test.

Running:
```bash
(.venv) $ pytest tests/test_basic_selenium.py
```

Returns
```bash
=================================== test session starts ====================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
sensitiveurl: .*
rootdir: /Users/ ... /web_vending_machine
plugins: variables-3.1.0, html-4.1.1, metadata-3.1.1, base-url-2.1.0, selenium-4.1.0
collected 1 item                                                                           

tests/test_basic_selenium.py .                                                       [100%]

==================================== 1 passed in 1.53s =====================================
```

## Install pytest-django

Before we combine Selenium and Django, let's install `pytest-django`, like this:

```bash
(.venv) $ pip install pytest-django
```

## Test Django with Selenium

Running:
```bash
(.venv) $ pytest tests/test_browser_one.py
```

Returns:
```bash
=================================== test session starts ====================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.4.0
django: version: 5.0.4, settings: web_vending_machine.settings (from ini)
sensitiveurl: .*
rootdir: /Users/ ... /web_vending_machine
configfile: pytest.ini
plugins: variables-3.1.0, html-4.1.1, metadata-3.1.1, django-4.8.0, base-url-2.1.0, selenium-4.1.0
collected 1 item                                                                                                                    

tests/test_browser_one.py .                                                                                                   [100%]

==================================== 1 passed in 1.47s =====================================
```
