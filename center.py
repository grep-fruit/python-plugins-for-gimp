#!/usr/bin/env python2

# this is a script from a walkthrough youtube tutorial that I am doing to learn  https://www.youtube.com/watch?v=8z0VEFBSgqA (channel : CodeGnat Studios)

from gimpfu import *

def center_elements(image, drawable, y_pos):
    layers = []
    listAllVisible(image, layers)

    for layer in layers:
        pdb.gimp_layer_set_offsets(layer, image.width / 2 - layer.width / 2, y_pos)

    return

# grab visible layers
# pdb is the thing that gimp has
def listAllVisible(parent, outputlist):
    for layer in parent.layers:
        if pdb.gimp_layer_get_visible(layer):
            outputlist.append(layer)
            if pdb.gimp_item_is_group(layer):
                listAllVisible(layer, outputlist)


register(
    "Center",
    "Center visible layers in the file.",
    "Center elements.",
    "Alex Zorzella",
    "Alex Zorzella",
    "2021",
    "<Image>/Functionality/Center_Elements",
    "*",
    [
        (PF_FLOAT, "y_pos", "Y Position :", 0)
    ],
    [],
    center_elements)

main()
