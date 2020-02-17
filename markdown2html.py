#!/usr/bin/python3
""" Markdown is awesome! All your README.md are made in Markdown,
    but do you know how Github are rendering them?

    It’s time to code a Markdown to HTML!
"""
import sys
import os
import fnmatch
import re
import hashlib


def inline_tags2(line, group):
    if group[0] == "[":
        hashed = hashlib.md5(group.encode())
        # print(str(hashed))
        return line.replace(group, hashed.hexdigest())
    else:
        new_group = group.replace("C", "")
        new_group = new_group.replace("c", "")
        new_group = new_group.replace("(", "")
        new_group = new_group.replace(")", "")
        return line.replace(group, new_group)

def inline_tags(line, group):
    md_inline = {"**": "b", "__": "em"}
    line = line.replace(group, "<" + md_inline[group] + ">", 1)
    line = line.replace(group, "<" + "/" + md_inline[group] + ">", 1)
    return line

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
        inline = re.compile(".*([**].*[**]|[__].*[__]).*")
        inline2 = re.compile(".*(\[\[.*\]\]).*")
        inline3 = re.compile(".*(\(\(.*\)\)).*")
        line_dict = {}
        lines = []
        listing = 0
        paragraph = 0
        with open(argv[2], "w+") as fhtml, open(argv[1], "r") as fmd:
            fmd = fmd.readlines()
            for i, line in enumerate(fmd):
                while inline.match(line):
                    # print("called!")
                    match = inline.match(line)
                    # print(match, group)
                    line = inline_tags(line, match.group(1))
                    # print(line)
                while inline2.match(line):
                    match = inline2.match(line)
                    group = match.group(1)
                    line = inline_tags2(line, group)
                if inline3.match(line):
                    match = inline3.match(line)
                    group = match.group(1)
                    line = inline_tags2(line, group)
                    # print(line)
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
