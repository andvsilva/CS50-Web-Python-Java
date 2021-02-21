# [Lecture 5 - JavaScript](https://cs50.harvard.edu/web/2020/weeks/5/)

Today, we’ll introduce a new programming language: ```JavaScript```.

Recall that in most online interactions, we have a client/user that sends an HTTP Request to a server, which sends back an HTTP Response. All of the Python code we’ve written so far using Django has been running on a server. JavaScript will allow us to run code on the client side, meaning no interaction with the server is necessary while it’s running, allowing our websites to become much more interactive.

In order to add some JavaScript to our page, we can add a pair of ```<script>``` tags somewhere in our HTML page. We use ```<script>``` tags to signal to the browser that anything we write in between the two tags is JavaScript code we wish to execute when a user visits our site. Our first program might look something like this:

```Bash
alert('Hello, world!');
```

The ```alert``` function in JavaScript displays a message to the user which they can then dismiss. To show where this would fit into an actual HTML document, here’s an example of a simple page with some JavaScript: [hello alert](html/hello_alert.html)

### Event

One feature of JavaScript that makes it helpful for web programming is that it supports [Event-Driven Programming.](https://vsvaibhav2016.medium.com/introduction-to-event-driven-programming-28161b79c223).

An event can be almost anything including a button being clicked, the cursor being moved, a response being typed, or a page being loaded. Just about everything a user does to interact with a web page can be thought of as an event. In JavaScript, we use [Event Listeners](https://www.w3schools.com/js/js_htmldom_eventlistener.asp) that wait for certain events to occur, and then execute some code.

Let’s begin by turning our JavaScript from above into a [function](https://www.w3schools.com/js/js_functions.asp) called hello:

```Bash
function hello() {
    alert('Hello, world!')
}
```

Now, let’s work on running this function whenever a button is clicked. To do this, we’ll create an HTML button in our page with an onclick attribute, which gives the browser instructions for what should happen when the button is clicked:

```Bash
<button onclick="hello()">Click Here</button>
```

These changes to our code

### Variables

JavaScript is a programming language just like Python, C, or any other language you’ve worked with before, meaning it has many of the same features as other languages including variables. There are three keywords we can use to assign values in JavaScript:

- ```var```: used to define a variable globally

```Bash
var age = 20;
```

- ```let```: used to define a variuables that is limited in scope to the current block such as a function or loop

```Bash
let counter = 1;
```

- ```const```: used to define a value that will not change

```Bash
const PI = 3.14;
```

For an example of how we can use a variable, let’s take a look at a page that keeps track of a counter: [counter.html](html/counter.html)

### querySelector

In addition to allowing us to display messages through alerts, JavaScript also allows us to change elements on the page. In order to do this, we must first introduce a function called ```document.querySelector```. This function searches for and returns elements of the DOM. For example, we would use:

```Bash
let heading = document.querySelector('h1');
```

to extract a heading. Then, to manipulate the element we’ve recently found, we can change its ```innerHTML``` property:

```Bash
heading.innerHTML = `Goodbye!`;
```

Just as in Python, we can also take advantage of conditions in JavaScript. For example, let’s say rather than always changing our header to Goodbye!, we wish to toggle back and forth between Hello! and Goodbye!. Our page might then look something like the one below. Notice that in JavaScript, we use ```===``` as a stronger comparison between two items which also checks that the objects are of the same type. We typically want to use ```===``` whenever possible. Please the file [hello goodbye](/html/hello_goodbye.html)

### DOM Manipulation

Let’s use this idea of DOM manipulation to improve our counter page: [counter DOM](html/counter_dom.html)

We can make this page even more interesting by displaying an alert every time the counter gets to a multiple of ten. In this alert, we’ll want to format a string to customize the message, which in JavaScript we can do using [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). Template literals requre that there are backticks (``` ` ```) around the entire expression and a ```$``` and curly braces around any substitutions. For example, let’s change our count function [counter DOM](html/counter_dom.html)

we’ve used an [anonymous function](https://www.w3schools.com/js/js_function_definition.asp), which is a function that is never given a name. Putting all of this together, our JavaScript now looks like this: [counter DOM](html/counter_dom.html)