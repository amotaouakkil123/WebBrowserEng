import socket
import ssl
import tkinter

class URL:
    def __init__(self, url):
        try:

            self.scheme, url = url.split("://", 1)
            assert self.scheme in ["http", "https", "file"]

            if self.scheme == "http":
                self.port = 80
            elif self.scheme == "https":
                self.port = 443

            if "/" not in url:
                url = url + "/"
            self.host, url = url.split("/", 1)
            self.path = "/" + url

            if ":" in self.host:
                self.host, port = self.host.split(":", 1)
                self.port = int(port)
        except:
            print("Malformed URL found, falling back to the WBE home page.")
            print(" URL was: " + url)
            self.__init__("https://browser.engineering")

    def request(self):
        s = socket.socket(
            socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )
        s.connect((self.host, self.port))
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        request = "GET {} HTTP/1.1\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
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

VSTEP, HSTEP = 13, 18
WIDTH, HEIGHT = 800, 600

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=800,
            height=600
        )
        self.width = 800
        self.height = 600
        self.canvas.pack(expand=True)
        self.window.bind("<Configure>", self.onResize)
        
        self.scroll = 0
        self.window.bind("<Down>", self.scrollDown)
        self.window.bind("<Up>", self.scrollUp)
        self.window.bind("<Button-4>", self.scrollUpMouse)
        self.window.bind("<Button-5>", self.scrollDownMouse)

    def load(self, url):
        body = url.request()
        text = lex(body)
        self.display_list = layout(text)
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y, c in self.display_list:
            if y > self.scroll + self.height: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c)

    SCROLL_STEP = 100

    def onResize(self, e):
        wScale = float(e.width) / self.width
        hScale = float(e.height) / self.height
        self.width = e.width
        self.height = e.height
        self.window.config(width=self.width, height=self.height)
        self.canvas.scale("all", 0, 0, wScale, hScale)

    def scrollDown(self, e):
        self.scroll += Browser.SCROLL_STEP
        self.draw()

    def scrollUp(self, e):
        self.scroll -= Browser.SCROLL_STEP
        self.draw()

    def scrollDownMouse(self, e):
        self.scroll += e.y
        self.draw()

    def scrollUpMouse(self, e):
        self.scroll -= e.y
        self.draw()

def layout(text):
    display_list = []
    cursor_x, cursor_y = HSTEP, VSTEP
    for c in text:
        display_list.append((cursor_x, cursor_y, c))
        cursor_x += HSTEP
            
        if cursor_x >= WIDTH - HSTEP:
            cursor_y += VSTEP
            cursor_x = HSTEP

        if c == '\n':
            cursor_y += VSTEP
            cursor_x = HSTEP

    return display_list

def lex(body):
    tex = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            tex += c
    return tex

if __name__ == "__main__":
    import sys
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()
