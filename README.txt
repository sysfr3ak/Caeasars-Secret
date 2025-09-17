  ____                           _       ____                     _   
 / ___|__ _  ___  ___  __ _ _ __( )___  / ___|  ___  ___ _ __ ___| |_ 
| |   / _` |/ _ \/ __|/ _` | '__|// __| \___ \ / _ \/ __| '__/ _ \ __|
| |__| (_| |  __/\__ \ (_| | |    \__ \  ___) |  __/ (__| | |  __/ |_ 
 \____\__,_|\___||___/\__,_|_|    |___/ |____/ \___|\___|_|  \___|\__|


Caesar Cipher CTF Challenge
===========================

Made by: ISUKA VISATH

Your Mission
------------
In this challenge, you are given a file called `resources.py`. This file contains:
- A list of 50 encrypted flags.
- A list of lowercase alphabet letters to help you with your decoding efforts.
- A list of common dictionary words.

One of the 50 flags is the correct flag that makes sense when decoded — the other 49 are gibberish!

What's a Caesar Cipher?
-----------------------
The Caesar Cipher is a type of substitution cipher where each letter in the text is shifted
by a fixed number down the alphabet. For example, with a shift of 3:
- a → d
- b → e
- c → f

Check out more about Caesar Cipher here if you're not familiar with it!

Instructions
------------
1. Write a Python script that:
   - Loops through all the 50 flags in the list.
   - Attempts to decode each flag with every possible shift.
   - Identifies the flag that makes sense in English.

2. The number of shifts is not provided!

3. The alphabet list, encrypted flags list, and a common dictionary words list are
   included in `resources.py`.
