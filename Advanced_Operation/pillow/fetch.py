# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import PIL
from PIL import Image, ImageFilter


if __name__ == '__main__':
    # image = Image.open("OET.jpg")
    image = Image.open("Tower-Bridge-2.jpg")

    # image.thumbnail((666, 666), Image.ANTIALIAS)  # 缩略图
    img = image.filter(ImageFilter.BLUR)

    image.show()  # 图片展示

    # image.save("Tower-Bridge-2.png")  # 可以转化文件格式
    image.save("Tower-Bridge-2.jpg", "jpeg")  # 可以转化文件格式，此提到格式为有损压缩格式
