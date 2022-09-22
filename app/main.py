#!/usr/bin/python3

import sys
from draw_cistercian import DrawCistercian


def main():
    if len(sys.argv) == 3:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Error: The argument is not an integer.")

        d = DrawCistercian(480, 720)
        d.draw_number(n)
        d.save(sys.argv[2])
    else:
        print("Error: You must pass an integer an the name of the file")


if __name__ == "__main__":
    main()
