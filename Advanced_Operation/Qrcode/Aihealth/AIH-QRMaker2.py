# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/18
#  @ Author : RichardLau_Cx
#  @ File   : QRMaker.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm

import qrcode
from PIL import Image

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

img = img.convert('RGBA')

# 获取二维码图片的宽高
img_w,img_h = img.size

# 打开logo图片
logo = Image.open("aihealth-logo2.png")

# 获取logo图片的宽高
logo_w,logo_h = logo.size

# 设置logo的大小最大为二维码大小的四分之一
factor = 4
size_w = int(img_w/factor)
size_h = int(img_h/factor)

if logo_w > size_w or logo_h > size_h:
    logo_w = size_w
    logo_h = size_h

# 重新调整logo的尺寸，高质量彩色
logo = logo.resize((logo_w,logo_h),Image.ANTIALIAS).convert('RGBA')

# 设置logo的位置，在二维码图片的中心
l_w = int((img_w-logo_w)/2)
l_h = int((img_h-logo_h)/2)

# 将logo粘贴到二维码上
img.paste(logo,(l_w,l_h),logo)

# 保存二维码
img.save("Aihealth2.png")

# 展示二维码
img.show()
