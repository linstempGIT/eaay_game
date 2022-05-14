import sys
import pygame
from settings import Settings

def run_game():

    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width,
        ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏循环
    while True:

        # 监视事件, 如果退出则关闭窗口循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘screen
        screen.fill(ai_setting.bg_color)

        # 在屏幕上更新screen(surface对象)内容
        pygame.display.flip()

run_game()