#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *
import os
import re

def ResizeSaveImage(image, layer):
    # Enter the image size to save(default 512)
    # 保存する画像サイズを入力（デフォルト512）
    new_width, new_height=512,512

    pdb.gimp_image_scale_full(image, new_width, new_height,4)
    pdb.gimp_layer_scale(layer, new_width, new_height, False)

    # # Enter the path to save xcf file
    # # XCF ファイルを保存するパスを入力
    # save_path=r"C:\test"
    # gimp.pdb.gimp_file_save(image, save_path, save_path)

    # # Enter the path to save the image
    # 画像を保存するパスを入力
    export_path=r"C:\test"

    files = os.listdir(export_path)
    pattern = re.compile(r'(\d+)\.png')
    max_number = 0
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number
    new_number = max_number + 1
    new_filename = "\\"+str(new_number) + ".png"

    gimp.pdb.file_png_save(image, layer, export_path+new_filename,export_path+new_filename, 0, 0, 0, 0, 0, 0, 0)

    gimp.message("save the image as["+str(new_number)+".png]" )
    # gimp.message("「"+str(new_number)+".png」として画像を保存しました" )
    
register(
        "stuff_image_size",                  #procedure name,プロシージャの名前
        "Resize_and_Save",                   #information of plug in,プラグインの情報
        "Resize the square image, and save it as sequential number",
        # 正方形の画像をリサイズし、連番にリネームして保存"
        #procedurehelp,詳しいプラグインの情報
        "do-etty",                           #author,プラグインの著者
        "do-etty",                           #copyright,コピーライト
        "2024/4/7",                          #Created date,日付
        "<Image>/pyplugin/ResizeSaveImage",  #display name,メニューに表示するプラグイン名
        "RGB*",                              #type of image,画像タイプ
        [
        # (PF_IMAGE, "image", "Input image", None),
        # (PF_LAYER, "layer", "Input layer", None)
        # (PF_DRAWABLE, "drawable", "Drawable", None)
        ],                                   #input,引数
        [],                                  #return,戻り値
        ResizeSaveImage                      # main function name,main関数名
        )

main()