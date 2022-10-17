#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Oct. 5, 2022
# This program asks the user to guess a number between 0 and 9
import random


def main():

    guess = int(input("guess number between 0 and 9:"))
    max_number = 9
    int(random.randint(1, max_number))
    if guess == random.randint:
        print("guessed correctly!")
    else:
        print("Wrong guess. The number was")


if __name__ == "__main__":
    main()
