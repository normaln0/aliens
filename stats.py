
from settings import Settings


set = Settings()

class Stats():
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        self.game_active = False
        
        
        with open('higscore.txt', 'r') as file:    
            self.high_score = int(file.readline())


    def reset_stats(self):
        self.guns_left = set.lives
        self.score = 0