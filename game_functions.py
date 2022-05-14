import sys
import pygame

def check_events(ship):
    '''响应按键和鼠标事件'''

    # 监视事件, 如果退出则关闭窗口循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像, 并切换到新屏幕'''

    # 每次循环时都重绘screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 在屏幕上更新screen(surface对象)内容
    pygame.display.flip()