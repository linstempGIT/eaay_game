class Settings():
    '''存储游戏所有设置的类'''

    def __init__(self) -> None:
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_y_speed = 1.5
        self.ship_x_speed = 1.5
        self.ship_fire_wait_time = 100
        self.ship_total_bullets = 300

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
