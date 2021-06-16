# good-wood-server
Back End Capstone

## To Run Locally

Clone down the directory
``` git clone git@github.com:Loganwebb1994/good-wood-server.git```


Run the following commands to install pipenv and create a virtual environment.

    ```pip3 install --user pipx```
    ```pipx install pipenv ```
    ```pipenv shell```


Next, install these third-party packages

```pipenv install```

Load Fixtures

```python3 manage.py makemigrations```
```python3 manage.py migrate```
```python3 manage.py loaddata arborists```
```python3 manage.py loaddata woodworkers```
```python3 manage.py loaddata drops```

Then start the server

```python3 manage.py runserver```

URL

https://good-wood-server.herokuapp.com/

Description

Api for backend capstone
