# Prime-visualizer

This is a small project testing out the Tkinter package to create a GUI. What I want to visualize are prime numbers. For this, this program has 3 functions:

1. Visualizing prime number factors of all numbers up to X.
2. Prime spiral, with settings to ignore certain numbers
3. Fetch all prime numbers (up to X) that end with the desired suffix.

For faster calculations, the prime numbers are fetched from a list of prime numbers up to 10 million (instead of being calculated every time). This list is generated and a code for generating such a list is included in the "scribble.ipynb" python notebook.

## 1. Visualizing prime number factors of all numbers up to X.

This is the main visualizer when starting the program. It consist of a main large area (grid). The column header (x-axis) shows the numbers up to X. The row header (y-axis) shows the prime numbers up to X (as such, the y-axis will alway be shorter than the x-axis).

GUI settings (top left):
(from left to right)

* **Black Prime**: field are coloured black when the primes (row) are factors of the number (column).
* **Gray**: same as **Black Prime**, however the colouring starts at white and turns darker at larger prime numbers (grayscale that turns darker towards the bottom rows).
* **Column**: Column uses the shading from **Gray**. It takes the darkest shade in the column and shades the whole column up to the largest prime factor, which is not the number itself (columns with no shadings will be prime numbers). In this regard, the column setting can be overlayed with the previous two setting.
* **text field + Update**: input number to limit the number of primes (rows) to visualize. With a number inside, press Update to apply setting.
* **RESET**: erases the board of visualizations.

Other settings that can be changed inside the code:

* **Maximum Number**: The upper limit for numbers (both numbers and prime numbers do not exceed this Maximum number)
* **Height & Width**: The starting window size
* **fontsize**: fontsize

*Currently the control using the mouse wheel is dodgy. Plan to fix it or remove it altogether.*

## 2. Prime spiral.

A prime spiral (or ulam spiral) is a visualization of numbers starting from the center and expands outward like a spiral with each additional number. Numbers that are prime are coloured distinctively. For more info, see the [wikipedia page](https://en.wikipedia.org/wiki/Ulam_spiral).

The prime spiral can be accessed on the top right. Given a number (up to 3162) and pressing **Generate Spiral** will generate a prime spiral with the diameter of the input number. The limit of the prime number however is the **Maximum Number^2**.

The **RESET** button can be used to return back to the initial window.

Other settings that can be changed inside the code:

* **starting_number**: indicates the starting number of the spiral. (what number the red square in the middle is)
* **number_progression**: determines the step size of the spiral when numbers are added. I.e. a **number_progression** of 2 would skip every other number.  
*care must be taken so that enough prime numbers exists to build the spiral. For example, if the setting for both are set to 2, then no prime numbers will fit the criteria as only even numbers are considered*

*Due to the nature of how this visualization works, visualizing large numbers turns the black squares into rectangles in order to fit the number into it*

## 3. Prime Numbers Fetcher

Clicking the **Prime numbers** button at the bottom opens a new window for the prime number fetcher function. This tool finds all the prime numbers with a given suffix. At the top left, input the ending digits (suffix) inside the text box and then press **Generate** to generate the table of prime numbers that fit the criteria. The resulting table will show all fitting prime numbers separate in columns corresponding to the number of digits.

The right window outputs some statistics. The proportion of primes up to X that fit the suffix criteria and the number of primes with specific number of digits. The bottom of this window then shows the distribution of the digit number of all the fitting prime numbers. The rows indicate the number from 0-9. The columns indicate the digits.

Other settings that can be changed inside the code:

* **magnitude**: sets the upper size for the largest number to be considered.
