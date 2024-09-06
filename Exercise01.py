#!/usr/bin/evn python3

# 1. Ask your favorite VA to "Write a function called repeat that takes a string
# and an integer and prints the string the given number of times."
def repeat(string, n):
    print(string * n)  # ha ha ha, no for

# 2. If the result uses a for loop, you could ask, "Can you do it without a for loop?"

# No for loop, but still VERY funny because there's no mention of why this is a pointless
# function to write given it's already implemented with the * operator.

# 3. Pick any other function in this chapter and ask a VA to write it. The
# challenge is to describe the function precisely enough to get what you want.
# Use the vocabulary you have learned so far in this book.

# Write me a python function, or set of functions, that can act as a template for
# creating ad-lib songs:
import random


def generate_verse(noun, verb, adjective, adverb):
    # Template for a verse with placeholders for words
    verse = f"""
    {adjective.capitalize()} {noun}, {adjective} {noun}
    You {verb} so {adverb}, {adjective} {noun}
    """
    return verse


def generate_chorus(noun, adjective):
    # Template for a chorus
    chorus = f"""
    Oh {adjective} {noun}, my {adjective} {noun}
    You make me feel so {adjective}, {noun}
    """
    return chorus


def generate_song(nouns, verbs, adjectives, adverbs):
    # Randomly selecting words from the lists for verses and chorus
    noun = random.choice( nouns )
    verb = random.choice( verbs )
    adjective = random.choice( adjectives )
    adverb = random.choice( adverbs )

    # Constructing the song
    song = ""
    for i in range( 2 ):  # 2 verses
        song += generate_verse( noun, verb, adjective, adverb )
        song += "\n"

    song += generate_chorus( noun, adjective )  # Chorus

    return song


# Example usage
nouns = ["Trevor", "Grumpy Cat", "skeptical Baby Yoda", "roll safe"]
verbs = ["flip", "prance", "giggle", "twirl"]
adjectives = ["amusing", "zany", "quirky", "loony"]
adverbs = ["absurdly", "bonkers", "nutty", "hysterically"]

song = generate_song( nouns, verbs, adjectives, adverbs )
print( song )
