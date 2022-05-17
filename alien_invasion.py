import pygame
import game_functions as gf
from button import Button
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from shipboard import Shipboard


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
    play_button = Button(screen, "Play")

    # 创建一个用于存储游戏统计信息的示例
    stats = GameStats()

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    
    # 创建一个ufo群
    ufos = Group()
    gf.create_fleet(screen, ai_settings, ufos)

    # 新建一个计分榜
    scb = Scoreboard(screen, stats)

    # 新建一个飞船信息栏
    shb = Shipboard(screen, ship)

    # 开始游戏循环
    while True:
        gf.check_events(screen, ai_settings, play_button, stats, ship, ufos)

        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ship)
            gf.update_ufos(ai_settings, ufos)
            gf.process_collision(ai_settings, stats, screen, ship, ufos)
            gf.check_ufos_bottom(ai_settings, stats, screen, ship, ufos)
            
        gf.update_screen(screen, ai_settings, play_button, stats, ship, ufos,
                            scb, shb)
            

run_game()