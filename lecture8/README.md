# [Lecture 8 - Scalability and Security](https://cs50.harvard.edu/web/2020/weeks/8/)

<!--ts-->
- [Introduction]()
- [Scalability]()
- [Scaling]()
- [Load Balancing]()
- [Autoscaling]()
  - [Server Failure]()
- [Scaling Databases]()
  - [Database Replication]()
- [Caching]()
- [Security]()
  - [Git and GitHub]()
- [HTML]()
- [HTTPS]()
  - [Secret-Key Cryptography]()
  - [Public-Key Cryptography]()
- [Databases]()
  - [APIs]()
  - [Environment Variables]()
- [JavaScript]()
  - [Cross-Site Request Forgery]()
- [What’s next?]()

## Introduction

- So far, we’ve discussed how to build simple web pages using HTML and CSS, and how to use Git and GitHub in order to keep track of changes to our code and collaborate with others. We also familiarized ourselves with the Python programming language, started using Django to create web applications, and learned how to use Django models to store information in our sites. We then introduced JavaScript and learned how to use it to make web pages more interactive, and talked about using animation and React to further improve our User Interfaces. We then talked about some best practices in software development and some technologies commonly used to achieve those best practices.

- Today, in our final lecture, we’ll discuss the issues of scaling up and securing our web applications.

## Scalability

So far in this course, we’ve built applications that are run only locally on our computers, but eventually, we’ll want to launch our sites so they can be accessed by anyone on the internet. In order to do this, we run our sites on servers, which are physical pieces of hardware dedicated to running applications. Servers can either be on-premise (We own and maintain physical servers where our application is hosted) or on the cloud (servers are owned by a different company such as Amazon or Google, and we pay to rent server space where our application is hosted). There are benefits and drawbacks to both options:

  - **Customization**: Hosting your own servers gives you the ability to decide exactly how they work, allowing for more flexibility than cloud-based hosting.
  
  - **Expertise**: It is much simpler to host an application on the cloud than it is to maintain your own servers.
  
  - **Cost**: Since server-hosting sites need to make a profit, they will charge you more than it costs them to maintain their on-premise servers, making cloud-based servers more expensive. However, the startup costs of running on-premise servers can be high, as you need to purchase physical servers and potentially hire someone with the expertise to set them up.
   
  - **Scalability**: Scaling is typically easier when hosting on the cloud. For example, if we host a site on premise that gets 500 visits per day, and then it starts getting 500,000 visits per day, we would have to order and setup more physical servers to handle the requests, and in the mean time many of our users will not be able to access the site. Most cloud hosting sites will allow you to rent server space flexibly, paying based on how much action your site sees.

When a user sends an HTTP request to this server, the server should send back a response. However, in reality, most servers get far more than one request at a time, as depicted to ```Server```

This is where we run into the issue of scalability. A single server can handle only so many requests at once, forcing us to make plans about what to do when our one server is overworked. Whether we decide to host on premise or on the cloud, we have to determine how many requests a server can handle without crashing, which can be done using any number of **benchmarking** tools including Apache Bench.

## Scaling

Once we have some upper limit on how many requests our server can handling, we can begin thinking about how we want to handle the scaling of our application. Two different approaches to scaling include:

1. **Vertical Scaling**: In vertical scaling, when our server is overwhelmed we simply buy or build a larger server. This strategy is limited however, as there is an upper limit on how powerful a single server can be.
2. **Horizontal Scaling**: In horizontal scaling, when our server is overwhelmed we buy or build more servers, and then split the requests among our multiple servers.

## Load Balancing

When we use horizontal scaling, we are faced with the additional problem of how we decide which servers are assigned to which requests. We answer that question by employing a load balancer, which is another piece of hardware that intercepts incoming requests, and then assigns those requests to one of our servers. There are a number of different methods for deciding which server receives which request, but here are a few:

- **Random**: In this simple method, the load balancer will decide randomly which server it should assign a request to.
- **Round-Robin**: In this method, the load balancer will alternate which server receives an incoming request. If we have three servers, the first request might go to server A, the second to server B, the third to server C, and the fourth back to server A.
- **Fewest Connections**: In this method, the load balancer looks for the server that is currently handling the fewest requests, and assigns the incoming request to that server. This allows us to make sure we’re not overworking one particular server, but it also takes longer for the load balancer to calculate the number of requests each server is currently handling than it dows for it to simply choose a random server.