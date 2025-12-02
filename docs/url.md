Understanding URLs
==================

**Author:** *Adam Motaouakkil*

# 1. Connecting to a Server

A url is made up of a scheme, hostname, and a path.
The scheme is something like http, https, file, and any other protocol you use to access information.
The host name is the string that identifies where the information is held.
The path is then the specific file or directory that you wish to navigate to.

After entering the URL, the OS puts the browser in touch with the server described by the hostname. The OS communicates with the Domain Name System (DNS) to convert the name to an IP.
Afterwards, the OS chooses which route to take to communicate with the server (Wi-Fi, wired...) using a routing table.
The signals are then sent through those media and picked up by series of routers that choose the best path for the signal to travel.
When the message reaches the server, a connection is then created.

In the example of `telnet example.org 80` it basically does what it does above: Opens up a socket at port 80 to the example.org ip.
It sends the request to connect and then receives the message.

# 2. Requesting Information

When sending information through https and http, you can use a multitude of message types:
GET, POST, and much more. When the sonnection is established, the browser requests information from the server in the form
of a `GET` method.
Here's an example:
    `GET /index.html HTTP/1.0
     Host: example.org`

GET is the method, /index.html is the path, then HTTP/1.0 is just the version, and the host: value is the header: value.

HTTP 1.0, 1.1, and others just implement different features.

# 3. The Server's Response

The server then responds in something like this:
    `HTTP/1.0 200 OK`
HTTP/1.0 is still the HTTP version, 200 or any digit is the response code, and the response description.
We have the error `404 Not Found` or `403 Forbidden` or `500 Server Error`.
In general the messages can be delineated in the following:

- 100s: Informational messages
- 200s: Success codes
- 300s: Request to follow-up (Redirect)
- 400s: Bad request
- 500s: Server handled the request badly

After sending the initial line, the server then responds with its own headers. After that, there is a blank line, followed
by html code, the body of the server's response (since the content type is text/html).

Overall: Browser sendings the `GET /index.html HTTP/1.0` -> Server responds with a `HTTP/1.0 <error code> <error description>`.

# 4. Sockets

Sockets are outlets by which a computer can communicate with another computer.
A socket has an *address family*, telling the computer which communication protocol to use.
It has a *type* describing the communication medium such as SOCK_STREAM or SOCK_DGRAM.
Then it has a *protocol* which is the communication protocol being used.

# 5. Encrypted Connections

HTTPS is more secure than HTTP as HTTPS stands for HTTP over TLS (Transport Layer Security). It is identical to the HTTP protocol
but all communications between the browser and the host are encrypted.
