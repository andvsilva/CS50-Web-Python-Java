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

```bash
# generator_hashes
$ python generator_hashes.py                                              4ms 
Type the string to generate the hash: andvsilva
#### MENU Choose one type of hash ### 
             1) MD5 
             2) SHA1
             3) SHA256
             4) SHA512
             Type the number of the hash to be generated: 1
(base) 
~/repo/CS50-Web-Python-Java/information_security_py/hash on  master! ⌚ 23:02:20
$ python generator_hashes.py                                                                                                                        9995ms 
Type the string to generate the hash: andvsilva
#### MENU Choose one type of hash ### 
             1) MD5 
             2) SHA1
             3) SHA256
             4) SHA512
             Type the number of the hash to be generated: 2
The hash SHA1 of the string is:  0d7044371abc9619a144606546c6c51c2df7dd72
(base) 
~/repo/CS50-Web-Python-Java/information_security_py/hash on  master! ⌚ 23:02:33
$ python generator_hashes.py                                                                                                                        6064ms 
Type the string to generate the hash: andvsilva
#### MENU Choose one type of hash ### 
             1) MD5 
             2) SHA1
             3) SHA256
             4) SHA512
             Type the number of the hash to be generated: 3
The hash SHA256 of the string is:  b87ba9d57d6ea058ad020967abfd28500c57edf907ef46fb39ed4d993555eea6
(base) 
~/repo/CS50-Web-Python-Java/information_security_py/hash on  master! ⌚ 23:02:43
$ python generator_hashes.py                                                                                                                        8277ms 
Type the string to generate the hash: andvsilva
#### MENU Choose one type of hash ### 
             1) MD5 
             2) SHA1
             3) SHA256
             4) SHA512
             Type the number of the hash to be generated: 4
The hash SHA512 of the string is:  666d26380225383c108d895b6bf435a86e0da3ff46e8bccc903b3da0304ebf7efb57656d75e294e516f7755a87fddd4235de2d4fa98ffcc5071f4125a4faf461

```

### Wordlists

```bash
# Generator of wordlists

$ python generator_wordlists.py
String to be permutated: abc
# 1 -> abc
# 2 -> acb
# 3 -> bac
# 4 -> bca
# 5 -> cab
# 6 -> cba
```

### Web Crawler

WebCrawler is a search engine, and is the oldest surviving search engine on the web today. For many years, it operated as a metasearch engine. WebCrawler was the first web search engine to provide full text search.

