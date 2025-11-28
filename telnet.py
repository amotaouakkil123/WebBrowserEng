import socket
import ssl

class URL:
    def __init__(self, url):
        if url == "":
            url = "file:///home/adam-motaouakkil/Repos/WebBrowserEng/"

        print("The initial url is " + url)

        self.scheme, url = url.split("://", 1)
        print("The split url is " + url)
        assert self.scheme in ["http", "https", "file"]

        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443
        elif self.scheme == "file":
            self.port = 8000

        if "/" != url[-1]:
            url = url + "/"

        if self.scheme != "file":
            self.host, url = url.split("/", 1)
            self.path = "/" + url

            if ":" in self.host:
                self.host, port = self.host.split(":", 1)
                self.port = int(port)
        else:
            self.host = "localhost"
            self.path = url

    def request(self):
        family = ""
        if self.scheme == "file":
            print("We are doing it the unix way")
            family = socket.AF_UNIX
        else:
            family = socket.AF_INET
        s = socket.socket(
            family,
            type=socket.SOCK_STREAM
            #proto=socket.IPPROTO_TCP,
        )
        print("The port is " + str(self.port))
        print("The url host is " + self.host)
        #s.connect((self.host, self.port))
        print(self.path)
        s.connect(self.path)
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        request = "GET {} HTTP/1.1\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "Connection: {}\r\n".format("close")
        request += "User-Agent: {}\r\n".format("chrome")
        request += "\r\n"
        s.send(request.encode("utf8"))
        response = s.makefile("r", encoding="utf8", newline="\r\n")
        statusline = response.readline()
        version, status, explanation = statusline.split(" ", 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line == "\r\n": break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip()
        
        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers

        content = response.read()
        s.close()
        return content

def show(body):
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            print(c, end="")
    
def load(url):
    body = url.request()
    show(body)

if __name__ == "__main__":
    import sys
    print(len(sys.argv))
    if len(sys.argv) < 2:
        url = ""
    else:
        url = sys.argv[1]
    print("This is the url " + url)
    load(URL(url))
