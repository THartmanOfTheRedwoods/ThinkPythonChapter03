#!/usr/bin/env python3

# Write a function called bottle_verse that takes a number as a parameter and
# displays the verse that starts with the given number of bottles.

def bottle_verse(n):
    if n <= 0: return
    print(f"""{n} bottle{'' if n == 1 else 's'} of beer on the wall
{n} bottle{'' if n == 1 else 's'} of beer 
Take one down, pass it around
{n-1} bottle{'' if n-1 == 1 else 's'} of beer on the wall
    """)

def bottle_song(n):
    for verse in range(n, -1, -1):
        bottle_verse(verse)

bottle_song(99)