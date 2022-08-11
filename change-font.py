#!/usr/bin/env python

'''Change font face for every text layer in a GIMP image.
   Only affects images at the top level: does not descend into layer groups.

   Based on Akkana Peck's script here : https://github.com/akkana/gimp-plugins/blob/master/changefont.py, which I split into three parts because it's more convenient for me to handle them separately.
'''


from gimpfu import *

def python_change_font(img, fontface):
    pdb.gimp_image_undo_group_start(img)

    for l in img.layers:
        if not pdb.gimp_item_is_text_layer(l):
            continue
        pdb.gimp_text_layer_set_font(l, fontface)

    pdb.gimp_image_undo_group_end(img)

register(
    "python_fu_change_font",
    "Change every text layer in an image to a new font",
    "Change every text layer in an image to a new font",
    "Akkana Peck",
    "Akkana Peck",
    "2016,2019",
    "Change Font in all Text Layers.",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_FONT, "fontface", "New Font", "Sans"),
        # problem : shows only option Sans and crashes if i try to select another one
        # probable cause of the problem : doesn't call for the font list or give any option to select from a menu or type it
    ],
    [],
    python_change_font,
    menu="<Image>/Functionality")

main()
