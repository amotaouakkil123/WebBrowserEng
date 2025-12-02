Communication and Encryption Protocols for the Internet
======================

# Hypertex Transfer Protocol

HTTP is a communication protocol that is lightweight and meant for distributed systems.
"It is generic, stateless, oject-oriented, and can be used for many tasks, as name servers and distributed
object management systems." By allowing typing of content, platforms can develop features independently.
It was designed for distributive, collaborative, hypermedia information systems.
In a system designed for retrieval, search, front-end updates, and annotation, HTTP was meant to be broad
and simple to implement, building on URI (Uniform Resource Identifier), location (URL), and name (URN).

HTTP is also a generic protocol to communicate between agents, proxies and gateways to other protocols like
SMTP, NNTP, FTP, Gopher, and WAIS, allowing for basic hypermedia access to resources.

# Terms

Connection: Virtual circuit established between two application programs.

Message: Basic unit of HTTP communcation, sequences of octets and transmitted through connection.

Request: The system asking for information from the receiving computer.

Response: The receiving computer sending back the information from the request.

Resource: A network object or service identified by a URI.

Entity: The representation of the data resource, may be enclosed in a request or response.
It contains metainformation in etity headers and content in the form of an entity body.

Client: The application that establishes connections for sending requests.

User Agent: Client that initiates a request (browsers, editors, and spiders).

Server: Application that accepts connections to service requests.

Origin Server: The server where the resource resides or to be created.

Proxy: An intermediary program that acts as both a server and a client for the purpose of making requests
on behalf of other clients. Requests may be reinterpreted, translated to other servers. It then forwards the request.

Gateway: A server that acts as an intermediary for some other server. It acts like an origin server when it is not,
and a client may think that they are communicating with an origin server, but it's just a gateway. They usually act
as a security buffer for origin servers, protocol translators to access resources stored on non-HTTP systems.

Tunnel: Blind relay between two connections, not party to HTTP communication. Tunnels are used when a portal is necessary
and the intermediary cannot interpret the relayed communication.

Cache: Local store of response messages and the subsystem that controls its message storage, retrieval, and deletion.
It stores cacheable responses to reduce response times.

Any program can be a client or a server. A server can be an origin server, proxy, gateway, or tunnel.

# HTTP Operation

HTTP protocols are based on a request and response paradigm. A client establishes a connection with a server and sends
a request to the server in the form of a request method, URI, and protocol version. You also send a message requesting modifiers.
Most HTTP communication is in the form of a browser user agent consisting of a request to be applied to a resource in some
origin server.

A more complicated situation occurs when one or more intermediaries are present: Proxy, gateway, and tunnel. A proxy will intercept the message, reformat it, and send it over to the URI once again. A gateway will receive that request to reformat it in a
format appropriate to the origin server. Tunnels are used when communication needs to pass through an intermediary like a firewall.
Some parts of the HTTP chain are not involved in every part of the chain, some are. Server are also processing requests from 
many other users and systems.

HTTP is generally taking place over TCP/IP. The default port is 80. HTTP is also implemented over other transport protocols,
but they need a reliable layer which TCP/IP usually is.

Current practices dictate that the connection be established by the client prior to each request and closed by the server after
sending the response. Either party can close the connection prematurely and handle these actions in a predictable manner.

# 2. Notational Conventions and Generic Grammar

If you want to understand the language specifications of HTTP this is the section from the standard that must be read.

# 3. Protocol Parameters

HTTP versions use HTTP/<major>.<minor>

HTTP/1.0 Servers must:

- Recognize the format of the Request-Line for HTTP/0.9 and HTTP/1.0 requests.
- Understand any valid request in the format of HTTP/0.9 or HTTP/1.0.
- Respond appropriately with a message in the same protocol version used by the client.

HTTP/1.0 Clients must:

- Recognize the format of the Status-Line for HTTP/1.0 responses.
- Understand any valid response in the format of HTTP/0.9 or HTTP/1.0.

Proxies and gateway applications must be careful to never send a message with a version indicator
which is greater than the application's native header.

Uniform Resource Identifiers:

URIs have many names such as www addresses, Universal Document Identifiers, Universal Resource Identifiers, and finally
the combination of Uniform Resource Locators (URL) and Names (URN). 

The general syntax of URIs are then represented in absolute or relative forms.

The typical http URL is as follows: `"http:" "//" host [ ":" port ] [ abs_path ]`
Host: A legal Internet host domain name.
Port: Digit of the port.

Date/Time Formats are like `Sun, 06 Nov 1994 08:49:37 GMT`

Content codings are used to indicate encoding transformation applied to a resource. This allows for a document to be compressed
 or encrypted without losing the identity of its underlying media type.

Media Type: Text, video, and so on.

Product Tokens are used to allow communicating applications to identify themselves, like User-Agent and Server
`User-Agent: CERN-LineMode/2.15 libwww/2.17b3` or `Server: Apache/0.8.4`

# 4. HTTP Message

HTTP messages consist of `Simple-Request`, `Simple-Response`, `Full-Request`, and `Full-Response`.

A full request will look like the following:

`Request-Line
 *( General-Header
  | Request-Header
  | Entity-Header )
CRLF
[ Entity-Body ]`

A full response will then look like the following:

`Status-Line
 *( General-Header
  | Response-Header
  | Entity-Header )
CRLF
[ Entity-Body ]`

Simple-Request and Simple-Response don't allow for any header information and merely include the request and the response
the body of the response.

`"GET" SP Request-URI CRLF`
`[ Entity-Body ]`

# 5. Request

A request line looks like the following: `Method SP Request-URI SP HTTP-Version CRLF`
The different methods implemented are GET, HEAD, POST, and an arbitrary extension-method. If a server does not implement the
method it should return code 501.
Then we have the Request-Header which is comprised of Authorization, From, If-Modified-Since, Referer, or User-Agent.

# 6. Response

Yet again, simple-response and full-response, following the same format as the response.

The status line is defined as follows: `HTTP-Version SP Status-Code SP Reason-Phrase CRLF`

The codes are defined as follows:

- 1xx: Informational.
- 2xx: Success - The action was received and undestood, and accepted.
- 3xx: Redirection - Further action must be taken.
- 4xx: Client Error - Request contains bad syntax or can't be fulfilled.
- 5xx: Server Error - Server failed to fulfill a valid request.

""
