from pygame.sprite import Group
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():

    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    
    # 创建一个ufo群
    ufos = Group()
    gf.creat_fleet(ai_settings, screen, ufos)

    # 开始游戏循环
    while True:
        gf.check_events(ship)
        ship.fire()
        ship.update()
        ship.bullets.update()
        gf.update_screen(ai_settings, screen, ship, ufos)

run_game()