# [Lecture 6 - User Interfaces](https://cs50.harvard.edu/web/2020/weeks/6/)

So far, we’ve discussed how to build simple web pages using HTML and CSS, and how to use Git and GitHub in order to keep track of changes to our code and collaborate with others. We also familiarized ourselves with the Python programming language, started using Django to create web applications, and learned how to use Django models to store information in our sites. We then introduced JavaScript and learned how to use it to make web pages more interactive.

Today, we’ll discuss common paradigms in User Interface design, using JavaScript and CSS to make our sites even more user friendly.

### User Interfaces
A User Interface is how visitors to a web page interact with that page. Our goal as web developers is to make these interactions as pleasant as possible for the user, and there are many methods we can use to do this.

### Single Page Applications
Previously, if we wanted a website with multiple pages, we would accomplish that using different routes in our Django application. Now, we have the ability to load just a single page and then use JavaScript to manipulate the DOM. One major advantage of doing this is that we only need to modify the part of the page that is actually changing. For example, if we have a Nav Bar that doesn’t change based on your current page, we wouldn’t want to have to re-render that Nav Bar every time we switch to a new part of the page.

Let’s look at an example of how we could simulate page switching in JavaScript: [code here](html/simplepage.html)
