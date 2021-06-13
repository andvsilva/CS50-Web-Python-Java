# [Lecture 6 - User Interfaces](https://cs50.harvard.edu/web/2020/weeks/6/)

So far, we’ve discussed how to build simple web pages using HTML and CSS, and how to use Git and GitHub in order to keep track of changes to our code and collaborate with others. We also familiarized ourselves with the Python programming language, started using Django to create web applications, and learned how to use Django models to store information in our sites. We then introduced JavaScript and learned how to use it to make web pages more interactive.

Today, we’ll discuss common paradigms in User Interface design, using JavaScript and CSS to make our sites even more user friendly.

### User Interfaces
A User Interface is how visitors to a web page interact with that page. Our goal as web developers is to make these interactions as pleasant as possible for the user, and there are many methods we can use to do this.

### Single Page Applications
Previously, if we wanted a website with multiple pages, we would accomplish that using different routes in our Django application. Now, we have the ability to load just a single page and then use JavaScript to manipulate the DOM. One major advantage of doing this is that we only need to modify the part of the page that is actually changing. For example, if we have a Nav Bar that doesn’t change based on your current page, we wouldn’t want to have to re-render that Nav Bar every time we switch to a new part of the page.

Let’s look at an example of how we could simulate page switching in JavaScript: [code here](html/simplepage.html)

```bash
# TERMINAL
$ google-chrome simplepage.html
```

```bash
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
```bash
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

```bash
# Add
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
```

And two corresponding routes in [views.py](singlepage/../singlepage1/singlepage/views.py). Notice that the ```section``` route takes in an integer, and then returns a string of text based on that integer as an HTTP Response.

Now, within our [index.html](singlepage/../singlepage1/singlepage/templates/singlepage/index.html) file, we’ll take advantage of AJAX, which we learned about last lecture, to make a request to the server to gain the text of a particular section and display it on the screen:

```bash
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

    1 - Any data associated with the state.
    2 - A title parameter ignored by most web browsers
    3 - What should be displayed in the URL
The other change we make in the above JavaScript is in setting the onpopstate parameter, which specifies what we should do when the user clicks the back arrow. In this case, we want to show the previous section when the button is pressed. Now, the site looks a little more user-friendly:

#### Scroll

In order to update and access the browser history, we used an important JavaScript object known as the [window](https://www.w3schools.com/js/js_window.asp). There are some other properties of the window that we can use to make our sites look nicer:

- ```window.innerWidth```: Width of window in pixels
- ```window.innerHeight```: Height of window in pixels

While the window represents what is currently visible to the user, the [document](https://www.w3schools.com/js/js_htmldom_document.asp) refers to the entire web page, which is often much larger than the window, forcing the user to scroll up and down to see the page’s contents. To work with our scrolling, we have access to other variables:

- ```window.scrollY```: How many pixels we have scrolled from the top of the page
- ```document.body.offsetHeight```: The height in pixels of the entire document.

We can use these measures to determine whether or not the user has scrolled to the end of a page using the comparison ```window.scrollY + window.innerHeight >= document.body.offsetHeight```. The following page, for example, will change the backgroud color to red when we reach the bottom of a page:


#### Infinite Scrool

Changing the background color at the end of the page probable isn't all that useful, but may want to detect that we're at the end of the page if want to implement **infinite scroll**. For example, if you're on a social media site, you don't want to have to load all posts at once, you might want to load the first ten, and then when the user reaches the bottom, load the next then. let's take a look at a **Django application** that could do this. This app has two paths in ```urls.py```

Notice that the posts view requires two arguments: a start point and an end point. In this view, we’ve created our own **API**, which we can test out by visiting the url ```localhost:8000/posts?start=10&end=15```, which returns the following **JSON**:

```bash
{
    "posts": [
        "Post #10",
        "Post #11", 
        "Post #12", 
        "Post #13", 
        "Post #14", 
        "Post #15"
    ]
}
```

```bash
# Terminal

$ cd scroll/
$ python manage.py runserver
$ python 
google-chrome http://127.0.0.1:8000/

http://127.0.0.1:8000/posts?start=10&end=15

