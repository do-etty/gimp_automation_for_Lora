#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *
import os
import re

def FitSizeToLarger(image, layer):
    width, height = image.width , image.height
    
    if height >= width:
        new_width,new_height = height,height
        gimp.message("set width to height" )
        # gimp.message("幅を高さに合わせました" )
    else:
        new_width,new_height = width,width
        gimp.message("set height to width" )
        # gimp.message("高さを幅に合わせました" )
    
    off_width= (new_width - width)/2
    off_height= (new_height - height)/2

    pdb.gimp_image_resize(image,new_width,new_height,off_width,off_height)

    pdb.gimp_layer_resize(layer,new_width,new_height,off_width,off_height)

# registration to gimp
# gimpへの登録 
register(
        "fit_side_to_larger",                #procedure name,プロシージャの名前
        "fit_side_to_largert",               #information of plug in,プラグインの情報
        "Resize the image width and height to match the larger size",
        # 画像のサイズを高さと幅の大きい方に合わせる
        #procedurehelp,詳しいプラグインの情報
        "do-etty",                           #author,プラグインの著者
        "do-etty",                           #copyright,コピーライト
        "2024/4/7",                          #Created date,日付
        "<Image>/pyplugin/FitWidthToHeight", #display name,メニューに表示するプラグイン名
        "RGB*",                              #type of image,画像タイプ
        [
        # (PF_IMAGE, "image", "Input image", None),
        # (PF_LAYER, "layer", "Input layer", None)
        # (PF_DRAWABLE, "drawable", "Drawable", None)
        ],                                  #input,引数
        [],                                 #return,戻り値
        FitSizeToLarger                     # main function name,main関数名
        )

main()