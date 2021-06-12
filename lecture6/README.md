# [Lecture 6 - User Interfaces](https://cs50.harvard.edu/web/2020/weeks/6/)

So far, we’ve discussed how to build simple web pages using HTML and CSS, and how to use Git and GitHub in order to keep track of changes to our code and collaborate with others. We also familiarized ourselves with the Python programming language, started using Django to create web applications, and learned how to use Django models to store information in our sites. We then introduced JavaScript and learned how to use it to make web pages more interactive.

Today, we’ll discuss common paradigms in User Interface design, using JavaScript and CSS to make our sites even more user friendly.

### User Interfaces
A User Interface is how visitors to a web page interact with that page. Our goal as web developers is to make these interactions as pleasant as possible for the user, and there are many methods we can use to do this.

### Single Page Applications
Previously, if we wanted a website with multiple pages, we would accomplish that using different routes in our Django application. Now, we have the ability to load just a single page and then use JavaScript to manipulate the DOM. One major advantage of doing this is that we only need to modify the part of the page that is actually changing. For example, if we have a Nav Bar that doesn’t change based on your current page, we wouldn’t want to have to re-render that Nav Bar every time we switch to a new part of the page.

Let’s look at an example of how we could simulate page switching in JavaScript: [code here](html/simplepage.html)

```Bash
# TERMINAL
$ google-chrome simplepage.html
```

```Bash
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>
        <script src="js/singlepage.js"></script>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <div id="page1">
            <h1>This is page 1</h1>
        </div>
        <div id="page2">
            <h1>This is page 2</h1>
        </div>
        <div id="page3">
            <h1>This is page 3</h1>
        </div>
    </body>
</html>
```

Notice in the HTML above that we have three buttons and three divs. At the moment, the divs contain only a small bit of text, but we could imagine each div containing the contents of one page on our site. Now, we’ll add some JavaScript that allows us to use the buttons to toggle between pages [here the javascript code](html/js/singlepage.js)

In many cases, it will be inefficient to load the entire contents of every page when we first visit a site, so we will need to use a server to access new data. For example, when you visit a news site, it would take far too long for the site to load if it had to load every single article it has available when you first visit the page. We can avoid this problem using a strategy similar to the one we used while loading currency exchange rates in the previous lecture. This time, we’ll take a look at using Django to send and receive information from our single page application. To show how this works, let’s take a look at a simple Django application. It has two URL patterns in ```urls.py```:


#### Django Application - Single Page
```Bash
$ django-admin startproject singlepage
$ cd singlepage
### Run 'python manage.py migrate' to apply them.
$ python manage.py migrate                                       16408ms 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

$ python manage.py runserver                                      2759ms 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 12, 2021 - 13:21:11
Django version 3.1.6, using settings 'singlepage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

**URL patterns in** [urls.py](singlepage/singlepage/views.py)

```Bash
# Add
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
```

And two corresponding routes in [views.py](singlepage/../singlepage1/singlepage/views.py). Notice that the ```section``` route takes in an integer, and then returns a string of text based on that integer as an HTTP Response.

Now, within our [index.html](singlepage/../singlepage1/singlepage/templates/singlepage/index.html) file, we’ll take advantage of AJAX, which we learned about last lecture, to make a request to the server to gain the text of a particular section and display it on the screen:

```Bash
# TERMINAL
$ google-chrome http://127.0.0.1:8000/sections/1
$ google-chrome http://127.0.0.1:8000/sections/2
$ google-chrome http://127.0.0.1:8000/sections/3


google-chrome http://127.0.0.1:8000/
```

```bash

~/repo/CS50-Web-Python-Java/lecture6/singlepage1 on  master! ⌚ 11:58:51
$ tree                                                                        1ms 
.
├── db.sqlite3
├── manage.py
├── singlepage
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-37.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── views.cpython-37.pyc
│   ├── templates
│   │   └── singlepage
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── singlepage1
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── settings.cpython-37.pyc
    │   ├── urls.cpython-37.pyc
    │   └── wsgi.cpython-37.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

8 directories, 26 files
```

Now, we’ve created a site where we can load new data from a server without reloading our entire HTML page!

One disadvantage of our site though is that the URL is now less informative. You’ll notice in the video above that the URL remains the same even when we switch from section to section. We can solve this problem using the [JavaScript History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This API allows us to push information to our browser history and update the URL manually. Let’s take a look at how we can use this API. Imagine we have a Django project identical to the previous one, but this time we wish to alter our script to be employ the history API:

In the ```showSection``` function above, we employ the history.pushState function. This function adds a new element to our browsing history based on three arguments:

    1. Any data associated with the state.
    2 - A title parameter ignored by most web browsers
    3 - What should be displayed in the URL
The other change we make in the above JavaScript is in setting the onpopstate parameter, which specifies what we should do when the user clicks the back arrow. In this case, we want to show the previous section when the button is pressed. Now, the site looks a little more user-friendly: