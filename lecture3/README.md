# [Lecture 3 - Django](https://cs50.harvard.edu/web/2020/weeks/3/)

[Django](https://docs.djangoproject.com/en/3.1/) is a Python-based web framework that will allow us to write Python code that dynamically generates HTML and CSS. The advantage to using a framework like Django is that a lot of code is already written for us that we can take advantage of. Django is a high-level Python web framework that is both free and open source.

## To install: Django

```bash
$ pip install django

$ python -m django --version                                                85ms 
3.1.6

$ django-admin                                                               2ms 

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as
settings are not properly configured (error:Requested setting INSTALLED_APPS, but
settings are not configured. You must either
define the environment variable
DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
```

## HTTP
```Bash
HTTP, or HyperText Transfer Protocol,
is a widely-accepted protocol for how
messages are transfered back and forth
across the internet. Typically
information online is passed between a
client (user) and a server. 

```

## To create a project in django

```Bash
$ django-admin startproject projectdjango
$ python manage.py runserver                                                 2ms 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 09, 2021 - 18:52:32
Django version 3.1.6, using settings 'projectdjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

```Bash
Open browser : http://127.0.0.1:8000/
Quit the server with CONTROL-C

$ python manage.py startapp hello

/CS50-Web-Python-Java/lecture3/djg on  master! ⌚ 17:23:55
$ python manage.py runserver                                             90167ms 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 09, 2021 - 19:23:57

http://127.0.0.1:8000/hello/andvsilva
```

```Bash
status code   Description
    200       OK
    301       Moved Permanently
    403       Forbidden
    404       Not Found
    500       Internal Server Error
```

### Django - course DIO

```bash
Python, Django with SQL

### A good practice is to create an environment
### for each project.

$ sudo apt install python3-venv
$ python3 -m venv my-project-env
$ source my-project-env/bin/activate
$ pip install requests

# install django
pip install django

$ django-admin startproject app

$ python manage.py runserver                                                              604ms 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 22, 2021 - 00:32:37
Django version 3.2.8, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Useful references:

- [How to Create a Simple Django Web App With Python](https://medium.com/better-programming/how-to-create-a-simple-django-web-app-with-python-7ba75b4e34a6)
- [A Crash Course in Django](https://medium.com/@arijbirnbaum/a-crash-course-in-django-f7a39629e7e0)


