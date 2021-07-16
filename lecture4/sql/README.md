## [Structured Query Language - SQL ](https://www.youtube.com/watch?v=zbMHLJ0dY4w&t=79s)

### Features of SQL:

- Has well defined standards
- Is easy to learn
- With the help of SQL, one can create multiple views
- Portability of code in SQl is a prominent feature

### Database

- Distributed
- Object Oriented
- Centralized
- Operational
- Graph
- NoSQL
- Cloud
- Relational

### Key elements of SQL for Data Science

- Relational Database Model
- SQL Query Commands
- Handling Null Values
- Working with Indexes
- Joins
- Keys Constraints
- Working with SubQuery
- Creating Tables and Databases


### SQL with Python

#### Python provides multiple libraries

- [SQLite](SQLite)
- [PostgreSQL](PostgreSQL)
- [MySQL](MySQL)

Data Scientists need to connect a SQL database so that data coming from the web application can be stored. It also helps to communicate between different data sources.

They will be able to use your Python skills to manipulate data stored in a SQL database. **They don’t need a CSV file.**

#### MySQL with Python

MySQL database consist two-step process for creating a database:

1. Make a connection to a MySQL server.

2. Execute separate queries to create the database and process data.

```Bash
pip install mysql-connector-python
```
 
### Installation

```Bash
# install for manjaro
$ sudo pacman -S mysql

$ sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

$ sudo systemctl start mariadb

$ sudo mysql_secure_installation

$ sudo systemctl status mariadb
```

### Usage

```Bash
$ mysql                                                     43ms 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 10.5.10-MariaDB Arch Linux

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| test               |
+--------------------+
2 rows in set (0.001 sec)

MariaDB [(none)]> CREATE DATABASE mydatabase;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydatabase         |
| mysql              |
| performance_schema |
| test               |
+--------------------+
5 rows in set (0.001 sec)

MariaDB [(none)]> USE mydatabase;
Database changed
MariaDB [mydatabase]> CREATE TABLE books( title VARCHAR(50) NOT NULL,  price INT NOT NULL, language VARCHAR(50) DEFAULT "ENGLISH", author VARCHAR(60) NOT NULL);
Query OK, 0 rows affected (0.018 sec)

MariaDB [mydatabase]> DESCRIBE books;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| title    | varchar(50) | NO   |     | NULL    |       |
| price    | int(11)     | NO   |     | NULL    |       |
| language | varchar(50) | YES  |     | ENGLISH |       |
| author   | varchar(60) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
 
MariaDB [mydatabase]> INSERT INTO books VALUE("Book Title", 50.00, "Hindi", "Author Name");
Query OK, 1 row affected (0.004 sec)

MariaDB [mydatabase]> SELECT * FROM books;
+------------+-------+----------+-------------+
| title      | price | language | author      |
+------------+-------+----------+-------------+
| Book Title |    50 | Hindi    | Author Name |
+------------+-------+----------+-------------+
1 row in set (0.001 sec)

```

## Pandasql - SQL Queries in python


```bash
'pandasql' allow you to query pandas DataFrames using SQL syntax.
It wokrs similar to sqldf in R. pandasql seeks to provide a more
familiar way of manipulating and cleaning data for people new 
to Python or pandas.
```

## Installation Instructions

```bash
# terminal.
pip install -U pandasql

# jupyter notebook - running in any cell.
!pip install -U pandasql
```

## Basics

```bash
sqldf - main function - two parameters

- A SQL query in string format 
- A set of session/environment variables (globals()) or locals())
```

## Import the library

```bash
from pandasql import sqldf

mysql = lambda q: sqldf(q, globals())
```

## Syntax

```bash
pandasql uses the SQLite syntax

# https://www.sqlite.org/lang.html
# SQL As Understood By SQLite

from pandasql import sqldf
mysql = lambda q: sqldf(q, globals()) mysql("SQL Query")

# or

from pandasql import sqldf
mysql = lambda q: sqldf(q, globals()) query = ''' SQL Query ''' mysql(query)
```

## Import libraries and Data

