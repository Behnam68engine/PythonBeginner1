# from tkinter import *
# import tkinter as tk
from tkinter import Tk
from typing import Any
# a1 = tk.Tk()
a1 = Tk()

a1.config(bg="red")
a1.title("Behi")
A2 = 2
B2 = 1000000
print(A2*B2)
print(A2/B2)
#print(A2**B2)
A3 = 2
B3 = 3
C3 = 4
print(A3 + B3 + C3)
X1 = 2000
Y1 = 10
Q1 = "salam"
print(Q1)
print(X1)


def f_x(a_4: Any, b_4: Any) -> None:
    """Calculates the product of two numbers and prints the result.

    Args:
        a_4 (Any): The first number.
        b_4 (Any): The second number.

    Returns:
        None: This function does not return anything; it prints the result.
    """
    print(a_4*b_4+1)
    print("salam2")


# y1
f_x(5, 60)
A5 = 12
B5 = 45
C5 = A5 * B5
print(C5)

x2 = input()
