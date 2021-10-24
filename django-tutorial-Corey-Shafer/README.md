# [Django Tutorial by Corey Schafer - The Best](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer)

**Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started**

First, let's to prepare the environment and install the packages to develop the tutorials.

```bash
# create a folder to store the codes
$ take django-tutorial-Corey-Shafer

# An enviromnent
$ sudo apt install python3-venv

# Active the enviromnent  
$ source app-project/bin/activate

## For deactivate just type:
## $ deactivate

## Install packages:

## freeze-requirements
$ pip install freeze-requirements                                                                                 6ms 
Collecting freeze-requirements
  Using cached freeze_requirements-0.5.3-py3-none-any.whl
Collecting click
  Downloading click-8.0.3-py3-none-any.whl (97 kB)
     |████████████████████████████████| 97 kB 723 kB/s 
Collecting six
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting sh
  Using cached sh-1.14.2-py2.py3-none-any.whl (40 kB)
Installing collected packages: six, sh, click, freeze-requirements
Successfully installed click-8.0.3 freeze-requirements-0.5.3 sh-1.14.2 six-1.16.0

## python - Upgrade - pip
$ python3 -m pip install --upgrade pip                                                                                                5996ms 
Requirement already satisfied: pip in ./app-project/lib/python3.8/site-packages (21.1.1)
Collecting pip
  Downloading pip-21.3.1-py3-none-any.whl (1.7 MB)
     |████████████████████████████████| 1.7 MB 5.1 MB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-21.3.1

## Install django version 2.1
$ pip install django==2.1            
Collecting django==2.1
  Downloading Django-2.1-py3-none-any.whl (7.3 MB)
     |████████████████████████████████| 7.3 MB 6.4 MB/s            
Collecting pytz
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 5.9 MB/s            
Installing collected packages: pytz, django
Successfully installed django-2.1 pytz-2021.3
(app-project) (base)

## check the version of the django.
$ python -m django --version
2.1

## Install requests
$ pip install requests                                                                                                                 264ms 
Collecting requests
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 123 kB/s             
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.7-py3-none-any.whl (38 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.3-py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 1.0 MB/s             
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.7-py2.py3-none-any.whl (138 kB)
     |████████████████████████████████| 138 kB 10.9 MB/s            
Collecting certifi>=2017.4.17
  Downloading certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
     |████████████████████████████████| 149 kB 4.8 MB/s            
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.7 idna-3.3 requests-2.26.0 urllib3-1.26.7
(app-project) (base) 

~/repo/CS50-Web-Python-Java/django-tutorial-Corey-Shafer on  master! ⌚ 11:46:25

$ pip freeze > requirements.txt ## Update in the future if more packages were installed


# The package installed for this project. -> requirement.txt (main folder)

$ pip freeze 
certifi==2021.10.8
charset-normalizer==2.0.7
click==8.0.3
Django==2.1
freeze-requirements==0.5.3
idna==3.3
pytz==2021.3
requests==2.26.0
sh==1.14.2
six==1.16.0
urllib3==1.26.7
(app-project) (base) 

## If you will start to work in this project, you need to 
## the packages listed in requirements.tx

## To install the dependencies for this project
## You just need type on the terminal

$ pip install -r requirements.txt

## Below we have the main command lines to work django application. See yourself:

## on the terminal:
$ django-admin                                        
Type 'django-admin help <subcommand>' for help on a specific subcommand.

'Available subcommands:'

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
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
(app-project) (base) 

## Let's start the project, just type on the terminal:
$ django-admin startproject django_project

# To the file inside the directory project
# cd to the folder django_project and 
# type tree
~/repo/CS50-Web-Python-Java/django-tutorial-Corey-Shafer/django_project on  master! ⌚ 12:05:38
$ tree
.
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 6 files
(app-project) (base) 

$ python manage.py runserver                                                  
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

October 23, 2021 - 15:17:09
Django version 2.1, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


$ python manage.py migrate

## open the browser and https://127.0.0.1:8000/admin/
```

![](figures/django_admin.png)


## Applications and Routes

```bash
# Terminal
$ python manage.py startapp blog

$ tree
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── static
│   │   └── blog
│   │       └── main.css
│   ├── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

10 directories, 30 files


In the folder:
── templates
│   │   └── blog
│   │       ├── about.html
│   │       ├── base.html
│   │       └── home.html

# see the 3 files -> pages

# style for the page:
static
│   │   └── blog
│   │       └── main.css

## open in the browser:
## http://127.0.0.1:8000/blog/
```

![](figures/blog_page.png)

```bash
### Add the code below to the file home.html

<article class="media content-section">
  <div class="media-body">
    <div class="article-metadata">
      <a class="mr-2" href="#">{{ post.author }}</a>
      <small class="text-muted">{{ post.date_posted }}</small>
    </div>
      <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
      <p class="article-content">{{ post.content }}</p>
  </div>
</article>

### file home.html
{% extends "blog/base.html" %}
{% block content%}
    {%for post in posts %}
        <article class="media content-section">
            <div class="media-body">
            <div class="article-metadata">
                <a class="mr-2" href="#">{{ post.author }}</a>
                <small class="text-muted">{{ post.date_posted }}</small>
            </div>
                <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
    {% endfor %}
{% endblock content %}
```

## Resources

- [Django Basics for a Beginner](https://medium.com/@humble_bee/django-basics-for-a-beginner-5d864e6aa084)
- [Build fast, responsive sites with Bootstrap](https://getbootstrap.com/)