# Using a Python virtual environment

You will want to use the *venv* module to create a “virtual environment”, with an independent set of Python packages installed in the project directory.
https://docs.python.org/3/library/venv.html

Confirm the Python version with `python --version`
```zsh
Python 3.11.7
```

**NOTE:** On a lot of Linux distributions and on macOS, `python` is Python 2. `python3` is Python 3. In other installations, `python` is a command alias for `python3`. We’ll always be using `python3`, but will shorten it to `python`. If you couldn't confirm the Python version, try with `python3 --version`.

## 1. Clone this repo

[Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to create a local copy on your computer.

## 2. Create and activate the virtual environment

Create the virtual environment with `python -m venv .venv`

### Activate on macOS and Linux

Activate the virtual environment with `source .venv/bin/activate`

### Activate on Windows

Activate on Windows with `.venv\Scripts\activate.bat`

**NOTE:** To activate on Windows with PowerShell use `.venv\Scripts\Activate.ps1`

