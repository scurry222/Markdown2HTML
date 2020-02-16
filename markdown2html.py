#!/usr/bin/python3
""" Markdown is awesome! All your README.md are made in Markdown,
    but do you know how Github are rendering them?

    It’s time to code a Markdown to HTML!
"""
import sys
import os
import fnmatch


def write_list(fhtml, line_dict, k, lines, tag):
    while line_dict[k] and line_dict[k] == tag:
        fhtml.write("<li>" + lines[k] + "</li>" + "\n")
        k += 1
    fhtml.write("</{}>\n".format(line_dict[k-1]))
    return k


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
        md = {1: "h1", 2: "h2", 3: "h3", 4: "h4", 5: "h5", 6: "h6", "-": "ul", "*": "ol"}
        line_dict = {}
        lines = []
        listing = 0
        paragraph = 0
        with open(argv[2], "w+") as fhtml, open(argv[1], "r") as fmd:
            fmd = fmd.readlines()
            for i, line in enumerate(fmd):
                if len(line) - len(line.lstrip("#")) > 0:
                    tag = md[len(line) - len(line.lstrip("#"))]
                    line = line.lstrip("# ")
                    line = line.rstrip("\n ")
                    fhtml.write("<{}>".format(tag) + line + "</{}>\n".format(tag))
                    # print(tag)
                elif len(line) - len(line.lstrip('-* ')) > 0:
                    tag = md[line[0]]
                    # print(line[0], tag)
                    strip = line.lstrip("*- ")
                    strip = strip.rstrip("\n")
                    if listing != 1:
                        fhtml.write("<{}>\n".format(tag))
                        listing = 1
                    fhtml.write("<li>" + strip + "</li>" + "\n")
                    # print(listing)
                    if i == len(fmd) - 1 or fmd[i+1][0] != line[0]:
                        fhtml.write("</{}>\n".format(tag))
                        listing = 0
                elif line.split(" ")[0] not in md:
                    if line[0] != "\n":
                        if paragraph != 1:
                            fhtml.write("<p>\n")
                            paragraph = 1
                        fhtml.write(line)
                        # if next line is part of the paragraph
                        if i != len(fmd) - 1 and fmd[i + 1][0] != "\n" and fmd[i + 1][0] not in md:
                            fhtml.write("<br/>\n")
                        else: 
                            fhtml.write("</p>\n")
                            paragraph = 0
        exit(0)
    except IOError:
        sys.stderr.write("Missing {}\n".format(argv[1]))
    exit(1)

if __name__ == "__main__":
    main(sys.argv)
