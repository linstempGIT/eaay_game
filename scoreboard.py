import pygame.font

class Scoreboard():
    '''显示得分信息'''

    def __init__(self, screen, stats):
        '''初始化显示得分涉及的属性'''

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 显示得分信息时使用的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('Times', 30)

        # 根据传入的stats初始化hight_score和score, level
        # 同时初始化score_image和hight_score_image, level_image
        self.update(stats)

        # 对于不需要在游戏过程中实时更新的元素尽量少在update中初始化


    def prep_score(self):
        '''将得分转换为一幅渲染图像'''

        rounded_score = int(round(self.score, 0))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_hight_score(self):
        '''将最高分数转换为图像'''

        hight_score_str = "{:,}".format(self.hight_score)
        self.hight_score_image = self.font.render(hight_score_str, True,
                                                    self.text_color)
        # 将最高得分放在屏幕顶部
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级转化为图像'''

        self.level_image = self.font.render(str(self.level), True,
                                                self.text_color)
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10


    def update(self, new_stats):
        '''对分数的变动进行重绘'''

        # 重新读取stats
        self.stats = new_stats
        
        # 更新score和hight_score, level
        self.score = self.stats.score
        self.hight_score = self.stats.highest_score
        self.level = new_stats.level

        # 更新得分图像和最高分数图像
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()
        
    def show_score(self):
        '''在屏幕上显示得分和最高得分'''
        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

