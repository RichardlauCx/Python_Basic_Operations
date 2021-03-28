# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/26
#  @ Author : RichardLau_Cx
#  @ File   : anniversary_of_the_founding_100.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm


import jieba
import imageio
import wordcloud
from PIL import Image


# 打开文件
txt = open("text100.txt", encoding="utf8")
text = txt.read()


# 使用jieba分词对文件进行中文分词
wordlist_jieba = jieba.lcut(text, cut_all=False)
wl_jb_txt = " ".join(wordlist_jieba)  # 将分词后的数据转化为字符串并用空格隔开


# imread函数并使用函数读取本地图片
mk = imageio.imread("map.jpg")


# 并配置词云对象w的参数
font = "C:\\Windows\\Fonts\\STXINGKA.TTF"  # 词云的中文字体所在路径

w = wordcloud.WordCloud(max_words=2000,

                        font_path=font,  # 这里要设置，否则中文会乱码

                        mask=mk,  # 指定mk为词云形状图片

                        background_color="red",

                        scale=5)


# 加载词云文本
w.generate(wl_jb_txt)

# 输出词云文件
filename = "建党100周年词云图.jpg"
w.to_file(filename)

cloud = Image.open(filename)
cloud.show()


