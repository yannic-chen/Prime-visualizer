import sys
import itertools
from tkinter import *

# Maximum number
N = 300
# Window dimension
height = 900
width = 1600

# Fastest way to create a list of primes


def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))


master_primes = get_primes_erat(N)
primes = master_primes
# primes = get_primes_erat(N)[2:]    #removes the first two primes "2" and "3"


# use scrollwheel           #doesnt work
def _on_mousewheel(event):
    root.yview_scroll((event.delta/120), "units")


# setup Tkinter window
root = Tk()
#root.maxsize(width=width, height=height)
root.title("Prime visualizer")
root.geometry('1280x720')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# root.bind_all("<MouseWheel>", _on_mousewheel) #doesnt work

frame_main = Frame(root, bg="gray")
frame_main.grid(sticky='news')


# Create a frame for the canvas with non-zero row&column weights
frame_canvas = Frame(root)
frame_canvas.grid(row=0, column=0, pady=(5, 5), padx=(5, 5), sticky='news')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)


# Add a canvas in that frame
canvas = Canvas(frame_canvas)
canvas.grid(row=0, column=0, sticky="news", pady=(5, 5), padx=(5, 5))


# Link a scrollbar to the canvas (vertical)
vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)
# Link a scrollbar to the canvas (horizontal)
hsb = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
hsb.grid(row=1, column=0, sticky='ew')
canvas.configure(xscrollcommand=hsb.set)


# Create a frame to contain the squares
squares = Frame(canvas)
canvas.create_window((1, 0), window=squares, anchor='nw')

# Description of the widget
#desc = Label(root, text=f'Visualizing Prime numbers', borderwidth=1, relief="raised", bg="snow", font=('times', 15)).grid(row=1, columnspan=N)


def initiate_label():
    # axis label
    x_label = Label(squares, text=f'numbers', borderwidth=1,
                    bg="snow").grid(row=0, columnspan=N)

    y_label = Label(squares, text=f'prime', borderwidth=1,
                    bg="snow").grid(column=0, rowspan=len(primes))

    # create the top row of numbers
    for i in range(1, N+1):
        Label(squares, text="%i" % i, width=2, borderwidth=1,
              relief="raised").grid(row=1, column=i+1, sticky='nesw')

    # create left column of primes
    for j in range(len(primes)):
        Label(squares, text="%i" % primes[j], width=2, borderwidth=1,
              relief="raised").grid(row=2+j, column=1, sticky='nesw')


initiate_label()

# colour in the grids if column number is a prime and at the row where it is a prime to.


def normal():
    print(len(primes))
    for idx, val in enumerate(primes):
        for num in range(1, N+1):
            if num % val == 0:
                Label(squares, bg="black").grid(
                    row=2+idx, column=num + 1, sticky='nesw')


def grayscale():
    start = 200
    scale = start / len(primes)
    color_palette = []
    shade = start  # starting at 255 returns white, which is difficult to see
    while shade > 0:
        color_palette.append('#{:02x}{:02x}{:02x}'.format(
            round(shade), round(shade), round(shade)))  # formats the specified value to the given format. Here the format is x = hex format.
        shade = shade - scale
    for idx, val in enumerate(primes):
        for num in range(1, N+1):
            if num % val == 0:
                Label(squares, bg=color_palette[idx]).grid(
                    row=2+idx, column=num + 1, sticky='nesw')


def grayscale_down():
    start = 200
    scale = start / len(primes)
    color_palette = []
    shade = start  # starting at 255 returns white, which is difficult to see
    while shade > 0:
        color_palette.append('#{:02x}{:02x}{:02x}'.format(
            round(shade), round(shade), round(shade)))  # formats the specified value to the given format. Here the format is x = hex format.
        shade = shade - scale
    for idx, val in enumerate(primes):
        for num in range(1, N+1):
            if num % val == 0 and num != val:
                Label(squares, bg=color_palette[idx]).grid(
                    row=2, column=num + 1, rowspan=1+idx, sticky='nesw')


def update():
    primes = master_primes[:int(E1.get())]


def clear():
    for widget in squares.winfo_children():
        widget.destroy()
    initiate_label()


# some extra options buttons, to change display
B0 = Button(canvas, text="Black Prime",
            command=normal).grid(row=0, column=0, sticky='nw')

B1 = Button(canvas, text="Grayscale Prime",
            command=grayscale).grid(row=0, column=1, sticky='nw')

B2 = Button(canvas, text="Column",
            command=grayscale_down).grid(row=0, column=2, sticky='nw')

L1 = Label(canvas, text="How many prime numbers").grid(
    row=0, column=3, sticky='nw')
E1 = Entry(canvas)
# has to be on two lines, otherwise cannot use get(), as .grid is prioritized over Entry for the variable E1.
E1.grid(row=0, column=6)
B3 = Button(canvas, text="Update", command=update).grid(
    row=0, column=7, sticky='nw')

B4 = Button(canvas, text="Clear all",
            command=clear).grid(row=0, column=8, sticky='nw')

# Update squares idle tasks to let tkinter calculate squares sizes
squares.update_idletasks()

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
