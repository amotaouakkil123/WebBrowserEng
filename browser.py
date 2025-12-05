import socket
import ssl
import tkinter
import tkinter.font
from layout import Text
from layout import Tag
from layout import Layout


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
        self.canvas.pack()
        
        self.display_list = []

        self.scroll = 0
        self.window.bind("<Down>", self.scrollDown)
        self.window.bind("<Up>", self.scrollUp)
        self.window.bind("<Button-4>", self.scrollUpMouse)
        self.window.bind("<Button-5>", self.scrollDownMouse)

    def load(self, url):
        body = url.request()
        tokens = lex(body)
        self.display_list = Layout(tokens).display_list
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x, y, c, f in self.display_list:
            if y > self.scroll + self.height: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x, y - self.scroll, text=c, anchor='nw', font=f)

    SCROLL_STEP = 100

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

def lex(body):
    out = []
    buffer = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
            if buffer: out.append(Text(buffer))
            buffer = ""
        elif c == ">":
            in_tag = False
            out.append(Tag(buffer))
            buffer = ""
        else:
            buffer += c

    if not in_tag and buffer:
        out.append(Text(buffer))

    return out


