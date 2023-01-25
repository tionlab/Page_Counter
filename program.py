from types import ClassMethodDescriptorType
from ursina import *

app = Ursina()

window.borderless = False
window.color = color._20

Text.default_font = 'BMHANNA_11yrs_ttf.ttf'

book = 0
book_text = Text(text=str(book), x=-0.02, y=0.4, scale=2, background=True)
button = Button(text='2 장', color=color.orange, x=0, scale=0.5)
down = Button(text='- 1 장', color=color.orange, x=-0.5, scale=0.2)
clear = Button(text='초기화', color=color.orange, x=0.5, scale=0.2)

def button_click():
    global book
    book += 2

def down_click():
    global book
    book -= 1

def clear_click():
    global book
    book = 0

down.on_click = down_click
button.on_click = button_click
clear.on_click = clear_click

def update():
    global book

    book_text.text = str(book)

app.run()