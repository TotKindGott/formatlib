#!/usr/bin/env python

__all__ = ['strip_mdown']


def strip_mdown(text):
    # Takes a Markdown-formatted string and returns it in plain text format
    
    from HTMLParser import HTMLParser
    from BeautifulSoup import BeautifulSoup as bs
    from markdown import markdown as md
    
    parser = HTMLParser()
    
    return parser.unescape(''.join(bs(md(text)).findAll(text=True)))

