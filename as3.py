#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program allows the user to input his/her age


def main():

    # input
    age = int(input(" add age here: "))

    # process & output
    if age > 18:
        print(" You can vote! ")
    elif age < 18:
        print("You cant vote sorry! ")



if __name__ == "__main__":
    main()
