import pygame
import game_functions as gf
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():

    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    pygame.font.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的示例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    
    # 创建一个ufo群
    ufos = Group()
    gf.create_fleet(ai_settings, screen, ufos)

    # 开始游戏循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, ufos)

        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ship)
            gf.update_ufos(ai_settings, ufos)
            gf.process_collision(ai_settings, stats, screen, ship, ufos)
            gf.check_ufos_bottom(ai_settings, stats, screen, ship, ufos)
            
        gf.update_screen(ai_settings, stats, screen, ship, ufos,
                                play_button)
            

run_game()