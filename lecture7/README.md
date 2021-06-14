# [Lecture 7 - Testing, CI/CD](https://cs50.harvard.edu/web/2020/weeks/7/)

- [Introduction]()
- [Testing]()
- [Assert]()
- [Test-Driven Development]()
- [Unit Testing]()
- [Django Testing]()
- [Client Testing]()
- [Selenium]()
- [CI/CD]()
- [GitHub Actions]()
- [Docker]()

## Introduction

- So far, we’ve discussed how to build simple web pages using HTML and CSS, and how to use Git and GitHub in order to keep track of changes to our code and collaborate with others. We also familiarized ourselves with the Python programming language, started using Django to create web applications, and learned how to use Django models to store information in our sites. We then introduced JavaScript and learned how to use it to make web pages more interactive, and talked about using animation and React to further improve our User Interfaces.

- Today, we’ll learn about best practices when if comes to working on and launching larger projects.

## Testing

One important part of the software development process is the act of **Testing** the code we’ve written to make sure everything runs as we expect it to. In this lecture, we’ll discuss several ways that we can improve the way we test our code.

## Assert

One of the simplest ways we can run tests in Python is by using the ```assert``` command. This command is followed by some expression that should be ```True```. If the expression is ```True```, nothing will happen, and if it is ```False```, an exception will be thrown. Let’s look at how we could incorporate command to test the square function we wrote when first learning Python. When the function is written correctly, nothing happens as the ```assert``` is ```True```

```bash
def square(x):
    return x * x

assert square(10) == 100

""" Output:

"""
```

And then when it is written incorrectly, an exception is thrown.

```bash
def square(x):
    return x + x

assert square(10) == 100

""" Output:
Traceback (most recent call last):
  File "assert.py", line 4, in <module>
    assert square(10) == 100
AssertionError
"""
```

## Test-Driven Development

As you begin building larger projects, you may want to consider using **test-driven development**, a development style where every time you fix a bug, you add a test that checks for that bug to a growing set of tests that are run every time you make changes. This will help you to make sure that additional features you add to a project don’t interfere with your existing features.

Now, let’s look at a slightly more complex function, and think about how writing tests can help us to find errors. We’ll now write a function called ```is_prime``` that returns ```True``` if and only if its input is prime:

```bash
import math

def is_prime(n):

    # We know numbers less than 2 are not prime
    if n < 2:
        return False

    # Checking factors up to sqrt(n)
    for i in range(2, int(math.sqrt(n))):

        # If i is a factor, return false
        if n % i == 0:
            return False

    # If no factors were found, return true
    return True
```

Now, let’s take a look at a function we’ve written to test our prime function:

```bash
## file: test0

from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")
```
At this point, we can go into our python interpreter and test out some values:

```bash
$ python                                                                     214ms 
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> test_prime(5, True)
>>> test_prime(10, False)
>>> test_prime(25, False)
ERROR on is_prime(25), expected False
```

We can see from the output above that 5 and 10 were correctly identified as prime and not prime, but 25 was incorrectly identified as prime, so there must be something wrong with our function. Before we look into what is wrong with our function though, let’s look at a way to automate our testing. One way we can do this is by creating a **shell script**, or some script that can be run inside our terminal. These files require a .sh extension, so our file will be called tests0.sh. Each of the lines below consists of

1. A ```python3``` to specify the Python version we’re running
2. A ```-c``` to indicate that we wish to run a command
3. A command to run in string format


```bash
python3 -c "from tests0 import test_prime; test_prime(1, False)"
python3 -c "from tests0 import test_prime; test_prime(2, True)"
python3 -c "from tests0 import test_prime; test_prime(8, False)"
python3 -c "from tests0 import test_prime; test_prime(11, True)"
python3 -c "from tests0 import test_prime; test_prime(25, False)"
python3 -c "from tests0 import test_prime; test_prime(28, False)"
```

Now we can run these commands by running ```source runtests.sh or chmod +x runtests.sh and ./runtests.sh``` in our terminal, giving us this result:

```bash
$ source runtests.sh
ERROR on is_prime(8), expected False
ERROR on is_prime(25), expected False
(base) 
```

## Unit Testing

Even though we were able to run tests automatically using the above method, we still might want to avoid having to write out each of those tests. Thankfully, we can use the Python ```unittest``` library to make this process a little bit easier. Let’s take a look at what a testing program might look like for our ```is_prime``` function.




















### Useful resources