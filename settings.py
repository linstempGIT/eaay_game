from os.path import dirname
from PIL import Image

class Settings():
    '''存储游戏所有设置的类'''

    # 在类变量中存储图片文件目录
    images_dir = dirname(__file__) + '/sources/images/'

    def __init__(self) -> None:
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_image_path = Settings.images_dir + 'ship.bmp'
        with Image.open(self.ship_image_path) as ship_image:
            self.ship_size = ship_image.size
        self.ship_width = self.ship_size[0]
        self.ship_height = self.ship_size[1]
        self.ship_centerx = self.screen_width // 2
        self.ship_bottom = self.screen_height // 4 * 3
        self.ship_top = self.ship_bottom + self.ship_height
        self.ship_y_speed = 1.5
        self.ship_x_speed = 1.5
        self.ship_fire_wait_time = 100
        self.ship_total_bullets = 300
        self.ship_limit = 3
        self.ship_fire_prepare = 100

        # ufo设置
        self.ufo_image_path = Settings.images_dir + 'ufo.bmp'
        with Image.open(self.ufo_image_path) as ufo_image:
                self.ufo_size = ufo_image.size
        self.ufo_width = self.ufo_size[0]
        self.ufo_height = self.ufo_size[1]
        # self.ufo_speed = 1    为可变量，需动态初始化
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示左移
        self.fleet_direction = 1
        # self.ufo_points = 1    为可变量，需动态初始化
        # 加快游戏节奏的速度
        self.speed_scale = 1.2
        # ufo点数的提高速度
        self.score_scale = 2.0

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # 动态初始化可变量
        self.reset()

    def increase_dificult(self):
        '''提高速度设置和ufo点数'''

        self.ufo_speed *= self.speed_scale
        self.ufo_points = int(self.ufo_points * self.score_scale)

    def reset(self):
        '''对settings直接的改变量，在restart游戏时需要重置'''

        self.ufo_speed = 1
        self.ufo_points = 1
