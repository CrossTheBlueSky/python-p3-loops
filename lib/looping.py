#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    squares = []
    for i in int_list:
        squares.append(i**2)
        print(squares)
    return squares


def fizzbuzz():
    i = 1
    while i <= 100:
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if out == "":
            out = i
        print(out)
        i += 1
