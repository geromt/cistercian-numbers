#!/usr/bin/python3
import os.path
import sys
import argparse
from draw_cistercian import DrawCistercian

# Configuration of the parser
parser = argparse.ArgumentParser(
    description="Creates a svg image of the integer between 0 and 9999",
    prog="cistercian_cli")
parser.add_argument("number", type=int, help="Integer number that will be draw")
parser.add_argument("-f", "--filename", default="out.svg",
                    help="Filename of the SVG file that will be created")
parser.add_argument("--width", type=int, default=480,
                    help="Width of the SVG image in pixels")
parser.add_argument("--height", type=int, default=720,
                    help="Height of the SVG image in pixels")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Displays more information")


def main():
    args = parser.parse_args()
    if 0 > args.number > 9999:
        print("Error: The number must be an integer between 0 and 9999")
        sys.exit(1)
    if args.width <= 0 or args.height <= 0:
        print("Error: The width and height of the file must be positive")
        sys.exit(1)

    d = DrawCistercian(args.width, args.height)
    # TODO: add stroke size and colors in the options
    d.draw_number(args.number)
    # TODO: if the file exists, ask
    if not os.path.splitext(args.filename)[1]:
        d.save(args.filename + ".svg")
    else:
        d.save(args.filename)

    if args.verbose:
        print(f"Created image {args.filename} with the cistercian number {args.number}")


if __name__ == "__main__":
    main()
