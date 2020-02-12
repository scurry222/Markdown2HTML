#!/usr/bin/python
import sys
import os

def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    try:
        f = open("README.md", "r")
        exit(0)
    except Exception:
        print("Missing <filename>")
        exit(1)

if __name__ == "__main__":
    main(sys.argv)