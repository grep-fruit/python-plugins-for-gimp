#!/usr/bin/env python

'''Change font size, for every text layer in a GIMP image.
   Only affects images at the top level: does not descend into layer groups.
   
   Based on Akkana Peck's script here : https://github.com/akkana/gimp-plugins/blob/master/changefont.py, which I split into three parts because it's more convenient for me to handle them separately.
'''

# to add later : initial color of the color selector is active foreground color (instead of white)


from gimpfu import *

def python_change_font_color(img, fontcolor):
    pdb.gimp_image_undo_group_start(img)

    for l in img.layers:
        if not pdb.gimp_item_is_text_layer(l):
            continue
        pdb.gimp_text_layer_set_color(l, fontcolor)

    pdb.gimp_image_undo_group_end(img)

register(
    "python_fu_change_color",
    "Change every text layer in an image to a new color",
    "Change every text layer in an image to a new color",
    "Akkana Peck",
    "Akkana Peck",
    "2016,2019",
    "Change Color in all Text Layers.",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_COLOR, "fontcolor", "Color", (100.0, 100.0, 100.0)),
    ],
    [],
    python_change_font_color,
    menu="<Image>/Functionality")

main()
