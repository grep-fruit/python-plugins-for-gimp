#!/usr/bin/env python2

# this is a script from a walkthrough youtube tutorial that I am doing to learn

from gimpfu import *

def center_elements(image, drawable):
    return

register(
    "Center",
    "Center visible layers in the file.",
    "Center elements.",
    "Alex from youtube",
    "Alex Zorzella",
    "2021",
    "<Image>/Tools/Center_Elements",
    "*",
    [

    ],
    [],
    center_elements) 

main()