```bash
### In this script, I am using the library snoop for debug (very good!!)
$ python webscrawler.py
21:18:39.75 >>> Call to start in File "webscrawler.py", line 16
21:18:39.75 ...... url = 'https://scikit-learn.org/stable/'
21:18:39.75   16 | def start(url):
21:18:39.75   18 |     wordlist = [] # to store the content of the site
21:18:39.75 .......... wordlist = []
21:18:39.75   19 |     source_code = requests.get(url).text # get text from site
21:18:44.89 .......... source_code = '\n\n<!DOCTYPE html>\n<!--[if IE 8]><html class="no-....org/versionwarning.js"></script>\n</body>\n</html>'
21:18:44.89 .......... len(source_code) = 26011
21:18:44.89   21 |     soup = BeautifulSoup(source_code, 'html.parser')
21:18:44.95 .......... soup = 
21:18:44.95                   <!DOCTYPE html>
21:18:44.95                   
21:18:44.95                   <!--[if IE 8]><html class="no-....org/versionwarning.js"></script>
21:18:44.95                   </body>
21:18:44.95                   </html>
21:18:44.95 .......... soup.shape = None
21:18:44.95 .......... soup.dtype = None
21:18:44.95   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:44.97 .......... each_text = <h4 class="sk-card-title card-title">Classification</h4>
21:18:44.97 .......... each_text.shape = None
21:18:44.97 .......... each_text.dtype = None
21:18:44.97   26 |         content = each_text.text
21:18:44.97 .............. content = 'Classification'
21:18:44.97   28 |         words = content.lower().split()
21:18:44.98 .............. words = ['classification']
21:18:44.98 .............. len(words) = 1
21:18:44.98   31 |         for each_word in words:
21:18:44.99 .............. each_word = 'classification'
21:18:44.99   32 |             wordlist.append(each_word)
21:18:45.00 .................. wordlist = ['classification']
21:18:45.00 .................. len(wordlist) = 1
21:18:45.00   31 |         for each_word in words:
21:18:45.01   33 |         clean_wordlist(wordlist)
classification : 1 
[('classification', 1)]
21:18:45.02   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.03 .......... each_text = <h4 class="sk-card-title card-title">Regression</h4>
21:18:45.03   26 |         content = each_text.text
21:18:45.04 .............. content = 'Regression'
21:18:45.04   28 |         words = content.lower().split()
21:18:45.05 .............. words = ['regression']
21:18:45.05   31 |         for each_word in words:
21:18:45.06 .............. each_word = 'regression'
21:18:45.06   32 |             wordlist.append(each_word)
21:18:45.07 .................. wordlist = ['classification', 'regression']
21:18:45.07 .................. len(wordlist) = 2
21:18:45.07   31 |         for each_word in words:
21:18:45.08   33 |         clean_wordlist(wordlist)
classification : 1 
regression : 1 
[('classification', 1), ('regression', 1)]
21:18:45.09   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.10 .......... each_text = <h4 class="sk-card-title card-title">Clustering</h4>
21:18:45.10   26 |         content = each_text.text
21:18:45.11 .............. content = 'Clustering'
21:18:45.11   28 |         words = content.lower().split()
21:18:45.12 .............. words = ['clustering']
21:18:45.12   31 |         for each_word in words:
21:18:45.13 .............. each_word = 'clustering'
21:18:45.13   32 |             wordlist.append(each_word)
21:18:45.14 .................. wordlist = ['classification', 'regression', 'clustering']
21:18:45.14 .................. len(wordlist) = 3
21:18:45.14   31 |         for each_word in words:
21:18:45.15   33 |         clean_wordlist(wordlist)
classification : 1 
regression : 1 
clustering : 1 
[('classification', 1), ('regression', 1), ('clustering', 1)]
21:18:45.16   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.17 .......... each_text = <h4 class="sk-card-title card-title">Dimensionality reduction</h4>
21:18:45.17   26 |         content = each_text.text
21:18:45.18 .............. content = 'Dimensionality reduction'
21:18:45.18   28 |         words = content.lower().split()
21:18:45.19 .............. words = ['dimensionality', 'reduction']
21:18:45.19 .............. len(words) = 2
21:18:45.19   31 |         for each_word in words:
21:18:45.20 .............. each_word = 'dimensionality'
21:18:45.20   32 |             wordlist.append(each_word)
21:18:45.22 .................. wordlist = ['classification', 'regression', 'clustering', 'dimensionality']
21:18:45.22 .................. len(wordlist) = 4
21:18:45.22   31 |         for each_word in words:
21:18:45.23 .............. each_word = 'reduction'
21:18:45.23   32 |             wordlist.append(each_word)
21:18:45.24 .................. wordlist = ['classification', 'regression', 'clustering', 'dimensionality', 'reduction']
21:18:45.24 .................. len(wordlist) = 5
21:18:45.24   31 |         for each_word in words:
21:18:45.24   33 |         clean_wordlist(wordlist)
classification : 1 
regression : 1 
clustering : 1 
dimensionality : 1 
reduction : 1 
[('classification', 1), ('regression', 1), ('clustering', 1), ('dimensionality', 1), ('reduction', 1)]
21:18:45.26   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.26 .......... each_text = <h4 class="sk-card-title card-title">Model selection</h4>
21:18:45.26   26 |         content = each_text.text
21:18:45.28 .............. content = 'Model selection'
21:18:45.28   28 |         words = content.lower().split()
21:18:45.28 .............. words = ['model', 'selection']
21:18:45.28   31 |         for each_word in words:
21:18:45.29 .............. each_word = 'model'
21:18:45.29   32 |             wordlist.append(each_word)
21:18:45.30 .................. wordlist = ['classification', 'regression', 'clustering', 'dimensionality', 'reduction', 'model']
21:18:45.30 .................. len(wordlist) = 6
21:18:45.30   31 |         for each_word in words:
21:18:45.31 .............. each_word = 'selection'
21:18:45.31   32 |             wordlist.append(each_word)
21:18:45.32 .................. wordlist = ['classification', 'regression', 'clustering', 'dimensionality', 'reduction', 'model', 'selection']
21:18:45.32 .................. len(wordlist) = 7
21:18:45.32   31 |         for each_word in words:
21:18:45.33   33 |         clean_wordlist(wordlist)
classification : 1 
regression : 1 
clustering : 1 
dimensionality : 1 
reduction : 1 
model : 1 
selection : 1 
[('classification', 1), ('regression', 1), ('clustering', 1), ('dimensionality', 1), ('reduction', 1), ('model', 1), ('selection', 1)]
21:18:45.34   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.35 .......... each_text = <h4 class="sk-card-title card-title">Preprocessing</h4>
21:18:45.35   26 |         content = each_text.text
21:18:45.36 .............. content = 'Preprocessing'
21:18:45.36   28 |         words = content.lower().split()
21:18:45.37 .............. words = ['preprocessing']
21:18:45.37 .............. len(words) = 1
21:18:45.37   31 |         for each_word in words:
21:18:45.38 .............. each_word = 'preprocessing'
21:18:45.38   32 |             wordlist.append(each_word)
21:18:45.39 .................. wordlist = ['classification', 'regression', 'clustering', 'dimensionality', ..., 'model', 'selection', 'preprocessing']
21:18:45.39 .................. len(wordlist) = 8
21:18:45.39   31 |         for each_word in words:
21:18:45.40   33 |         clean_wordlist(wordlist)
classification : 1 
regression : 1 
clustering : 1 
dimensionality : 1 
reduction : 1 
model : 1 
selection : 1 
preprocessing : 1 
[('classification', 1), ('regression', 1), ('clustering', 1), ('dimensionality', 1), ('reduction', 1), ('model', 1), ('selection', 1), ('preprocessing', 1)]
21:18:45.41   25 |     for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
21:18:45.42 <<< Return value from start: None
(base) 
```