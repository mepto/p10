# SoftDesk


## What it does

Saves projects, users and comments as API for several platforms.


## How to install

### Clone the repository on your computer

`git clone https://github.com/mepto/p10.git`

### Python version

Make sure you use python 3.10. Check your python version:

`python --version`

### Virtual environment

Create and activate your virtual environment. The methodology below uses the venv module but you may use your favorite
 virtual environment instead.

* Creation from project root:

`python -m venv <your-virtual-env-name>` 
 
* Activation in Windows:

`<your-virtual-env-name>\Scripts\activate.bat`

* Activation in Linux:

`source <your-virtual-env-name>/bin/activate`

### Secret key

Create a `.softdesk.secret` file in the `main` folder and add a json 
dictionary with: 
- the `SECRET_KEY` item for Django and 
- the `DB_PWD` item for the database.

### Requirements

Install the required python packages with pip

`pip install -r requirements.txt`

If you need to upgrade pip, type in the following command:

`python -m pip install --upgrade pip`

### Database

The database is a postgresql database. 
You will need to create one on your local machine. 
Install postgresql on your windows machine if it is not already by going to 
https://www.postgresql.org/download/windows/ and using the installer, selecting 
the version relevant to your environment.

On Windows, once the installation is done, open the sql shell from the 
windows menu. Leave the defaults until the password where you should input 
the one you provided during the installation.

When the "postgres=#" prompt appears, create a new user with the following 
command:

`CREATE USER softdesk_user WITH PASSWORD '<yourpassword>';`

Then create a database:

`CREATE DATABASE softdesk_db;`

Ensure user is owner of the database:
`ALTER DATABASE softdesk_db OWNER TO softdesk_user;`

### Migrations

# Once the database is created, you will need to run the migrations.

`python manage.py migrate`

### Retrieve static files

`python manage.py collectstatic`

### Start server

`python manage.py runserver`

NB: If you experience issues when running the server, it might be because the 
PYTHONPATH is not properly declared. You need it to run your server in your 
virtual environment. This might easily happen if, when installing the python 
version, you didn't tick the "Add to Python <version> to PATH."
The following link may help you with adding it to you environment variables:
https://www.edureka.co/blog/add-python-to-path/

### Changes to the project

#### Commits

The pre-commit package is there to make sure that checks such as imports and 
PEP8 are properly respected. After requirements are set, run

`pre-commit install`

You can also run the checks separate from commit by running

`pre-commit run --all-files`


## Postman documentation

The documentation for API endpoints is available on Postman at 
https://documenter.getpostman.com/view/12049100/2s93JzMgbq
