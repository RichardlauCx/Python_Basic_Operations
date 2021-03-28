# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter

# resolution ratio：240 * 60
WIDTH = 60 * 4
HEIGHT = 60


def rndColor_background():
    """
    生成随机颜色，返回RGB色彩空间（验证码背景）
    :return:R,G,B
    """
    return \
        (
            random.randint(64, 255),
            random.randint(64, 255),
            random.randint(64, 255),
        )


def rndChar():
    """
    由大写字母对应的ASCII码值来随机生成
    :return: 随机字母
    """
    return chr(random.randint(65, 90))


def rndColor_char():
    """
    生成随机颜色，返回RGB色彩空间（验证码字符）
    :return:R,G,B
    """
    return \
        (
            random.randint(32, 255),
            random.randint(32, 255),
            random.randint(32, 255),
        )


def start():
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))  # 创建新图像，白色初始底色

    font = ImageFont.truetype("arial.ttf", 36)  # 创建Font对象（字体首字母得小写）
    # font = ImageFont.truetype("symbol.ttf", 36)  # 创建Font对象
    draw = ImageDraw.Draw(img)  # 创建Draw对象

    # 填充每个像素，为随机颜色
    for x in range(WIDTH):
        for y in range(HEIGHT):
            draw.point((x, y), fill=rndColor_background())
            
    # 输出验证码上的数字
    for t in range(4):
        draw.text((60*t + 10, 10), rndChar(), font=font, fill=rndColor_char())

    # 模糊操作
    image = img.filter(ImageFilter.BLUR)

    image.show()

    image.save("CAPTCHA.jpg", "jpeg")  # 这两个指的是一种格式


if __name__ == '__main__':
    start()
