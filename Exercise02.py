#!/usr/bin/evn python3

# Write a function named print_right that takes a string named text as a
# parameter and prints the string with enough leading spaces that the last letter
# of the string is in the 40th column of the display.
def print_right01(text, spaces=40):
    spaces -= len(text)
    ws = ""
    while spaces > 0:
        ws += ' '
        spaces -= 1
    print(ws + text)

def print_right02(text, spaces=40):
    spaces -= len(text)
    ws = ' '*spaces
    print(ws + text)

def print_right03(text, spaces=40):
    print( f"{text:>{spaces}}" )

def print_right04(text, spaces=40):
    line = ' '*spaces + text
    print(line[-spaces:])

print_right01('Monty')
print_right02("Python's")
print_right03('Flying Circus')
print_right04('was amazing!?!')