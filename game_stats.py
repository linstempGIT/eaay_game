from os.path import dirname

class GameStats():
    '''跟踪游戏的统计信息'''

    def __init__(self):
        '''初始化统计信息'''

        # 游戏启动状态判断
        self.game_active = False
        self.reset_stats()
        # 在任何情况下都不要重置最高得分
        self.store_hs_path = dirname(__file__) + '/sources/highest.txt'
        # 如果最高分数文件存在则读取，否则重建最高分数文件，分数为0
        self.highest_score = self.read_highest_score()


    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        
        self.score = 0
        self.level = 1

    def read_highest_score(self):
        '''尝试读取最高分数，如果失败则返回0'''

        try:
            with open(self.store_hs_path, 'r', encoding='utf-8') as f:
                return int(f.read())
        except:
                return 0
                
    def store_highest_score(self):
        '''对最高分数进行存储'''

        with open(self.store_hs_path, 'w', encoding='utf-8') as f:
            f.write(str(self.highest_score))