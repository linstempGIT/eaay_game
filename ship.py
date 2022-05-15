import pygame
from os.path import dirname
from bullet import Bullet
from pygame.sprite import Group

dir_name = dirname(__file__)

class Ship():

    def __init__(self, screen, ai_settings) -> None:
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图形并获取其外接矩形
        self.image = pygame.image.load(dir_name
        +'/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.screen_rect.centery * 3) // 2

        # 在飞船的属性center, bottom中存储小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #飞船携带的子弹总数
        self.total_bullets = self.ai_settings.ship_total_bullets
        # 创建一个用于存储子弹的编组
        self.bullets = Group()
        # 开火标志
        self.fire_button = False
        # 开火准备
        self.fire_prepare = 100

    def fire(self):
        self.fire_prepare += 1
        if self.fire_button == True and\
        self.fire_prepare >= self.ai_settings.ship_fire_wait_time and\
        self.total_bullets > 0:
            # 创建一个子弹, 并将其加入到编组bullets中
            new_bullet = Bullet(self.screen, self.ai_settings, self)
            self.bullets.add(new_bullet)
            self.total_bullets -= 1
            self.fire_prepare = 0

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_x_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_x_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_y_speed
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_y_speed

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):

        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)