### You will see in the browser one Javascript Object:
{"posts": ["Post #10", "Post #11", "Post #12", "Post #13", "Post #14", "Post #15"]}
```

Now, in the ```index.html``` template that the site loads, we start out with only an empty ```div``` in the body and some styling. Notice that we load our static files at the beginning, and then we reference a JavaScript file within our ```static``` folder.

Now with JavaScript, we’ll wait until a user scrolls to the end of the page and then load more posts using our **API** - [index.html](scroll/posts/templates/posts/index.html)

Now, we’ve created a site with infinite scroll!

#### Animation

Another way we can make our sites a bit more interesting is by adding some animation to them. It turns out that in addition to providing styling, **CSS makes it easy for us to animate HTML elements**.

To create an animation in CSS, we use the format below, where the animation specifics can include starting and ending styles (```to``` and ```from```) or styles at different stages in the duration (anywhere from ```0%``` to ```100%```). For example:

```bash
@keyframes animation_name {
    from {
        /* Some styling for the start */
    }

    to {
        /* Some styling for the end */
    }
}
```

or: 

```bash
@keyframes animation_name {
    0% {
        /* Some styling for the start */
    }

    75% {
        /* Some styling after 3/4 of animation */
    }

    100% {
        /* Some styling for the end */
    }
}
```

Then, to apply an animation to an element, we include the ```animation-name```, the ```animation-duration``` (in seconds), and the ```animation-fill-mode``` (typically ```forwards```). **For example, here’s a page where a title grows when we first enter the page:** [animate.html](html/animate.html)


We can do more than just manipulate size: **the below example shows how we can change the position of a heading just by changing a few lines:** [animate1.html](html/animate1.html)

Now, let’s look at setting some intermediate CSS properties as well. We can specify the style at any percentage of the way through an animation. In the below example we’ll move the title from left to right, and then back to left by altering only the animation from above


```bash
@keyframes move {
    0% {
        left: 0%;
    }
    50% {
        left: 50%;
    }
    100% {
        left: 0%;
    }
}
```

If we want to repeat an animation multiple times, we can change the ```animation-iteration-count``` to a number higher than one (or even infinite for endless animation). There are many [animation properties](https://www.w3schools.com/cssref/css3_pr_animation.asp) that we can set in order to change different aspects of our animation.

In addition to CSS, we can use JavaScript to further control our animations. Let’s use our moving header example (with infinite repetition) to show how we can create a button that starts and stops the animation. Assuming we already have an animation, **button, and heading, we can add the following script to start and pause the animation:** [animate2.html](html/animate2.html)

Now, let’s look at how we can apply our new knowledge of animations to the posts page we made earlier. Specifically, let’s say we want the ability to hide posts once we’re done reading them. Let’s imagine a Django project identical to the one we just created, but with some slightly different HTML and JavaScript. The first change we’ll make is to the ```add_post``` function, this time also adding a button to the right side of the post: [index.html](hide/posts/templates/posts/index.html)

```bash
// file: hide/posts/templates/posts/index.html

// Add a new post with given contents to DOM
function add_post(contents) {

    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = `${contents} <button class="hide">Hide</button>`;

    // Add post to DOM
    document.querySelector('#posts').append(post);
};
```

Now, we’ll work on hiding a post when the ```hide``` button is clicked. To do this, we’ll add an event listener that is triggered whenever a user clicks anywhere on the page. We then write a function that takes in the ```event``` as an argument, which is useful because we can use the ```event.target``` attribute to access what was clicked on. We can also use the ```parentElement``` class to find the parent of a given element in the DOM.

```bash
// file: hide/posts/templates/posts/index.html

// If hide button is clicked, delete the post
document.addEventListener('click', event => {

    // Find what was clicked on
    const element = event.target;

    // Check if the user clicked on a hide button
    if (element.className === 'hide') {
        element.parentElement.remove()
    }
    
});
```
#### Django application

```bash
# Terminal
$ cd hide/ # Django application
$ python manage.py runserver
```

We can now see that we’ve implemented the hide button, but it doesn’t look as nice as it possible could. Maybe we want to have the post fade away and shrink before we remove it. In order to do this, we’ll first create a CSS animation. The animation below will spend 75% of its time changing the ```opacity``` from 1 to 0, which esentially makes the post fade out slowly. It then spends the rest of the time moving all of its ```height```-related attributes to 0, effectively shrinking the post to nothing.

```bash
// file: hide/posts/templates/posts/index.html

