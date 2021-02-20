# [Lecture 5 - JavaScript](https://cs50.harvard.edu/web/2020/weeks/5/)

Today, we’ll introduce a new programming language: ```JavaScript```.

Recall that in most online interactions, we have a client/user that sends an HTTP Request to a server, which sends back an HTTP Response. All of the Python code we’ve written so far using Django has been running on a server. JavaScript will allow us to run code on the client side, meaning no interaction with the server is necessary while it’s running, allowing our websites to become much more interactive.

In order to add some JavaScript to our page, we can add a pair of ```<script>``` tags somewhere in our HTML page. We use ```<script>``` tags to signal to the browser that anything we write in between the two tags is JavaScript code we wish to execute when a user visits our site. Our first program might look something like this:

```Bash
alert('Hello, world!');
```

The ```alert``` function in JavaScript displays a message to the user which they can then dismiss. To show where this would fit into an actual HTML document, here’s an example of a simple page with some JavaScript: [hello.html](/html/hello.html)

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