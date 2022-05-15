import pygame
from os.path import dirname
from pygame.sprite import Sprite

dir_name = dirname(__file__)

class Ufo(Sprite):
    '''表示单个ufo类'''

    def __init__(self, ai_settings, screen):
        '''初始化ufo并设置其起始位置'''

        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载ufo图像，并为其创建一个rect对象
        self.image = pygame.image.load(dir_name
        + '/images/ufo.bmp')
        self.rect = self.image.get_rect()

        # 每个ufo最初都在屏幕左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储ufo的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制ufo'''
        self.screen.blit(self.image, self.rect)