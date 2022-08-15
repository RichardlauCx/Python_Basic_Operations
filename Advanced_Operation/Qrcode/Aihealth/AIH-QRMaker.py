# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/18
#  @ Author : RichardLau_Cx
#  @ File   : QRMaker.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm

import qrcode

from PIL import Image
import matplotlib.pyplot as plt

"""

# 调用制作QR方法，传入url或者想要展示的内容，提供简单调用接口
# qr = qrcode.make('https://www.baidu.com/')
qr = qrcode.make('欢迎使用QR生成接口')
# qr = qrcode.make('https://kg.qq.com/node/personal?uid=6a9b9b83242c3082&chain_share_id=bRIY3jN-no96MebGznCipWFPW00oqMZe9-ZTMXOKzU4')

with open('welcome.png', 'wb') as f:
    qr.save(f)
    
"""

# data = 'https://kg.qq.com/node/personal?uid=6a9b9b83242c3082&chain_share_id=bRIY3jN-no96MebGznCipWFPW00oqMZe9-ZTMXOKzU4'  # 提供数据源
data = 'https://www.aihnet.cn/?page_id=6532&lang=zh'  # 提供数据源
# QRFile = r'qr.png'
QRFile = r'products.png'  # 生成二维码名称

# 实例化QRCode类对象
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# 传入数据
qr.add_data(data)
qr.make(fit=True)

# 生成二维码
img = qr.make_image()

# 添加logo，打开logo照片
icon = Image.open("aihealth-logo.png")
# 获取图片的宽高
img_w, img_h = img.size
# 参数设置logo的大小
factor = 6
size_w = int(img_w / factor)
size_h = int(img_h / factor)
icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
# 重新设置logo的尺寸
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
# 得到画图的x，y坐标，居中显示
w = int((img_w - icon_w) / 2)
h = int((img_h - icon_h) / 2)
# 黏贴logo照
img.paste(icon, (w, h), mask=None)
# 终端显示图片
plt.imshow(img)
plt.show()
# 保存img
img.save("Aihealth.png")


# # 保存二维码
# QR.save(QRFile)
#
# # 展示二维码
# QR.show()