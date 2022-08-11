#!/usr/bin/env python

'''Change font size for every text layer in a GIMP image.
   Only affects images at the top level: does not descend into layer groups.
   
   Based on Akkana Peck's script here : https://github.com/akkana/gimp-plugins/blob/master/changefont.py, which I split into three parts because it's more convenient for me to handle them separately.
'''


from gimpfu import *

def python_change_font(img, fontsize):
    pdb.gimp_image_undo_group_start(img)

    for l in img.layers:
        if not pdb.gimp_item_is_text_layer(l):
            continue
        pdb.gimp_text_layer_set_font_size(l, fontsize, 0)

    pdb.gimp_image_undo_group_end(img)

register(
    "python_fu_change_size",
    "Change every text layer in an image to a new size",
    "Change every text layer in an image to a new size",
    "Akkana Peck", # do I write my own name here? idk
    "Akkana Peck",
    "2016,2019",
    "Change Size in all Text Layers.",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_SPINNER, "fontsize", "New Font Size",
         50, (1, 500, 1)),
    ],
    [],
    python_change_font,
    menu="<Image>/Functionality")

main()
