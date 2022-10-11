#!/usr/bin/python3
import os.path
import sys
import re
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
                    help="Width of the SVG image in pixels. Default: 480")
parser.add_argument("--height", type=int, default=720,
                    help="Height of the SVG image in pixels. Default: 720")
parser.add_argument("--background", default="#FFFFFF",
                    help="Background color in hexadecimal. Default: #FFFFFF (white)")
parser.add_argument("--color", default="#000000",
                    help="Stroke color in hexadecimal. Default: #000000 (black)")
parser.add_argument("--stroke", type=int, default=5,
                    help="Stroke width ni pixels. Default: 5")
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
    if os.path.isdir(args.filename):
        print("Error: Filename is a directory")

    color_pattern = re.compile("#[a-fA-F0-9]{6}")
    if not color_pattern.fullmatch(args.background):
        print("Error: The hexadecimal background color is not a valid value")
        sys.exit(1)
    if not color_pattern.fullmatch(args.color):
        print("Error: The hexadecimal stroke color in not a valid value")
        sys.exit(1)
    if args.stroke <= 0:
        print("Error: The stroke width must be a positive integer")
        sys.exit(1)

    d = DrawCistercian(args.width, args.height, args.background, args.color,
                       args.stroke)
    d.draw_number(args.number)

    if not os.path.splitext(args.filename)[1]:
        d.save(args.filename + ".svg")
    else:
        d.save(args.filename)

    if args.verbose:
        print(f"Created image {args.filename} with the cistercian number {args.number}")


if __name__ == "__main__":
    main()
