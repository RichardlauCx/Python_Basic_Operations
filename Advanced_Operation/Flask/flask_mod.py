# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import flask
from flask import Flask

app = Flask(__name__)  # flask 实例，传入当前调用函数名
url = "/"
# url = "/test/index.html"
# url = r"\F:\Computer\Web_leading_end\网页设计作品--Wolf pack（蓝色网络）\index.html"


@app.route(url)  # 通过URL，路由到对应资源（若仅为一个斜杠，则对应下面的函数返回值）
# @app.route('/hello')
def hello():
    return "Hello RichardLau_Cx!"


def test():
    print(flask.__doc__)
    print(flask.__version__)


if __name__ == '__main__':
    # test()
    app.run()  # 默认会以一个5000端口来运行
