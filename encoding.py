# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import emoji
import turtle


def library_emoji():
    print(emoji.emojize(":U+1F618:", use_aliases=True))
    print(emoji.emojize(':kissing_face:'))
    print(emoji.emojize(":kissing_face:"))
    print(emoji.emojize('Python is :thumbs_up:'))
    print(emoji.emojize(":grin:", use_aliases=True))
    print(emoji.emojize(":snake:", use_aliases=True))


def turtle_emoji():
    p = turtle.Pen()
    p.write(emoji.emojize(":snake:", use_aliases=True))


if __name__ == '__main__':
    # library_emoji(
    turtle_emoji()