import pygame.font

class Shipboard():
    '''显示飞船相关信息'''

    def __init__(self, screen, ship):
        '''初始化显示飞船相关信息的属性'''

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 显示飞船信息时使用的字体
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont('Times', 30)

        # left_bullets和left_ships是可变元素，使用动态初始化
        self.update(ship)

        # 对于不需要及时更新的元素应尽量静态初始化

    def prep_left_bullets(self):
        '''将飞船剩余子弹数转换为图像'''

        left_bullets_str = str(self.left_bullets)
        self.left_bullets_image = self.font.render(left_bullets_str, True,
                                                        self.text_color)
        # 将剩余子弹数显示在左上角
        self.left_bullets_rect = self.left_bullets_image.get_rect()
        self.left_bullets_rect.left = self.screen_rect.left + 20
        self.left_bullets_rect.top = 20

    def prep_left_ships(self):
        '''将飞船剩余备用飞船数转换为图像'''

        left_ships_str = str(self.left_ships)
        self.left_ships_image = self.font.render(left_ships_str, True, self.text_color)

        # 将剩余飞船数放在子弹数下方
        self.left_ships_rect = self.left_ships_image.get_rect()
        self.left_ships_rect.left = self.screen_rect.left + 20
        self.left_ships_rect.top = self.left_bullets_rect.bottom + 10

    def update(self, new_ship):
        '''对飞船的变动信息进行重新读取'''

        # 重新读取飞船
        self.ship = new_ship

        # 更新left_bullets和left_ships
        self.left_bullets = self.ship.total_bullets
        self.left_ships = self.ship.remain_ships

        # 更新子弹数图和剩余飞船数图
        self.prep_left_bullets()
        self.prep_left_ships()

    def show_ship_infos(self):
        '''在屏幕上显示子弹数和剩余飞船数'''

        self.screen.blit(self.left_bullets_image, self.left_bullets_rect)
        self.screen.blit(self.left_ships_image, self.left_ships_rect)
