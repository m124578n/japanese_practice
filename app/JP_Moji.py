from .japanese import moji_type
import random


class Moji:
    def __init__(self, now_moji=None) -> None:
        self.all_type = moji_type
        if now_moji:
            for x in self.all_type:
                if x['type'] == now_moji:
                    self.now_type = x
                    break
        else:
            self.now_type = moji_type[0]['data']
        self.moji = None
    
    def get_moji(self, change):
        if change:
            self.moji = random.choice(self.now_type['data'])
            return self.moji
        else:
            return self.moji
    
    def change_type(self, moji_t):
        for x in self.all_type:
            if x['type'] == moji_t:
                self.now_type = x
                break
