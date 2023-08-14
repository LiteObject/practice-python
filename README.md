## Python Basics
- `pip` is the Python package manager that installs, updates, uninstalls packages.
- `venv` allows you to manage seperate package installations for different projects and is installed with Python 3 by default.
- `conda` installed with miniconda, can be used to manage both packages and virtual environments.

## How to install Python, pip, venv
- First update your Linux distro: 
  - `sudo apt update && sudo apt upgrade`
- Confirm that Python3 i already installed:
  - `python3 --version`
- To update Python:
  - `sudo apt upgrade python3`  
- To install pip:
  - `sudo apt install python3-pip`
- To install venv:
  - `sudo apt install python3-venv`

## Create a virtual environment
>Using virtual environments is a recommended best practice for Python development projects. By creating a virtual environment, you can isolate
your project tools and avoid versioning conflicts with tools for other projects.

- To create a virtual environment:
  - `python3 -m venv myenv`
  - This will create a new virtual environment directory names `myenv` in the current directory.
- To activate the virtual environment:
  - `source myenv/bin/activate`

## Common `pip` commands
- `pip --version`
- `pip help`
- `pip list`
- `pip show <PACKAGE_NAME>`
- `pip install <PACKAGE_NAME>`
- `pip install git+https://github.com/.../sample-project.git@main`
- `pip install --upgrade <PACKAGE_NAME>`
- `pip uninstall <PACKAGE_NAME>`

---

## Jupyter Notebook

Jupyter Notebook is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations, and text.

Jupyter Notebook is a popular tool among data scientists. Users can use Jupyter Notebook for data cleaning and transformation, numerical simulation, statistical modeling, data visualization, and machine learning.

Jupyter Notebook was formerly known as __IPython__ notebook. The project was renamed Jupyter in 2014. Jupyter Notebook is maintained by the people at Project Jupyter.

## 

---
## Helpful Links:
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)


