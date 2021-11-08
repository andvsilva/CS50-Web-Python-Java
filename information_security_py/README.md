# Information Secure with Python (Course - DIO)

## Python security


What is information security simple definition?

Information security refers to the processes and methodologies
which are designed and implemented to protect print, electronic
or any other form of confidential, private and sensitive
information or data from unauthorized access, use, misuse, disclosure, destruction, modification, or disruption.Jan 17, 2020


## 3 Principles:

- Confidentiality
- Integrity
- Availability

### What is ICMP?

```bash
ICMP - 'Internet Control Message Protocol' 
```

ICMP (Internet Control Message Protocol) is an error-reporting protocol that network devices such as routers use to generate error messages to the source IP address when network problems prevent delivery of IP packets. ICMP creates and sends messages to the source IP address indicating that a gateway to the internet, such as a router, service or host, cannot be reached for packet delivery. Any IP network device has the capability to send, receive or process [ICMP](https://www.techtarget.com/searchnetworking/definition/ICMP) messages.

```bash
# see more info using the command man
$ man ping
NAME
       ping - send ICMP ECHO_REQUEST to network hosts

SYNOPSIS
       ping [-aAbBdDfhLnOqrRUvV46] [-c count] [-F flowlabel] [-i interval] [-I interface] [-l preload] [-m mark] [-M pmtudisc_option] [-N nodeinfo_option]
            [-w deadline] [-W timeout] [-p pattern] [-Q tos] [-s packetsize] [-S sndbuf] [-t ttl] [-T timestamp option] [hop...] {destination}

DESCRIPTION
       ping uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway. ECHO_REQUEST datagrams (“pings”) have an
       IP and ICMP header, followed by a struct timeval and then an arbitrary number of “pad” bytes used to fill out the packet.

       ping works with both IPv4 and IPv6. Using only one of them explicitly can be enforced by specifying -4 or -6.

       ping can also send IPv6 Node Information Queries (RFC4620). Intermediate hops may not be allowed, because IPv6 source routing was deprecated (RFC5095).
```

```bash
# Example - ping
$ python pingmultiple.py
PING www.google.com (142.250.74.36) 56(84) bytes of data.
64 bytes from arn09s22-in-f4.1e100.net (142.250.74.36): icmp_seq=1 ttl=59 time=268 ms

--- www.google.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 267.969/267.969/267.969/0.000 ms
------------------------------------------------------------
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=59 time=1084 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1083.905/1083.905/1083.905/0.000 ms
------------------------------------------------------------
PING 4.4.4.4 (4.4.4.4) 56(84) bytes of data.

--- 4.4.4.4 ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms

------------------------------------------------------------
```

### TCP - Tramission Control Protocol

```bash
# Client 
$ python client_tcp.py 
############################################################
Setting the Client for the TCP...
Socket was created successfully!
Type the Host or IP address to be connected: www.google.com
Type the Port to be connected: 80
Client TCP was connected with sucess at the host - www.google.com and Port 80

```

### User Datagram Protocol - IPv4 or IPv6

```bash
Client-Server
```

![](gifs/Client_server_socket.gif)