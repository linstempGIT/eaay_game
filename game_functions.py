import sys
import pygame
from ufo import Ufo
from time import sleep

def check_keydowm_events(event, ai_settings, stats, screen, ship, ufos):
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
        if stats.game_active == False:
            # 当游戏处于非激活时，按下空格开始
            pygame.mouse.set_visible(False)
            restart(ai_settings, stats, screen, ship, ufos)
        else:
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

def check_play_button(ai_settings, screen, stats, play_button,
                        ship, ufos, mouse_x, mouse_y):

    '''在玩家点击play时开始游戏'''

    button_ckicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_ckicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重新开始游戏
        restart(ai_settings, stats, screen, ship, ufos)


def check_events(ai_settings, screen, stats, play_button, ship, ufos):
    '''响应按键和鼠标事件'''

    # 监视事件, 如果退出则关闭窗口循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, ai_settings, stats, screen, ship, ufos)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button,
                                ship, ufos, mouse_x, mouse_y)

def update_screen(ai_settings, stats, screen, ship, ufos, play_button):
    '''更新屏幕上的图像, 并切换到新屏幕'''

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

    # 每次循环显示剩余可用飞船
    print_remain_ship(screen, stats)

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        gameover_score(stats, screen)
        play_button.draw_button()
    
    # 在屏幕上更新screen(surface对象)内容
    pygame.display.flip()

def delete_bullets(ship):
    '''删除飞出屏幕外的子弹'''

    for bullet in ship.bullets.copy():
        if bullet.rect.bottom <= 0:
            ship.bullets.remove(bullet)

def update_bullets(ship):
    '''更新子弹位置，并删除已消失的子弹'''

    ship.bullets.update()
    delete_bullets(ship)


def process_collision(ai_settings, stats, screen, ship, ufos):
    '''对子弹的击中效果进行功能实现，同时对ufo舰队进行重生''' 
    '''对飞船碰撞ufo进行功能实现，'''

    # 检查是否有子弹击中ufo
    # 如果击中，就删除相应的子弹和ufo
    collisions = pygame.sprite.\
        groupcollide(ship.bullets,ufos, True, True)

     # 游戏击中ufo得分
    stats.score += len(collisions)

    # 如果所有飞船被击中
    if len(ufos) == 0:
        # 删除现有的子弹，并对ufos重生
        # ship.bullets.empty()
        create_fleet(ai_settings, screen, ufos)

    # 检测ufo和飞船是否碰撞
    if pygame.sprite.spritecollideany(ship, ufos):
        if stats.ships_left > 0:
            # 如果碰撞且飞船数大于零开始下一艘飞船
            restart(ai_settings, stats, screen, ship, ufos)
        else:
            # 游戏结束
            stats.game_active = False
            pygame.mouse.set_visible(True)

def update_ship(ship):
    '''更新飞船位置，并实现开火功能'''

    ship.fire()
    ship.update()

def print_remain_bullets(screen, ship):
    '''显示飞船子弹的剩余数量'''

    font = pygame.font.SysFont('Times', 10)
    screen.blit(font.render(str(ship.total_bullets),
    True, [255, 0, 0]), [5, 5])

def print_remain_ship(screen, stats):
    '''显示剩余可用的飞船'''
    
    font = pygame.font.SysFont('Times', 10)
    screen.blit(font.render(str(stats.ships_left),
    True, [255, 0, 0]), [1185, 5])

def get_number_ufos_x(ai_settings):
    '''计算每行能容纳下多少个ufo'''

    available_space_x = ai_settings.screen_width - 2 * ai_settings.ufo_width
    number_ufos_x = int(available_space_x / (2 *ai_settings.ufo_width))
    return number_ufos_x

def get_number_rows(ai_settings):
    '''计算屏幕可容纳多少行ufo舰队'''

    available_space_y = (ai_settings.ship_top - (3 * ai_settings.ufo_height)
                             - ai_settings.ship_height)
    number_rows = int(available_space_y / (4 * ai_settings.ufo_height))
    return number_rows

def create_ufo(ai_settings, screen, ufos, ufo_number, row_number):
    '''创建一个ufo并将其放入行编组ufos'''

    ufo = Ufo(ai_settings, screen)
    ufo_width = ufo.rect.width
    ufo.x = ufo_width + 2 * ufo_width * ufo_number
    ufo.rect.x = ufo.x
    ufo.rect.y = ufo.rect.height + 4 * ufo.rect.height * row_number
    ufos.add(ufo)

def create_fleet(ai_settings, screen, ufos):
    '''创建ufo舰队'''

    # creat_fleet只对外部已存在的Goup进行重新编排
    # 不改变外部变量对group的指向

    number_ufos_x = get_number_ufos_x(ai_settings)
    number_rows = get_number_rows(ai_settings)

    # 创建第一行ufo舰队
    for row_number in range(number_rows):
        for ufo_number in range(number_ufos_x):
            #  创建第一个ufo并将其加入当前行
            create_ufo(ai_settings, screen, ufos, ufo_number, row_number)

def check_fleet_edges(ai_settings, ufos):
    '''有ufo到达边缘时采取相应的措施'''

    for ufo in ufos.sprites():
        if ufo.check_edges():
            change_fleet_direction(ai_settings, ufos)
            break
    
def change_fleet_direction(ai_settings, ufos):
    '''将ufo舰队向下移，并改变它们的方向'''

    for ufo in ufos.sprites():
        ufo.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_ufos(ai_settings, ufos):
    '''更新ufos中所有ufo的位置'''

    check_fleet_edges(ai_settings, ufos)
    ufos.update()

def check_ufos_bottom(ai_settings, stats, screen, ship, ufos):
    '''检查是否有ufo到达屏幕底端'''
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            if stats.ships_left > 0:
                restart(ai_settings, stats, screen, ship, ufos)
                break
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
                break

def flash_screen(screen):
    '''该函数对屏幕暂时黑屏'''

    screen.fill((0, 0, 0))
    pygame.display.flip()
    sleep(0.5)

def gameover_score(stats, screen):
    '''游戏结束打印结算分数'''

    font = pygame.font.SysFont('Times', 30)
    x = 600 - 15 * len(str(stats.score))
    screen.blit(font.render(str(stats.score),
    True, [255, 0, 0]), [x, 300])

def restart(ai_settings, stats, screen, ship, ufos):
    '''如果激活状态为假重开游戏，否则启用下一艘飞船'''

    # 启用下一艘飞船
    if stats.game_active:
        # 屏幕暂时黑屏
        flash_screen(screen)
        # 将ship_left减1
        stats.ships_left -= 1
        # 清空ufos，创建一群新的ufo舰队
        ufos.empty()
        create_fleet(ai_settings, screen, ufos)
        # 将飞船重置
        ship.reset_ship(True)# 创建新ufo舰队，重置飞船
    #重开游戏
    else:    
        ufos.empty()
        create_fleet(ai_settings, screen, ufos)
        ship.reset_ship(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

    
