#!/usr/bin/python3
""" Markdown is awesome! All your README.md are made in Markdown,
    but do you know how Github are rendering them?

    It’s time to code a Markdown to HTML!
"""
import sys
import os


def main(argv):
    """ main - script that ttakes an argument 2 strings:
                first argument is the name of the markdown file.
                second argument is the output file name.
    """
    if len(argv) < 2:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    try:
        f = open("README.md", "r")
        exit(0)
    except IOError:
        print("Missing {}".format(argv[1]))
    exit(1)
    
if __name__ == "__main__":
    main(sys.argv)
