# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/27
#  @ Author : RichardLau_Cx
#  @ File   : anniversary_of_the_founding_100.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm

# 为了我党建立100周年的纪念LED


import pygame
import pprint


def main():
    # 初始化字体模块
    pygame.init()

    # 初始化字体模块
    pygame.font.init()

    # 如果字体模块已初始化，则为true
    # print('是否初始化', pygame.font.get_init())
    # 获取默认字体的文件名
    # print('默认字体名', pygame.font.get_default_font())

    # 获取所有可用的字体
    # pprint.pprint(pygame.font.get_fonts())

    # 在系统上找到特定的字体
    # print('查找字体', pygame.font.match_font('arial'))

    # 从系统字体创建一个Font对象
    # （名称，大小，粗体=假，斜体=假） - >字体
    a = pygame.font.SysFont('华文行楷', 50)

    # 从文件或对象绘制文本
    # pygame.font.Font('文件或对象',大小)

    # 在新Surface上绘制文本
    # 显示内容、是否消除锯齿、字体颜色、背景颜色
    # text = a.render("庆祝建党第一百周年 --我爱你祖国", True, (255, 255, 255), (255, 0, 0))
    text = a.render("热烈庆祝建党一百周年 --我爱你中国(^_-)", True, (255, 245, 0), (255, 0, 0))

    # 取消初始化字体模块
    # pygame.font.quit()
    # 设置屏幕尺寸
    # screen = pygame.display.set_mode((500, 100))
    screen = pygame.display.set_mode((600, 150))
    # 设置矩形区域
    ztx, zty, ztw, zth = text.get_rect()
    # 绘制显示文字的矩形区域
    # jx = pygame.Rect(500, 50 - zth / 2, ztw, zth)  # 初始位置设置屏幕右边，并居住显示，2/1屏幕的高度 - 2/1字体的高度 向上移动是减
    jx = pygame.Rect(600, 75 - zth / 2, ztw, zth)  # 初始位置设置屏幕右边，并居住显示，2/1屏幕的高度 - 2/1字体的高度 向上移动是减
    # 设置游戏时钟
    clock = pygame.time.Clock()

    while True:
        # 文字滚动的频率
        clock.tick(20)
        # 重绘屏幕
        screen.fill((0, 0, 0))
        # 退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        # 文字从右向左移动
        jx.x -= 5

        # 如果字体全部移动出屏幕，则设置字体X轴位置为510, 500的话会出现的比较突然
        if jx.x < 0 - ztw:
            jx.x = 510
        # 屏幕绘制字体，
        screen.blit(text, [jx.x, jx.y])
        # 更新屏幕显示
        pygame.display.update()


if __name__ == '__main__':
    main()