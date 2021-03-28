# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/18
#  @ Author : RichardLau_Cx
#  @ File   : QRMaker.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm

import qrcode

"""
# 调用制作QR方法，传入url或者想要展示的内容，提供简单调用接口
# qr = qrcode.make('https://www.baidu.com/')
qr = qrcode.make('欢迎使用QR生成接口')
# qr = qrcode.make('https://kg.qq.com/node/personal?uid=6a9b9b83242c3082&chain_share_id=bRIY3jN-no96MebGznCipWFPW00oqMZe9-ZTMXOKzU4')

with open('welcome.png', 'wb') as f:
    qr.save(f)
    
"""

data = 'https://kg.qq.com/node/personal?uid=6a9b9b83242c3082&chain_share_id=bRIY3jN-no96MebGznCipWFPW00oqMZe9-ZTMXOKzU4'  # 提供数据源
QRFile = r'qr.png'

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
QR = qr.make_image()

# 保存二维码
QR.save(QRFile)

# 展示二维码
QR.show()