@keyframes hide {
    0% {
        opacity: 1;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    75% {
        opacity: 0;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    100% {
        opacity: 0;
        height: 0px;
        line-height: 0px;
        padding: 0px;
        margin-bottom: 0px;
    }
}
```

Next, we would add this animation to our post’s CSS. Notice that we initially set the ```animation-play-state``` to paused, meaning the post will not be hidden by default.

```bash
// file: hide/posts/templates/posts/index.html

.post {
    background-color: #77dd11;
    padding: 20px;
    margin-bottom: 10px;
    animation-name: hide;
    animation-duration: 2s;
    animation-fill-mode: forwards;
    animation-play-state: paused;
}
```

Finally, we want to be able to start the animation once the ```hide``` button has been clicked, and then remove the post. We can do this by editing our JavaScript from above:

```bash
// file: hide/posts/templates/posts/index.html

// If hide button is clicked, delete the post
document.addEventListener('click', event => {
    
    // Find what was clicked on
    const element = event.target;

    // Check if the user clicked on a hide button
    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () =>  {
            element.parentElement.remove();
        });
    }
});
```

```bash
# Terminal
$ cd hide/ # Django application
$ python manage.py runserver &
$ google-chrome http://127.0.0.1:8000/ 
```

As you can see above, the hide functionality now looks a lot nicer!

### [React - A JavaScript library for building user interfaces](https://reactjs.org/)

At this point, you can imagine how much JavaScript code would have to go into a more complicated website. We can mitigate how much code we actually need to write by employing a JavaScript framework, just as we employed Bootstrap as a CSS framework to cut down on the amount of CSS we actually had to write. One of the most popular JavaScript frameworks is a library called *React*.

So far in this course, we’ve been using **imperative programming** methods, where we give the computer a set of statements to execute. For example, to update the counter in an HTML page we might have have code that looks like this:

View:

```bash
<h1>0</h1>
```

Logic:
```bash
let num = parseInt(document.querySelector("h1").innerHTML);
num += 1;
document.querySelector("h1").innerHTML = num;
```

React allows us to use ```declarative programming```, which will allow us to simply write code explaining *what* we wish to display and not worry about *how* we’re displaying it. In React, a counter might look a bit more like this:

View:

```bash
<h1>{num}</h1>
```

Logic:

```bash
num += 1;
```

The React framework is built around the idea of components, each of which can have an underlying state. A component would be something you can see on a web page like a post or a navigation bar, and a state is a set of variables associated with that component. The beauty of React is that when the state changes, React will automatically change the DOM accordingly.

There are a number of ways to use React, (including the popular [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) command published by Facebook) but today we’ll focus on getting started directly in an HTML file. To do this, we’ll have to import three JavaScript Packages:

- ```React```: Defines components and their behavior
- ```ReactDOM```: Takes React components and inserts them into the DOM
- ```Babel```: Translates from [JSX](https://reactjs.org/docs/introducing-jsx.html), the language in which we’ll write in React, to plain JavaScript that our browsers can interpret. JSX is very similar to JavaScript, but with some additional features, including the ability to represent HTML inside of our code.

Let’s dive in and create our first React application! [react.html](html/react.html)

Since this is our first React app, let’s take a detailed look at what each part of this code is doing:

- In the three lines above the title, we import the latest versions of React, ReactDom, and Babel.
- In the body, we include a single ```div``` with an ```id``` of ```app```. We almost always want to leave this empty, and fill it in our react code below.
- We include a script tag where we specify that ```type="text/babel"```. This signals to the browser that the following script needs to be translated using Babel.
- Next, we create a component called App that extends React.Component. Components in React are represented as JavaScript classes, which are similar to the Python classes we learned about earlier. This allows us to start creating a component without rewriting a lot of code included in the React.Component class definition.
- Inside of our component, we include a render function. All componenets are required to have this function, and whatever is returned within the function will be added to the DOM, in this case, we are simply adding <div>Hello!</div>.
- The last line of our script employs the ReactDOM.render function, which takes two arguments:
  1. A component to render
  2. An element in the DOM inside of which the component should be rendered

Now that we understant what the code is doing, we can take a look at the resulting webpage:

One useful feature of React is the ability to render components within other components. To demonstrate this, let’s create another component called ```Hello```:

```bash
class Hello extends React.Component {
    render() { 
        return (
            <h1>Hello</h1>
        );
    }
}
```

And now, let’s render three ```Hello``` components inside of our ```App``` component:

```bash
class App extends React.Component {
    render() { 
        return (
            <div>
                <Hello />
                <Hello />
                <Hello />
            </div>
        );
    }
}
```

This gives us a page that looks like: [react1.html](html/react1.html)

So far, the components haven’t been all that interesting, as they are all exactly the same. We can make these components more flexible by adding additional properties (**props** in React terms) to them. For example, let’s say we wish to say hello to three different people. We can provide those people’s names in a method that looks similar to HTML tags:

```bash
class App extends React.Component {
    render() { 
        return (
            <div>
                <Hello name="Harry" />
                <Hello name="Ron" />
                <Hello name="Hermione" />
            </div>
        );
    }
}
```

```bash
class Hello extends React.Component {
    render() { 
        return (
            <h1>Hello, {this.props.name}!</h1>
        );
    }
}
```


Now, our page displays the three names: [react2.html](html/react2.html)

Now, let’s see how we can use React to re-implement the counter page we built when first working with JavaScript. Our overall structure will remain the same, but inside of our ```App``` class, we’ll include a ```constructor``` method, a method called when the component is first created. This constructor will always take ```props``` as an argument, and the first line will always be ```super(props)```; which sets up the object based on the ```React.Component``` class. Next, we initialize the state of the component, which is a JavaScript object that stores information about the component. At the moment, we’ll just set ```count``` to be 0.

```bash
constructor(props) {
    super(props);
    this.state = {
        count: 0
    };
}
```

Now, we can work on the render function, where we’ll specify a header and a button. We’ll also add an event listener for when the button is clicked, which React does using the onClick attribute:

```bash
render() { 
    return (
        <div>
            <h1>{this.state.count}</h1>
            <button onClick={this.count}>Count</button>
        </div>
    );
}
```

Finally, let’s define the count function. To do this, we’ll use the this.setState function, which can take as argument a function from the old state to the new state.

```bash
count = () => {
    this.setState(state => ({
        count: state.count + 1
    }))
}
```

Now we have a functioning counter site: [counter.html](html/counter.html)

#### Addition

Now that we have a feel for the React framework, let’s work on using what we’ve learned to build a game-like site where users will solve addition problems. We’ll begin by creating a new file with the same setup as our other React pages. To start building this application, let’s think about what we might want to keep track of in the state. We should include anything that we think might change while a user is on our page. Let’s set the state to include:

- ```num1```: The first number to be added
- ```num2```: The second number to be added
- ```response```: What the user has typed in
- ```score```: How many questions the user has answered correctly.

Now, our constructor will look like this:

```bash
constructor(props) {
    super(props);
    this.state = {
        num1: 1,
        num2: 1,
        response: '',
        score: 0
    };
}
```

Now, using the values in the state, let’s create a render function with what we wish to display

```bash
render() { 
    return (
        <div>
            <div>{this.state.num1} + {this.state.num2}</div>
            <input type="text" value={this.state.response} />
            <div> Score: {this.state.score}</div>
        </div>
    );
}
```

At this point, the user cannot type anything in the input box because its value is fixed as ```this.state.response``` which is currently the empty string. To fix this, let’s add an ```onChange``` attribute to the input box, and set it equal to a function called ```updateResponse```

```bash
onChange={this.updateResponse}
```

Now, we’ll have to define the ```updateResponse``` function, which takes in the event that triggered the function, and sets the ```response``` to the current value of the input. This function allows the user to type, and stores whatever has been typed in the ```state```.

```bash
updateResponse = (event) => {
    this.setState({
        response: event.target.value
    });
}
```

Now, let’s add the ability for a user to submit a problem. We’ll first add another event listener and link it to a function we’ll write next:

```bash
onKeyPress={this.inputKeyPress}
```

Now, we’ll define the ```inputKeyPress``` function. In this function, we’ll first check whether the ```Enter``` key was pressed, and then check to see if the answer is correct. When the user is correct, we want to increase the score by 1, choose random numbers for the next problem, and clear the response. If the answer is incorrect, we want to decrease the score by 1 and clear the response.

```bash
inputKeyPress = (event) => {
                    
    // Check if the Enter key was pressed
    if (event.key === 'Enter') {

        // Extract answer
        const answer = parseInt(this.state.response)

        // Check if answer is correct
        if (answer === this.state.num1 + this.state.num2) {
            this.setState(state => ({
                score: state.score + 1,
                num1: Math.ceil(Math.random() * 10),
                num2: Math.ceil(Math.random() * 10),
                response: ''
            }));
        } else {
            this.setState(state => ({
                score: state.score - 1,
                response: ''
            }));
        }
    }
}
```

To put some finishing touches on the application, let’s add some style to the page. We’ll center everything in the app, and then make the problem larger by adding an ```id``` of ```problem``` to the div containing the problem, and then adding the following CSS to a style tag:

```bash
#app {
    text-align: center;
    font-family: sans-serif;
}

#problem {
    font-size: 72px;
}
```

Finally, let’s add the ability to win the game after gaining 10 points. To do this, we’ll add a condition to the ```render``` function, returning something completely different once we have 10 points:

```bash
render() { 

    // Check if the score is 10
    if (this.state.score === 10) {
        return (
            <div id="winner">
                You won!
            </div>
        );
    }

    return (
        <div>
            <div id="problem">{this.state.num1} + {this.state.num2}</div>
            <input onKeyPress={this.inputKeyPress} onChange={this.updateResponse} type="text" value={this.state.response} />
            <div> Score: {this.state.score}</div>
        </div>
    );
}
```

To make the win more exciting, we’ll add some style to the alternative div as well:

```bash
#winner {
    font-size: 72px;
    color: green;
}
```

Now, let’s take a look at our application: [addition.html](html/addition.html)

That’s all for lecture today! Next time, we’ll talk about some best practices for building larger web applications.