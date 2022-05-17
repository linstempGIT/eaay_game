import pygame
from os.path import dirname
from pygame.sprite import Sprite

dir_name = dirname(__file__) + '/sources/images/'

class Ufo(Sprite):
    '''表示单个ufo类'''

    def __init__(self, screen, ai_settings):
        '''初始化ufo并设置其起始位置'''

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载ufo图像，并为其创建一个rect对象
        self.image = pygame.image.load(dir_name + 'ufo.bmp')
        self.rect = self.image.get_rect()

        # 每个ufo最初都在屏幕左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储ufo的准确位置
        self.x = float(self.rect.x)

    def check_edges(self):
        '''如果ufo在屏幕边缘，返回True'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        '''向右移动外星人'''
        self.x += (self.ai_settings.ufo_speed *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        '''在指定位置绘制ufo'''
        self.screen.blit(self.image, self.rect)