```bash
>>> import numpy as np
>>> import pandas as pd
>>> import pandasql as psql
>>> from pandasql import sqldf
>>> birth = psql.load_births()
>>> birth

##  Birth Data Set 
>>> birth = psql.load_births()
>>> birth
          date  births
0   1975-01-01  265775
1   1975-02-01  241045
2   1975-03-01  268849
3   1975-04-01  247455
4   1975-05-01  254545
..         ...     ...
403 2012-08-01  359554
404 2012-09-01  361922
405 2012-10-01  347625
406 2012-11-01  320195
407 2012-12-01  340995

[408 rows x 2 columns]

##  Meat Data Set 
>>> meat = psql.load_meat()
>>> meat
          date    beef   veal  ...  broilers  other_chicken  turkey
0   1944-01-01   751.0   85.0  ...       NaN            NaN     NaN
1   1944-02-01   713.0   77.0  ...       NaN            NaN     NaN
2   1944-03-01   741.0   90.0  ...       NaN            NaN     NaN
3   1944-04-01   650.0   89.0  ...       NaN            NaN     NaN
4   1944-05-01   681.0  106.0  ...       NaN            NaN     NaN
..         ...     ...    ...  ...       ...            ...     ...
822 2012-07-01  2200.8    9.5  ...    3127.0           43.4   497.2
823 2012-08-01  2367.5   10.1  ...    3317.4           51.0   530.1
824 2012-09-01  2016.0    8.8  ...    2927.1           43.7   453.1
825 2012-10-01  2343.7   10.3  ...    3335.0           43.8   579.9
826 2012-11-01  2206.6   10.1  ...    3006.7           37.5   515.3

[827 rows x 8 columns]

>>> sqldatabase = psql.sqldf("SELECT * FROM meat LIMIT 5;")
>>> sqldatabase
                         date   beef   veal    pork  lamb_and_mutton broilers other_chicken turkey
0  1944-01-01 00:00:00.000000  751.0   85.0  1280.0             89.0     None          None   None
1  1944-02-01 00:00:00.000000  713.0   77.0  1169.0             72.0     None          None   None
2  1944-03-01 00:00:00.000000  741.0   90.0  1128.0             75.0     None          None   None
3  1944-04-01 00:00:00.000000  650.0   89.0   978.0             66.0     None          None   None
4  1944-05-01 00:00:00.000000  681.0  106.0  1029.0             78.0     None          None   None
>>> mysqldb = psql.sqldf("SELECT * FROM birth LIMIT 5;")
>>> mysqldb
                         date  births
0  1975-01-01 00:00:00.000000  265775
1  1975-02-01 00:00:00.000000  241045
2  1975-03-01 00:00:00.000000  268849
3  1975-04-01 00:00:00.000000  247455
4  1975-05-01 00:00:00.000000  254545

## We can use the power of SQL JOIN here with pandas DataFrame
>>> query = '''
... SELECT m.date, m.beef, m.veal, m.pork, b.births
... FROM meat AS m
... INNER JOIN
... birth AS b
... ON m.date = b.date;
... '''
>>> mysql_query = psql.sqldf(query)
>>> mysql_query
                           date    beef  veal    pork  births
0    1975-01-01 00:00:00.000000  2106.0  59.0  1114.0  265775
1    1975-02-01 00:00:00.000000  1845.0  50.0   954.0  241045
2    1975-03-01 00:00:00.000000  1891.0  57.0   976.0  268849
3    1975-04-01 00:00:00.000000  1895.0  60.0  1100.0  247455
4    1975-05-01 00:00:00.000000  1849.0  59.0   934.0  254545
..                          ...     ...   ...     ...     ...
402  2012-07-01 00:00:00.000000  2200.8   9.5  1721.8  368450
403  2012-08-01 00:00:00.000000  2367.5  10.1  1997.9  359554
404  2012-09-01 00:00:00.000000  2016.0   8.8  1911.0  361922
405  2012-10-01 00:00:00.000000  2343.7  10.3  2210.4  347625
406  2012-11-01 00:00:00.000000  2206.6  10.1  2078.7  320195

[407 rows x 5 columns]

```

## Read Data using SQL Query

### Resources

- [MySQL on Manjaro](https://medium.com/@rshrc/mysql-on-manjaro-973e4bfc4f05)

- [How To Install MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

- [SQL For Data Science: A Beginner’s Guide!](https://www.analyticsvidhya.com/blog/2021/06/sql-for-data-science-a-beginners-guide/)

- [Pandasql -The Best Way to Run SQL Queries in Python](https://www.analyticsvidhya.com/blog/2021/07/pandasql-best-way-to-run-sql-queries-and-codes-in-jupyter-notebook-using-python/)