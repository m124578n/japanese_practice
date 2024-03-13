from .japanese import moji_type
import random
from .utils import trans_str_to_list


class Moji:
    def __init__(self, user) -> None:
        self.all_type = moji_type
        for x in self.all_type:
            if x['type'] == user.now_moji_type:
                self.now_type = x
                break
        if user.records != []:
            self.moji = {
                'id' : user.records[-1].id,
                'moji' : user.records[-1].moji_data,
                'spell' : trans_str_to_list(user.records[-1].moji_spell),
                }
        else:
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


class TimerMoji:
    def __init__(self, user) -> None:
        self.all_type = moji_type
        for x in self.all_type:
            if x['type'] == user.moji_type:
                self.moji_type = x
                break
        if user.records != []:
            self.moji = {
                'id' : user.records[-1].id,
                'moji' : user.records[-1].moji_data,
                'spell' : trans_str_to_list(user.records[-1].moji_spell),
                }
        else:
            self.moji = None

    def get_moji(self, change):
        if change:
            self.moji = random.choice(self.moji_type['data'])
            return self.moji
        else:
            return self.moji

    @staticmethod
    def get_all_type():
        return moji_type
    