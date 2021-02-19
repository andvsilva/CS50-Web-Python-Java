# [Lecture 4 - SQL, Models, and Migrations](https://cs50.harvard.edu/web/2020/weeks/4/)

[SQL](https://dev.mysql.com/doc/), or Structured Query Language, is a programming language that allows us to update and query databases.

## Database

Before we get into how to use the SQL language, we should discuss how our data is stored. When using SQL, we’ll work with a [relational database](https://www.oracle.com/database/what-is-a-relational-database/#:~:text=A%20relational%20database%20is%20a,of%20representing%20data%20in%20tables) where we can find all of our data stored in a number of tables. Each of these tables is made up of a set number of columns and a flexible number of rows.

To illustrate how to work with SQL, we’ll use the example of a website for an airline used to keep track of flights and passengers. In the following table, we see that we’re keeping track of a number of flights, each of which has an origin, a destination, and a duration.

There are several different relational database management systems that are commonly used to store information, and that can easily interact with SQL commands:

- [MySQL](https://www.mysql.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://www.sqlite.org/index.html)

## SQLite3

```bash
## terminal
## To install
$ sudo apt-get install sqlite3 libsqlite3-dev

## This a basic example to show the main METHODS - SQL
# create file sql
~/repo/CS50-Web-Python-Java/lecture4/data
$ touch flights.sql

# open sqlite3 file flights
~/repo/CS50-Web-Python-Java/lecture4/data
$ sqlite3 flights.sql                                      
SQLite version 3.33.0 2020-08-14 13:23:32
Enter ".help" for usage hints.
sqlite> CREATE TABLE flights (
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> origin TEXT NOT NULL,
   ...> destination TEXT NOT NULL,
   ...> duration INTEGER NOT NULL
   ...> );

# Listing all current tables (Just flights for now)
sqlite> .tables
flights

# Querying for everything within flights (Which is now empty)
sqlite> SELECT * FROM flights;

# Adding one flight
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);

# Checking for new information, which we can now see
sqlite> SELECT * FROM flights;
1|New York|London|415

# Adding some more flights
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);

# Querying this new information
sqlite> SELECT * FROM flights;
1|New York|London|415
2|Shanghai|Paris|760
3|Istanbul|Tokyo|700
4|New York|Paris|435
5|Moscow|Paris|245
6|Lima|New York|455

# Changing the settings to make output more readable
sqlite> .mode columns
sqlite> .headers yes
sqlite> SELECT * FROM flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415     
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
4   New York  Paris        435     
5   Moscow    Paris        245     
6   Lima      New York     455 

sqlite> SELECT * FROM flights WHERE origin = "New York";
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415     
4   New York  Paris        435

# We can also use more than just equality to filter out 
# our flights. For integer and real values, we can use 
# greater than or less than:
sqlite> SELECT * FROM flights WHERE duration > 500;
id  origin    destination  duration
--  --------  -----------  --------
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700

# And we can also use other logic (AND, OR) like in Python:
## SQL AND, OR and NOT Operators: 
## https://www.w3schools.com/sql/sql_and_or.asp
sqlite> SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
id  origin    destination  duration
--  --------  -----------  --------
2   Shanghai  Paris        760

sqlite> SELECT * FROM flights WHERE duration > 500 OR destination = "Paris";
id  origin    destination  duration
--  --------  -----------  --------
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
4   New York  Paris        435     
5   Moscow    Paris        245

# We can also use the keyword IN to see if a bit of data 
# is one of several options:

sqlite> SELECT * FROM flights WHERE origin IN ("New York", "Lima");
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415     
4   New York  Paris        435     
6   Lima      New York     455  

# We can even use regular expressions to search words more 
# broadly using the LIKE keyword. The below query finds all 
# results with an a in the origin, by using % as a wildcard
# character.

sqlite> SELECT * FROM flights WHERE origin LIKE "%a%";
id  origin    destination  duration
--  --------  -----------  --------
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
6   Lima      New York     455
```

## Functions

There are also a number of SQL functions we can apply to the results of a query. These can be useful if we don’t need all of the data returned by a query, but just some summary statistics of the data.

- [AVERAGE](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [COUNT](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [MAX](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [MIN](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [SUM](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [...](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

### [UPDATE](https://www.w3schools.com/sql/sql_update.asp)
we may also want to be able update rows of a table that already exist.

```bash
sqlite> SELECT * FROM flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415     
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
4   New York  Paris        435     
5   Moscow    Paris        245     
6   Lima      New York     455

# update table a new information
sqlite> UPDATE flights
   ...>     SET duration = 430
   ...>     WHERE origin = "New York"
   ...>     AND destination = "London";

sqlite> SELECT * FROM flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       430    # new info add  
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
4   New York  Paris        435     
5   Moscow    Paris        245     
6   Lima      New York     455
```

### [DELETE](https://www.w3schools.com/sql/sql_delete.asp)

```bash
sqlite> SELECT * FROM flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       430     
2   Shanghai  Paris        760     
3   Istanbul  Tokyo        700     
4   New York  Paris        435     
5   Moscow    Paris        245     
6   Lima      New York     455

# delete row
sqlite> DELETE FROM flights WHERE destination = "Tokyo";

sqlite> SELECT * FROM flights;
id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       430     
2   Shanghai  Paris        760     
4   New York  Paris        435     
5   Moscow    Paris        245     
6   Lima      New York     455
```

### Other Clauses

There are a number of additional clauses we can use to control queries coming back to us

- [LIMIT](https://www.w3schools.com/sql/sql_top.asp): Limits the number of results returned by a query
- [ORDER BY](https://www.w3schools.com/sql/sql_orderby.asp): Orders the results based on a specified column
- [GROUP BY](https://www.w3schools.com/sql/sql_groupby.asp): Groups results by a specified column
- [HAVING](https://www.w3schools.com/sql/sql_having.asp): Allows for additional constraints based on the number of results

### Joining Tables
- A [FOREIGN KEY](https://www.w3schools.com/sql/sql_foreignkey.asp) is a key used to link two tables together.

### JOIN Query
  - [JOIN](https://www.w3schools.com/sql/sql_join.asp)

### Django Models

[Django Models](https://docs.djangoproject.com/en/3.0/topics/db/models/) are a level of [abstraction](https://techterms.com/definition/abstraction) on top of SQL that allow us to work with databases using Python classes and objects rather than direct SQL queries.

Let’s get started on using models by creating a django project for our airline, and creating an app within that project

```bash
~/repo/CS50-Web-Python-Java/lecture4
$ django-admin startproject airline

~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py startapp flights

```

Now we’ll have to go through the process of adding an app as usual:

1. Add ```flights``` to the ```INSTALLED_APPS``` list in ```settings.py```
2. Add a route for ```flights``` in ```urls.py```:

```bash
### urls.py
path("flights/", include("flights.urls")),
```

1. Create a ```urls.py``` file within the ```flights``` application. And fill it with standard ```urls.py``` imports and lists.

```Bash
### flights/urls.py 
from django.urls import path

from . import views

urlpatterns = [
    
]
```

Now, rather than creating actual paths and getting started on ```views.py```, we’ll create some models in the ```models.py``` file. In this file, we’ll outline what data we want to store in our application. Then, Django will determine the SQL syntax necessary to store information on each of our models. Let’s take a look at what a model for a single flight might look like:

```bash
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
```

Let’s take a look at what’s going on in this model definition:

- In the first line, we create a new model that **extends** Django’s model class.
- Below, we add fields for origin, destination, and duration. The first two are [Char Fields](https://docs.djangoproject.com/en/3.0/ref/forms/fields/#charfield), meaning they store strings, and the third is an [Integer Field](https://docs.djangoproject.com/en/3.0/ref/forms/fields/#integerfield). These are just two of many [built-in Django Field classes](https://docs.djangoproject.com/en/3.0/ref/forms/fields/#built-in-field-classes)
- We specify maximum lengths of 64 for the two Character Fields. you can check the specifications available for a given field by checking the [documentation](https://docs.djangoproject.com/en/3.0/ref/forms/fields/#built-in-field-classes).


### Migrations

Now, even though we’ve created a model, we do not yet have a database to store this information to create a database from our models, we navigate to the main directory of our project and run the command.

```bash
# terminal 
$ python manage.py makemigrations
```

This command creates some Python files that will create or edit our database to be able to store what we have in our models. You should get an output that looks something like the one below, and if you navigate to your migrations directory, you’ll notice a new file was created for us

![](figures/makemigrations.png)

Next, to apply these migrations to our database, we run the command

```bash
## terminal
python manage.py migrate
```

Now, you’ll see some default migrations have been applied along with our own, and you’ll also notice that we now have a file called db.sqlite3 in our project’s directory

![](figures/migrate.png)

```bash
~/repo/CS50-Web-Python-Java/lecture4/airline
$ ls                                                                          3218ms 
airline  db.sqlite3  flights  manage.py

```

### Shell

Now, to begin working adding information to and manipulating this database, we can enter Django’s shell where we can run Python commands within our project.

```Bash
## terminal
$ python manage.py shell                                                         3ms 
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

```

```bash
# Import our flight model
In [1]: from flights.models import Flight

# Create a new flight
In [2]: f = Flight(origin="New York", destination="London", duration=415)

# Instert that flight into our database
In [3]: f.save()

# Query for all flights stored in the database
In [4]: Flight.objects.all()
Out[4]: <QuerySet [<Flight: Flight object (1)>]>
```

![](figures/shell.png)

When we query our database, we see that we get just one flight called Flight object (1). This isn’t a very informative name, but we can fix that. Inside models.py, we’ll define a __str__ function that provides instructions for how to turn a Flight object into a string:

```Bash
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

Now, when we go back to the shell, our output is a bit more readable:

```bash
# Create a variable called flights to store the results of a query
In [7]: flights = Flight.objects.all()

# Displaying all flights
In [8]: flights
Out[8]: <QuerySet [<Flight: 1: New York to London>]>

# Isolating just the first flight
In [9]: flight = flights.first()

# Printing flight information
In [10]: flight
Out[10]: <Flight: 1: New York to London>

# Display flight id
In [11]: flight.id
Out[11]: 1

# Display flight origin
In [12]: flight.origin
Out[12]: 'New York'

# Display flight destination
In [13]: flight.destination
Out[13]: 'London'

# Display flight duration
In [14]: flight.duration
Out[14]: 415
```

![](figures/shell_flight_properties.png)

This is a good start, but thinking back to earlier, we don’t want to have to store the city name as an origin and destination for every flight, so we probably want another model for an airport that is somehow related to the flight model:

```Bash
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

We’ve seen everything in our new ```Airport``` class before, but the changes to the ```origin``` and ```destination``` fields within the ```Flight``` class are new to us:

- We specify that the ```origin``` and ```destination``` fields are each [Foreign Keys](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/), which means they refer to another object.
- By entering ```Airport``` as our first argument, we are specifying the type of object this field refers to.
- The next argument, ```on_delete=models.CASCADE``` gives instructions for what should happen if an airport is deleted. In this case, we specify that when an airport is deleted, all flights associated with it should also be deleted. There are [several other options](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete) in addition to CASCADE.
- We provide a [related name](https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.related_name), which gives us a way to search for all flights with a given airport as their origin or destination.

Every time we make changes in ```models.py```, we have to make migrations and then migrate. Note that you may have to delete your existing flight from New York to London, as it doesn’t fit in with the new database structure.

### ERROR - an invalid foreign key

- Python 3.7.9

```bash
~/repo/CS50-Web-Python-Java/lecture4/airline on  master! ⌚ 0:22:03
$ python manage.py makemigrations                                               527260ms 
Migrations for 'flights':
  flights/migrations/0002_auto_20210219_0222.py
    - Create model Airport
    - Alter field destination on flight
    - Alter field origin on flight
(base) 
~/repo/CS50-Web-Python-Java/lecture4/airline on  master! ⌚ 0:22:26
$ python manage.py migrate                                                         534ms 
Operations to perform:
...
django.db.utils.IntegrityError: The row in table 'flights_flight' with primary key '1' has an invalid foreign key: flights_flight.origin_id contains a value 'New York' that does not have a corresponding value in flights_airport.id.

```

### To solve - The Error

Try to delete all the migration files exept __init__.py and
also delete db.sqlite3. After that run makemigrations and
migrate again - [here the solution](https://stackoverflow.com/a/58684324)

- **NOTE**: Maybe in the python 3.8.1 or above this error does not happen.

```bash
$ python manage.py makemigrations
Migrations for 'flights':
  flights/migrations/0001_initial.py
    - Create model Airport
    - Create model Flight
(base) 
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py migrate                                                                                                                              487ms 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
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
  Applying flights.0001_initial... OK
  Applying sessions.0001_initial... OK
```

Now, let’s try these new models out in the Django shell:

```Bash
$ python manage.py shell

# Import all models
In [1]: from flights.models import *

# Create some new airports
In [2]: jfk = Airport(code="JFK", city="New York")
In [4]: lhr = Airport(code="LHR", city="London")
In [6]: cdg = Airport(code="CDG", city="Paris")
In [9]: nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
In [3]: jfk.save()
In [5]: lhr.save()
In [8]: cdg.save()
In [10]: nrt.save()

# Add a flight and save it to the database
In [10]: f = Flight(origin=jfk, destination=lhr, duration=414)
In [11]: f.save()

# Display some info about the flight
In [14]: f
Out[14]: <Flight: 1: New York (JFK) to London (LHR)>
In [15]: f.origin
Out[15]: <Airport: New York (JFK)>

# Using the related name to query by airport of arrival:
In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>

In [15]: f.origin.city
Out[15]: 'New York'

In [16]: f.origin.code
Out[16]: 'JFK'

In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>
```

### Starting our Application

We can now begin to build an application around this process of using models to interact with a database. Let’s begin by creating an index route for our airline. Inside ```urls.py```:

```bash
~/repo/CS50-Web-Python-Java/lecture4/airline/flights

urls.py:

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
]%                                                                                                                                                             (base)
```


Inside ```views```:

```bash
from django.shortcuts import render
from .models import Flight, Airport

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
```

```bash
## pwd - layout and index file html
$ ~/repo/CS50-Web-Python-Java/lecture4/airline/flights/templates/flights
```
Inside our new ```layout.html``` file:

```bash
~/repo/CS50-Web-Python-Java/lecture4/airline 
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 19, 2021 - 03:24:04
Django version 3.1.6, using settings 'airline.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[19/Feb/2021 03:24:06] "GET /flights/ HTTP/1.1" 200 384
```

![](/lecture4/figures/flights_html.png)

Now, let’s add some more flights to our application by returning to the **Django shell**:

```Bash
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py shell
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.19.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from flights.models import *

# Using the filter command to find all airports based in New York
In [2]: Airport.objects.filter(city="New York")
Out[2]: <QuerySet [<Airport: New York (JFK)>]>

# Using the get command to get only one airport in New York
In [3]: Airport.objects.get(city="New York")
Out[3]: <Airport: New York (JFK)>

# Assigning some airports to variable names:
In [4]: jfk = Airport.objects.get(city="New York")

In [5]: cdg = Airport.objects.get(city="Paris")

# Creating and saving a new flight:
In [6]: f = Flight(origin=jfk, destination=cdg, duration=435)

In [7]: f.save()

```

```bash
# terminal
$ python manage.py runserver

$ google-chrome http://127.0.0.1:8000/flights/
```

![](/lecture4/figures/flights_html_addmore.png)

### Django Admin

Since it is so common for developers to have to create new objects like we’ve been doing in the shell, Django comes with a [default admin interface](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) that allows us to do this more easily. To begin using this tool, we must first create an administrative user:

```Bash
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py createsuperuser
Username (leave blank to use 'andsilva'): andvsilva
Email address: myemail@gmail.com
Password: 
Password (again):
Superuser created successfully.
```

Now, we must add our models to the admin application by entering the ```admin.py``` file within our app, and importing and registering our models. This tells Django which models we would like to have access to in the admin app.

![](/lecture4/figures/login_admin.png)

After loggin in, you’ll be brought to a page like the one below where you can create, edit, and delete objects stored in the database

![](/lecture4/figures/logged_admin.png)


### Add Airport

![](/lecture4/figures/Add_airport.png)

![](/lecture4/figures/history_Add.png)

![](/lecture4/figures/All_airport.png)

### Add Flight

![](/lecture4/figures/Add_flight.png)

Now, let’s add a few more pages to our site. We’ll begin by adding the ability to click on a flight to get more information about it. To do this, let’s create a URL path that includes the ```id``` of a flight:

```Bash

# ADD the path to urls.py
path("<int:flight_id>", views.flight, name="flight")

# FILE urls.py
$ ~/repo/CS50-Web-Python-Java/lecture4/airline/flights/urls.py
```

Then, in ```views.py``` we will create a ```flight``` function that takes in a flight id and renders a new html page:

```Bash
# ADD function to the file views
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })

## FILE views.py 
$ ~/repo/CS50-Web-Python-Java/lecture4/airline/flights/views.py
```

Now we’ll create a template to display this flight information with a link back to the home page

```Bash
# FILE flights.html at flights/templates/flights
{% extends "flights/layout.html" %}

{% block body %}
    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin: {{ flight.origin }}</li>
        <li>Destination: {{ flight.destination }}</li>
        <li>Duration: {{ flight.duration }} minutes</li>
    </ul>
    <a href="{% url 'index' %}">All Flights</a>
{% endblock %}
```

Finally, we need to add the ability to link from one page to another, so we’ll modify our index page to include links:

```Bash
{% extends "flights/layout.html" %}

{% block body %}
    <h1>Flights:</h1>
    <ul>
        {% for flight in flights %}
            <li><a href="{% url 'flight' flight.id %}">Flight {{ flight.id }}</a>: {{ flight.origin }} to {{ flight.destination }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### Many-to-Many Relationships

Now, let’s work on integrating passengers into our models. We’ll create a passenger model to start:

```Bash
# FILE models.py at flights/
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
```

- As we discussed, passengers have a **Many to Many** relationship with flights, which we describe in Django using the ManyToManyField.
- The first argument in this field is the class of objects that this one is related to.
- We have provided the argument ```blank=True``` which means a passenger can have no flights
- We have added a ```related_name``` that serves the same purpose as it did earlier: it will allow us to find all passengers on a given flight.

To actually make these changes, we must make migrations and migrate. We can then register the Passenger model in ```admin.py``` and visit the admin page to create some passengers!

Now that we’ve added some passengers, let’s update our flight page so that it displays all passengers on a flight. We’ll first visit ```views.py``` and update our flight view to provide a list of passengers as context. We access the list using the related name we defined earlier.

```Bash
## terminal
### makemigrations
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py makemigrations
Migrations for 'flights':
  flights/migrations/0002_passenger.py
    - Create model Passenger

### migrate
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying flights.0002_passenger... OK
(base)

# RUN server
$ python manage.py runserver
```

```Bash
# ADD the function to views 
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })
```

Now, add a list of passengers to ```flight.html```:

```Bash
<h2>Passengers:</h2>
<ul>
    {% for passenger in passengers %}
        <li>{{ passenger }}</li>
    {% empty %}
        <li>No Passengers.</li>
    {% endfor %}
</ul>
```

### Add Passenger

![](/lecture4/figures/Add_passenger.png)

### Add Passenger to Flight

![](/lecture4/figures/Add_passenger_toFlight.png)

Now, let’s work on giving visitors to our site the ability to book a flight. We’ll do this by adding a booking route in ```urls.py```:

```Bash
### at flights/
path("<int:flight_id>/book", views.book, name="book")
```

Now, we’ll add a **book function** to ```views.py``` that adds a passenger to a flight:

```Bash
def book(request, flight_id):

    # For a post request, add a new flight
    if request.method == "POST":

        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

```

Next, we’ll add some context to our flight template so that the page has access to everyone who is not currently a passenger on the flight using Django’s ability to [exclude]() certain objects from a query:

```Bash
### ADD this function to the FILE views at flights/
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
```

### Book the passenger to the flight

![](/lecture4/figures/Book_passenger_ToFlight.png)

Another advantage of using the Django admin app is that it is customizable. For example, if we wish to see all aspects of a flight in the admin interface, we can create a new class within ```admin.py``` and add it as an argument when registering the ```Flight``` model:

```Bash
# ADD this class to the FILE admin.py
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

# Register your models here.
admin.site.register(Flight, FlightAdmin)
```

Now, when we visit the admin page for flights, we can see the ```id``` as well


![](/lecture4/figures/flights_origdestdur.png)

Check out [Django’s admin documentation](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) to find more ways to customize the admin app.

```Bash
### FILE admin
### FlightAdmin
### PassengerAdmin

from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
# Register your models here.
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
```
![](/lecture4/figures/change_passenger_flight.png)
### Users

The last thing we’ll discuss in lecture today is the idea of authentication, or allowing users to log in and out of a website. Fortunately, Django makes this very easy for us, so let’s go through an example of how we would do this. We’ll start by creating a new app called ```users```. Here we’ll go through all the normal steps of creating a new app, but in our new ```urls.py``` file, we’ll add a few more routes:

```Bash
## terminal
~/repo/CS50-Web-Python-Java/lecture4/airline
$ python manage.py startapp users
```

```Bash
## urls.py at users/
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
```

Let’s begin by creating a form where a user can log in. We’ll create a ```layout.html``` file as always, and then create a ```login.html``` file which contains a form, and that displays a message if one exists.

Now, in ```users/views.py```, we’ll add three functions:

```Bash
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    # Pass is a simple way to tell python to do nothing.
    pass
```

```Bash
## FILE users/login.html
{% extends "users/layout.html" %}

{% block body %}
    {% if message %}
        <div>{{ message }}</div>
    {% endif %}

    <form action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <input type="text", name="username", placeholder="Username">
        <input type="password", name="password", placeholder="Password">
        <input type="submit", value="Login">
    </form>
{% endblock %}

```

Next, we can head to the admin site and add some users. After doing that, we’ll go back to ```views.py``` and update our ```login_view``` function to handle a ```POST``` request with a username and password:

```Bash
# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")
```

Finally, to allow the user to log out, we’ll update the ```logout_view``` function so that it uses Django’s built-in ```logout``` function:

```Bash
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out"
            })
```

Now that we’re finished, here’s a demonstration of the site

![](/lecture4/figures/login_user.png)

That’s all for this lecture! Next time, we’ll learn our second programming language of the course: JavaScript.

## Useful References

- [SQL Tutorial](https://www.w3schools.com/sql/)
