import sys
import itertools
from itertools import cycle
from tkinter import *
import math

# ------------------------------------------------------Settings-------------------------------------
# Maximum number
N = 100
magnitude = 9999
# Window dimension
height = 900
width = 1600
# fontsize
fontsize = 8

# ------------------------------------------------------Functions-------------------------------------


def prime_table_window():
    # Window2-------- Generate Table of Primes -------------
    def prime_table(ending="0", magnitude=magnitude):
        # reset the widget and stored information
        '''
        Need to find a way to exclude the labels and table being deleted, otherwise need to reapply and rebuild the stats labels.
        '''
        for widget in second_frame2.winfo_children():
            widget.destroy()
        for widget in stats_frame2.winfo_children():
            widget.destroy()
        dictionary_number_digit = (
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        )
        # reapply the stats labels
        L22 = Label(stats_frame2, text="Stats", bg="white", borderwidth=1,
                    relief="raised").pack(side=TOP, fill=X, anchor=CENTER)
        L221 = Label(stats_frame2, text=f"Proportion of Primes to {magnitude}: {1/math.log(magnitude):.3}", bg="white", borderwidth=1,
                     relief="raised").pack(side=TOP, fill=X, anchor=CENTER)

        # rebuild the frequency tab and table
        freq_tab = Frame(stats_frame2, bg="yellow")
        freq_tab.grid_rowconfigure(0, weight=1)
        freq_tab.grid_columnconfigure(0, weight=1)
        freq_tab.pack(side=BOTTOM, fill=X, anchor=SW)
        L230 = Label(freq_tab, text=f"Number \ Digit ").grid(
            row=0, column=0, sticky='news')
        for i in range(1, 8):
            Label(freq_tab, text=(i)).grid(row=0, column=9-i, sticky='nesw')
        for i in range(10):
            Label(freq_tab, text=f"{i}").grid(
                row=i + 1, column=0, sticky='news')

        # the magnitude determines upper limit to which prime numbers should be considered
        primes_for_table = limiting(magnitude)
        # creates the table header
        for i in range(len(str(magnitude))):
            zeros = i*"0"
            Label(second_frame2, text=(
                f"10{zeros}"), width=2, borderwidth=1, relief="raised").grid(row=0, column=i, sticky='nesw')

        # if no suffix is written, fill in all prime numbers
        if ending == 0:
            # initial start

            col = 0
            count = 0
            prev_prime_len = 1
            for i in primes_for_table:
                # count the frequency of digits
                # needs to reverse, otherwise, the first digit is actually the leftmost digit
                for idx, val in enumerate(str(i)[::-1]):
                    dictionary_number_digit[idx][int(val)] += 1
                # reset row and go to next column
                if prev_prime_len < len(str(i)):
                    count = 0
                    col += 1
                # fill in number and prepare for next iteration
                Label(second_frame2, text=(i)).grid(
                    row=count + 1, column=col, sticky='nesw')
                count += 1
                prev_prime_len = len(str(i))

        # fill in only the prime numbers with suffix
        else:
            # initial start
            col = 0
            count = 0
            # filter list of primes for only the ones with ending
            suff = [j for j in primes_for_table if str(j).endswith(ending)]
            prev_prime_len = len(str(suff[0]))
            for i in suff:
                # count the frequency of digits
                # needs to reverse, otherwise, the first digit is actually the leftmost digit
                for idx, val in enumerate(str(i)[::-1]):
                    dictionary_number_digit[idx][int(val)] += 1
                a = len(str(i))
                # reset row and go to next column
                if prev_prime_len < a:
                    count = 0
                    col += 1
                # fill in number and prepare for next iteration
                Label(second_frame2, text=(i)).grid(
                    row=count + 1, column=a - 1, sticky='nesw')
                count += 1
                prev_prime_len = len(str(i))

        # fill in the stats of the prime numbers of interest
        L23 = Label(stats_frame2, text=f"Number of Primes in 10: {sum([1 for i in suff if len(str(i)) == 1])}", bg="white",
                    borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
        L24 = Label(stats_frame2, text=f"Number of Primes in 100: {sum([1 for i in suff if len(str(i)) == 2])}", bg="white",
                    borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
        L25 = Label(stats_frame2, text=f"Number of Primes in 1000: {sum([1 for i in suff if len(str(i)) == 3])}", bg="white",
                    borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
        L26 = Label(stats_frame2, text=f"Number of Primes in 10000: {sum([1 for i in suff if len(str(i)) == 4])}", bg="white",
                    borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
        L27 = Label(stats_frame2, text=f"Number of Primes in 100000: {sum([1 for i in suff if len(str(i)) == 5])}", bg="white",
                    borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
        for idx, val in enumerate(dictionary_number_digit):
            for j in val.items():
                if j[1] != 0:
                    Label(freq_tab, text=(j[1])).grid(
                        row=j[0] + 1, column=8 - idx, sticky='nesw')
                else:
                    Label(freq_tab, bg="white").grid(
                        row=j[0] + 1, column=8 - idx, sticky='nesw')

    # Window2-------- Generate and Structure of window -------------
    window2 = Toplevel(root)
    window2.title(f"Prime number to {magnitude}")
    # Dont know why I need to specify .pack and .grid seperately. Since otherwise it places in the first window
    option_frame2 = Frame(window2, bg="SystemButtonFace")
    option_frame2.pack(side=TOP, fill=X)
    L21 = Label(option_frame2,
                text="Prime number suffix (leave blank to get all):", bg="SystemButtonFace").pack(side=LEFT, anchor=NW)
    E21 = Entry(option_frame2)
    E21.pack(side=LEFT, anchor=NW,)
    B21 = Button(option_frame2, text="Generate",
                 command=lambda: prime_table(ending=E21.get())).pack(side=LEFT, anchor=NW,)
    main_frame2 = Frame(window2, bg="white")
    main_frame2.pack(side=TOP, fill=BOTH, expand=1)
    main_frame2.grid_rowconfigure(1, weight=1)
    main_frame2.grid_columnconfigure(1, weight=1)

    main_canvas2 = Canvas(main_frame2, bg="light blue")
    main_canvas2.grid(row=1, column=1, sticky='news')
    second_frame2 = Frame(main_canvas2, bg="bisque")
    main_canvas2.create_window((0, 0), window=second_frame2, anchor="nw")

    stats_frame2 = Frame(main_frame2, bg="blue",
                         borderwidth=1, relief="raised")
    stats_frame2.grid(row=1, column=3, sticky='nes')
    L22 = Label(stats_frame2, text="Stats", bg="white", borderwidth=1,
                relief="raised").pack(side=TOP, fill=X, anchor=CENTER)
    # Prime number theorem states that the number of primes up to N is ~ N/ln(N)
    # ln(N) is the average distance between primes
    # therefore, the Nth prime is ~ N*ln(N)
    # the ":.3" prints out in 3 signficiant figure
    L221 = Label(stats_frame2, text=f"Proportion of Primes to {magnitude}:  {1/math.log(magnitude):.3}", bg="white", borderwidth=1,
                 relief="raised").pack(side=TOP, fill=X, anchor=CENTER)
    '''
    L23 = Label(stats_frame2, text="Number of Primes in 10:", bg="white",
                borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
    L24 = Label(stats_frame2, text="Number of Primes in 100:", bg="white",
                borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
    L25 = Label(stats_frame2, text="Number of Primes in 1000:", bg="white",
                borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
    L26 = Label(stats_frame2, text="Number of Primes in 10000:", bg="white",
                borderwidth=1, relief="raised").pack(side=TOP, fill=X, anchor=NW)
    '''

    # initial Frequency of digits table
    freq_tab = Frame(stats_frame2, bg="yellow")
    freq_tab.grid_rowconfigure(0, weight=1)
    freq_tab.grid_columnconfigure(0, weight=1)
    freq_tab.pack(side=BOTTOM, fill=X, anchor=SW)
    L230 = Label(freq_tab, text=f"Digit: ").grid(
        row=0, column=0, sticky='news')
    for i in range(1, 8):
        Label(freq_tab, text=(i)).grid(row=0, column=9-i, sticky='nesw')
    for i in range(10):
        Label(freq_tab, text=f"{i}").grid(row=i + 1, column=0, sticky='news')

    # Add scrollbars
    vscroll2 = Scrollbar(main_frame2, orient=VERTICAL,
                         command=main_canvas2.yview)
    vscroll2.grid(row=1, column=2, sticky='ns', pady=(10, 0))
    hscroll2 = Scrollbar(main_frame2, orient=HORIZONTAL,
                         command=main_canvas2.xview)
    hscroll2.grid(row=2, column=1, sticky='ew', padx=(10, 0))

    # Configure the canvas
    main_canvas2.configure(yscrollcommand=vscroll2.set,
                           xscrollcommand=hscroll2.set)
    main_canvas2.bind('<Configure>', lambda e: main_canvas2.configure(
        scrollregion=main_canvas2.bbox("all")))


def initiate_label():
    if N <= 500:
        # create the top row of numbers
        for i in range(1, N+1):
            Label(second_frame, text="%i" % i, font=("", (fontsize if N <= 300 else fontsize//2)), width=2, borderwidth=1,
                  relief="raised").grid(row=0, column=i, sticky='nesw')

        # create left column of primes
        for j in range(len(primes)):
            Label(second_frame, text="%i" % primes[j], font=("", (fontsize if N <= 300 else fontsize//2)), width=2, borderwidth=1,
                  relief="raised").grid(row=1+j, column=0, sticky='nesw')

# when inputting number of prime numbers


def update():
    prime_var.set(E1.get())
    clear()

# clears the screen


def clear():
    for widget in second_frame.winfo_children():
        widget.destroy()
    initiate_label()


# Grid coloring function
def fill_prime(color="black", column=0):
    if color == "grayscale":
        # starting at 255 returns white, which is difficult to see depending on background
        start = 255
        scale = start / len(primes)
        color_palette = []
        shade = start
        while shade > 0:
            color_palette.append('#{:02x}{:02x}{:02x}'.format(
                round(shade), round(shade), round(shade)))  # formats the specified value to the given format. Here the format is x = hex format.
            shade = shade - scale
        if column != 0:
            for idx, val in enumerate(primes[:prime_var.get()]):
                for num in range(1, N+1):
                    if num % val == 0 and num != val:
                        # font size is effectively there to make the cells as small as possible,
                        Label(second_frame, bg=color_palette[idx], font=("Courier", 1)).grid(
                            row=1, column=num, rowspan=1+idx, sticky='nesw')
        else:
            for idx, val in enumerate(primes[:prime_var.get()]):
                for num in range(1, N+1):
                    if num % val == 0:
                        Label(second_frame, bg=color_palette[idx], font=("Courier", 1)).grid(
                            row=1+idx, column=num, sticky='nesw')
    if color == "black":
        for idx, val in enumerate(primes[:prime_var.get()]):
            for num in range(1, N+1):
                if num % val == 0:
                    Label(second_frame, bg="black", font=("Courier", 2)).grid(
                        row=1+idx, column=num, sticky='nesw')

# prime spiral


def move_right(x, y): return x+1, y
def move_down(x, y): return x, y-1
def move_left(x, y): return x-1, y
def move_up(x, y): return x, y+1


moves = [move_right, move_down, move_left, move_up]


def spiral(number=N):
    for widget in second_frame.winfo_children():
        widget.destroy()
    spiral_primes = limiting(number**2)
    _moves = cycle(moves)
    n = 1
    pos = math.ceil(number), math.ceil(number)
    times_to_move = 1

    Label(second_frame, text=(f"{n}" if number < 200 else ""), bg="red", font=("Courier", max(1, int(12/math.log10(number/math.log10(number/5)))))).grid(
        row=pos[0], column=pos[1], sticky='nesw')

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= number**2:
                    return
                pos = move(*pos)
                n += 1
                if n in spiral_primes:
                    Label(second_frame, text=(f"{n}" if number < 200 else ""), bg="black", font=("Courier", max(1, int(12/math.log10(number/math.log10(number/5))))), fg='white').grid(
                        row=pos[0], column=pos[1], sticky='nesw')
                    spiral_primes.pop(0)

        times_to_move += 1


# Fastest way to create a list of primes
'''
#obsolete, since I generated a list of primes to 10.000.000

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
'''


def limiting(N):
    if N >= data[-1]:
        return data
    master_primes = []
    temp = 0
    while N > data[temp]:
        master_primes.append(data[temp])
        temp += 1
    return master_primes


# ------------------------------------------------------Tkinter setup-------------------------------------
root = Tk()
root.maxsize(width=1920, height=1080)
root.title(f"Prime visualizer to {N}")

# creating a main frame
main_frame = Frame(root, bg="white")

# Create options Frame
options_frame = Frame(root, bg="gray")
options_frame.pack(side=TOP, fill=X)

#Buttons and Forms
B0 = Button(options_frame, text="Black Prime",
            command=fill_prime).pack(side=LEFT)
B1 = Button(options_frame, text="Gray", command=lambda: fill_prime(
    color="grayscale")).pack(side=LEFT)
B2 = Button(options_frame, text="Column",
            command=lambda: fill_prime(color="grayscale", column=1)).pack(side=LEFT)
L1 = Label(options_frame, text="Prime numbers up to:").pack(side=LEFT)
# has to be on two lines, otherwise cannot use get(), as .grid is prioritized over Entry for the variable E1.
E1 = Entry(options_frame)
E1.pack(side=LEFT)
B3 = Button(options_frame, text="Update", command=update).pack(side=LEFT)
B4 = Button(options_frame, text="RESET", command=clear).pack(side=LEFT)
B4 = Button(options_frame, text="Generate Spiral",
            command=lambda: spiral(number=int(E2.get()))).pack(side=RIGHT)
E2 = Entry(options_frame)
E2.insert(END, int(N/10))
E2.pack(side=RIGHT)
L2 = Label(options_frame, text="Spiral Size (max 3162):").pack(side=RIGHT)
B5 = Button(root, text="Prime numbers",
            command=prime_table_window).pack(side=BOTTOM)


# Create main Frame
main_frame.pack(side=TOP, fill=BOTH, expand=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# axis label
Label(main_frame, text=f'numbers', borderwidth=1,
      bg="snow").grid(row=1, column=1)
Label(main_frame, text=f'prime', borderwidth=1, bg="snow").grid(column=0)

# creating a canvas. Only canvas are scrollable
main_canvas = Canvas(main_frame, bg="light blue")
main_canvas.grid(row=2, column=1, sticky='news')

# Add scrollbars
vscroll = Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
vscroll.grid(row=2, column=2, sticky='ns', pady=(10, 0))
hscroll = Scrollbar(main_frame, orient=HORIZONTAL, command=main_canvas.xview)
hscroll.grid(row=3, column=1, sticky='ew', padx=(10, 0))


# Configure the canvas
main_canvas.configure(yscrollcommand=vscroll.set,
                      xscrollcommand=hscroll.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(
    scrollregion=main_canvas.bbox("all")))

# Create A second frame inside canvas to hold the widgets
second_frame = Frame(main_canvas, bg="bisque")
# second_frame.grid_propagate(False)

# Add the second frame to a window in the canvas
# (0,0) places the second_frame into the upper left corner
main_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# ------------------------------------------------------Calculations-------------------------------------
prime_var = IntVar()
prime_var.set(N)
'''
#instead of generating, loading is faster
master_primes = get_primes_erat(prime_var.get())
'''
with open("prime(10m).txt", "r") as file:
    data = eval(file.readline())
master_primes = limiting(prime_var.get())
primes = master_primes
initiate_label()

# ------------------------------------------------------Others-------------------------------------
# windows zoom


def zoomer(event):
    if (event.delta > 0):
        main_canvas.scale("all", event.x, event.y, 1.1, 1.1)
    elif (event.delta < 0):
        main_canvas.scale("all", event.x, event.y, 0.9, 0.9)
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))


root.bind("<MouseWheel>", zoomer)

'''
def grab(event):
    _y = event.y
    _x = event.x


def drag(event):
    if (_y-event.y < 0):
        main_canvas.yview("scroll", -1, "units")
    elif (_y-event.y > 0):
        main_canvas.yview("scroll", 1, "units")
    if (_x-event.x < 0):
        main_canvas.xview("scroll", -1, "units")
    elif (_x-event.x > 0):
        main_canvas.xview("scroll", 1, "units")
    _x = event.x
    _y = event.y
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))


# Button 3 is the right mouse button
main_canvas.bind("<Button 3>", grab)
main_canvas.bind("<B3-Motion>", drag)
'''

root.mainloop()
