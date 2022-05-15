import sys
import pygame
from ufo import Ufo

def check_keydowm_events(event, ship):
    '''响应按下按键'''

    global ship_fire_define

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        ship.fire_button = True  
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    '''响应松开按键'''

    global ship_fire_define

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_SPACE:
        ship.fire_button = False

def check_events(ship):
    '''响应按键和鼠标事件'''

    # 监视事件, 如果退出则关闭窗口循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, ufos):
    '''更新屏幕上的图像, 并切换到新屏幕'''

    # 每次循环将飞出屏幕外的子弹删除
    delete_bullets(ship)

    # 每次循环时都重绘screen
    screen.fill(ai_settings.bg_color)
    
    # 每次循环进行子弹重绘
    for bullet in ship.bullets.sprites():
        bullet.draw_bullet()

    # 每次循环进行飞船重绘
    ship.blitme()

    # 每次循环进行ufos重绘
    ufos.draw(screen)

    # 每次循环显示剩余子弹数量
    print_remain_bullets(screen, ship)

    # 在屏幕上更新screen(surface对象)内容
    pygame.display.flip()

def delete_bullets(ship):
    '''删除飞出屏幕外的子弹'''

    for bullet in ship.bullets.copy():
        if bullet.rect.bottom <= 0:
            ship.bullets.remove(bullet)

def print_remain_bullets(screen, ship):
    '''显示飞船子弹的剩余数量'''

    font = pygame.font.SysFont('Times', 10)
    screen.blit(font.render(str(ship.total_bullets),
    True, [255, 0, 0]), [5, 5])
    
def creat_fleet(ai_settings, screen, ufos):
    '''创建ufo舰队'''

    number_ufos_x = 8

    # 创建第一行ufo舰队
    for ufo_number in range(number_ufos_x):
        #  创建第一个ufo并将其加入当前行
        ufo = Ufo(ai_settings, screen)
        ufo.x = (2 * ufo_number + 1) * 64
        ufo.rect.x = ufo.x
        ufos.add(ufo)