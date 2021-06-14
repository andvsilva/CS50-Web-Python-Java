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

 
### Instalation

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



### Resources

- [MySQL on Manjaro](https://medium.com/@rshrc/mysql-on-manjaro-973e4bfc4f05)

- [How To Install MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)