#!/usr/bin/env python3
import random
import string
import secrets
import sys
import os.path
from os import path

n = 14


def build_string_with_secrets():
    # Use secrets module for strong cross-platform entropy
    # https://docs.python.org/3/library/secrets.html#recipes-and-best-practices
    # Python 3.10 or above for 'secrets' support
    if sys.version_info < (3, 10):
        raise Exception("Use only with Python 3.10 or higher")
    my_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_" + "-"
    secret_string = ''.join(secrets.choice(my_alphabet) for i in range(n))

    return secret_string


def build_string_with_srandom():
    # Use random.SystemRandom().shuffle strong Linux/Unix entropy
    # Shuffle has a limited life, ending in 3.11
    # "Deprecated since version 3.9, will be removed in version 3.11"
    # https://docs.python.org/3/library/random.html?highlight=systemrandom#random.SystemRandom
    universe = ["a", "b", "c", "d", "e", "f", "g", "h", 
            	"i", "j", "k", "l", "m", "n", "o", "p", 
            	"q", "r", "s", "t", "u", "v", "w", "x", 
            	"y", "z", "A", "B", "C", "D", "E", "F", 
            	"G", "H", "I", "J", "K", "L", "M", "N", 
            	"O", "P", "Q", "R", "S", "T", "U", "V", 
            	"W", "X", "Y", "Z", "0", "1", "2", "3",
            	"4", "5", "6", "7", "8", "9", "_", "-"]

    rand_string = ""
    # shuffle all characters
    # generate other characters
    for i in range(n):
        random.SystemRandom().shuffle(universe)
        rand_string += random.choice(universe)
    return rand_string


def build_string_with_srandom_sample():
    my_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_" + "-"
    srandom_list = []
    srandom_string = ""
    for i in range(n):
        srandom_list += random.SystemRandom().sample(my_alphabet, k=1)
    return srandom_string.join(srandom_list)


def build_string_with_srandom_samplev2():
    my_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_" + "-"
    srandom_string = ""
    srandom_list = random.SystemRandom().sample(my_alphabet, k=n)
    return srandom_string.join(srandom_list)


if __name__ == '__main__':
    # Unfinished experimenting with different ways to 
    # create 'unique' strings, a common requirement
    print(f"Using Secrets:                     {build_string_with_secrets()}")
    print(f"Using random.SystemRandomShuffle:  {build_string_with_srandom()}")
    print(f"Using random.SystemRandomSample:   {build_string_with_srandom_sample()}")
    print(f"Using random.SystemRandomSamplev2: {build_string_with_srandom_samplev2()}")






