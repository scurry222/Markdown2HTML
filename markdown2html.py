#!/usr/bin/python3
""" Markdown is awesome! All your README.md are made in Markdown,
    but do you know how Github are rendering them?

    It’s time to code a Markdown to HTML!
"""
import sys
import os
import fnmatch


def main(argv):
    """ main - script that takes an argument 2 strings:
                first argument is the name of the markdown file.
                second argument is the output file name.
    """
    if len(argv) < 3 or not fnmatch.fnmatchcase(argv[1], "*.md") or not\
            fnmatch.fnmatchcase(argv[2], "*.html"):
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)
    try:
        d = {}
        lines = []
        with open(argv[1], "r") as fmd:
            for i, line in enumerate(fmd):
                key, value = i, len(line) - len(line.lstrip("#"))
                d[key] = value
                line = line.lstrip("# ")
                lines.append(line.rstrip("\n"))
        with open(argv[2], "w+") as fhtml:
            for k, v in d.items():
                if d[k] and 0 < d[k] < 7:
                    fhtml.write("<h{}>".format(d[k]) + lines[k] +
                                "</h{}>\n".format(d[k]))
        exit(0)
    except IOError:
        sys.stderr.write("Missing {}\n".format(argv[1]))
    exit(1)

if __name__ == "__main__":
    main(sys.argv)
