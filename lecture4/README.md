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

## Useful References

- [SQL Tutorial](https://www.w3schools.com/sql/)
