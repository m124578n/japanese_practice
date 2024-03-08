# from flask import Flask
# from flask import render_template, redirect, url_for
# from flask import request

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# import sqlalchemy as sa

# import random
# import json

# app = Flask(__name__, static_folder='assets/')
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# class User(db.Model):
#     id = sa.Column(sa.Integer, primary_key=True)
#     now_moji_type = sa.Column(sa.String(30), nullable=False)



# with app.app_context():
#     db.create_all()


# hiragana = [
#     {'moji': 'あ', 'spell': 'a'},
#     {'moji': 'か', 'spell': 'ka'},
#     {'moji': 'さ', 'spell': 'sa'},
#     {'moji': 'た', 'spell': 'ta'},
#     {'moji': 'な', 'spell': 'na'},
#     {'moji': 'は', 'spell': 'ha'},
#     {'moji': 'ま', 'spell': 'ma'},
#     {'moji': 'や', 'spell': 'ya'},
#     {'moji': 'ら', 'spell': 'ra'},
#     {'moji': 'わ', 'spell': 'wa'},
#     {'moji': 'い', 'spell': 'i'},
#     {'moji': 'き', 'spell': 'ki'},
#     {'moji': 'し', 'spell': 'shi'},
#     {'moji': 'ち', 'spell': 'chi'},
#     {'moji': 'に', 'spell': 'ni'},
#     {'moji': 'ひ', 'spell': 'hi'},
#     {'moji': 'み', 'spell': 'mi'},
#     {'moji': 'り', 'spell': 'ri'},
#     {'moji': 'う', 'spell': 'u'},
#     {'moji': 'く', 'spell': 'ku'},
#     {'moji': 'す', 'spell': 'su'},
#     {'moji': 'つ', 'spell': 'tsu'},
#     {'moji': 'ぬ', 'spell': 'nu'},
#     {'moji': 'ふ', 'spell': 'fu'},
#     {'moji': 'む', 'spell': 'mu'},
#     {'moji': 'ゆ', 'spell': 'yu'},
#     {'moji': 'る', 'spell': 'ru'},
#     {'moji': 'ん', 'spell': 'n'},
#     {'moji': 'え', 'spell': 'e'},
#     {'moji': 'け', 'spell': 'ke'},
#     {'moji': 'せ', 'spell': 'se'},
#     {'moji': 'て', 'spell': 'te'},
#     {'moji': 'ね', 'spell': 'ne'},
#     {'moji': 'へ', 'spell': 'he'},
#     {'moji': 'め', 'spell': 'me'},
#     {'moji': 'れ', 'spell': 're'},
#     {'moji': 'お', 'spell': 'o'},
#     {'moji': 'こ', 'spell': 'ko'},
#     {'moji': 'そ', 'spell': 'so'},
#     {'moji': 'と', 'spell': 'to'},
#     {'moji': 'の', 'spell': 'no'},
#     {'moji': 'ほ', 'spell': 'ho'},
#     {'moji': 'も', 'spell': 'mo'},
#     {'moji': 'よ', 'spell': 'yo'},
#     {'moji': 'ろ', 'spell': 'ro'},
#     {'moji': 'を', 'spell': 'o'}
#     ]

# hirataku = [
#     {'moji': 'が', 'spell': 'ga'},
#     {'moji': 'ざ', 'spell': 'za'},
#     {'moji': 'だ', 'spell': 'da'},
#     {'moji': 'ば', 'spell': 'ba'},
#     {'moji': 'ぱ', 'spell': 'pa'},
#     {'moji': 'ぎ', 'spell': 'gi'},
#     {'moji': 'じ', 'spell': 'ji'},
#     {'moji': 'ぢ', 'spell': 'ji'},
#     {'moji': 'び', 'spell': 'bi'},
#     {'moji': 'ぴ', 'spell': 'pi'},
#     {'moji': 'ぐ', 'spell': 'gu'},
#     {'moji': 'ず', 'spell': 'zu'},
#     {'moji': 'づ', 'spell': 'zu'},
#     {'moji': 'ぶ', 'spell': 'bu'},
#     {'moji': 'ぷ', 'spell': 'pu'},
#     {'moji': 'げ', 'spell': 'ge'},
#     {'moji': 'ぜ', 'spell': 'ze'},
#     {'moji': 'で', 'spell': 'de'},
#     {'moji': 'べ', 'spell': 'be'},
#     {'moji': 'ぺ', 'spell': 'pe'},
#     {'moji': 'ご', 'spell': 'go'},
#     {'moji': 'ぞ', 'spell': 'zo'},
#     {'moji': 'ど', 'spell': 'do'},
#     {'moji': 'ぼ', 'spell': 'bo'},
#     {'moji': 'ぽ', 'spell': 'po'}
#     ]

# hirayoonn = [
#     {'moji': 'きゃ', 'spell': 'kya'},
#     {'moji': 'ぎゃ', 'spell': 'gya'},
#     {'moji': 'しゃ', 'spell': 'sha'},
#     {'moji': 'じゃ', 'spell': 'ja'},
#     {'moji': 'ちゃ', 'spell': 'cha'},
#     {'moji': 'にゃ', 'spell': 'nya'},
#     {'moji': 'ひゃ', 'spell': 'hya'},
#     {'moji': 'びゃ', 'spell': 'bya'},
#     {'moji': 'ぴゃ', 'spell': 'pya'},
#     {'moji': 'みゃ', 'spell': 'mya'},
#     {'moji': 'りゃ', 'spell': 'rya'},
#     {'moji': 'きゅ', 'spell': 'kyu'},
#     {'moji': 'ぎゅ', 'spell': 'gyu'},
#     {'moji': 'しゅ', 'spell': 'shu'},
#     {'moji': 'じゅ', 'spell': 'ju'},
#     {'moji': 'ちゅ', 'spell': 'chu'},
#     {'moji': 'にゅ', 'spell': 'nyu'},
#     {'moji': 'ひゅ', 'spell': 'hyu'},
#     {'moji': 'びゅ', 'spell': 'byu'},
#     {'moji': 'ぴゅ', 'spell': 'pyu'},
#     {'moji': 'みゅ', 'spell': 'myu'},
#     {'moji': 'りゅ', 'spell': 'ryu'},
#     {'moji': 'きょ', 'spell': 'kyo'},
#     {'moji': 'ぎょ', 'spell': 'gyo'},
#     {'moji': 'しょ', 'spell': 'sho'},
#     {'moji': 'じょ', 'spell': 'jo'},
#     {'moji': 'ちょ', 'spell': 'cho'},
#     {'moji': 'にょ', 'spell': 'nyo'},
#     {'moji': 'ひょ', 'spell': 'hyo'},
#     {'moji': 'びょ', 'spell': 'byo'},
#     {'moji': 'ぴょ', 'spell': 'pyo'},
#     {'moji': 'みょ', 'spell': 'myo'},
#     {'moji': 'りょ', 'spell': 'ryo'}
#     ]

# katagana = [
#     {'moji': 'ア', 'spell': 'a'},
#     {'moji': 'カ', 'spell': 'ka'},
#     {'moji': 'サ', 'spell': 'sa'},
#     {'moji': 'タ', 'spell': 'ta'},
#     {'moji': 'ナ', 'spell': 'na'},
#     {'moji': 'ハ', 'spell': 'ha'},
#     {'moji': 'マ', 'spell': 'ma'},
#     {'moji': 'ヤ', 'spell': 'ya'},
#     {'moji': 'ラ', 'spell': 'ra'},
#     {'moji': 'ワ', 'spell': 'wa'},
#     {'moji': 'イ', 'spell': 'i'},
#     {'moji': 'キ', 'spell': 'ki'},
#     {'moji': 'シ', 'spell': 'shi'},
#     {'moji': 'チ', 'spell': 'chi'},
#     {'moji': 'ニ', 'spell': 'ni'},
#     {'moji': 'ヒ', 'spell': 'hi'},
#     {'moji': 'ミ', 'spell': 'mi'},
#     {'moji': 'リ', 'spell': 'ri'},
#     {'moji': 'ウ', 'spell': 'u'},
#     {'moji': 'ク', 'spell': 'ku'},
#     {'moji': 'ス', 'spell': 'su'},
#     {'moji': 'ツ', 'spell': 'tsu'},
#     {'moji': 'ヌ', 'spell': 'nu'},
#     {'moji': 'フ', 'spell': 'fu'},
#     {'moji': 'ム', 'spell': 'mu'},
#     {'moji': 'ユ', 'spell': 'yu'},
#     {'moji': 'ル', 'spell': 'ru'},
#     {'moji': 'ン', 'spell': 'n'},
#     {'moji': 'エ', 'spell': 'e'},
#     {'moji': 'ケ', 'spell': 'ke'},
#     {'moji': 'セ', 'spell': 'se'},
#     {'moji': 'テ', 'spell': 'te'},
#     {'moji': 'ネ', 'spell': 'ne'},
#     {'moji': 'ヘ', 'spell': 'he'},
#     {'moji': 'メ', 'spell': 'me'},
#     {'moji': 'レ', 'spell': 're'},
#     {'moji': 'オ', 'spell': 'o'},
#     {'moji': 'コ', 'spell': 'ko'},
#     {'moji': 'ソ', 'spell': 'so'},
#     {'moji': 'ト', 'spell': 'to'},
#     {'moji': 'ノ', 'spell': 'no'},
#     {'moji': 'ホ', 'spell': 'ho'},
#     {'moji': 'モ', 'spell': 'mo'},
#     {'moji': 'ヨ', 'spell': 'yo'},
#     {'moji': 'ロ', 'spell': 'ro'},
#     {'moji': 'ヲ', 'spell': 'o'}
#     ]

# katataku = [
#     {'moji': 'ガ', 'spell': 'ga'},
#     {'moji': 'ザ', 'spell': 'za'},
#     {'moji': 'ダ', 'spell': 'da'},
#     {'moji': 'バ', 'spell': 'ba'},
#     {'moji': 'パ', 'spell': 'pa'},
#     {'moji': 'ギ', 'spell': 'gi'},
#     {'moji': 'ジ', 'spell': 'ji'},
#     {'moji': 'ジ', 'spell': 'ji'},
#     {'moji': 'ビ', 'spell': 'bi'},
#     {'moji': 'ピ', 'spell': 'pi'},
#     {'moji': 'グ', 'spell': 'gu'},
#     {'moji': 'ズ', 'spell': 'zu'},
#     {'moji': 'ズ', 'spell': 'zu'},
#     {'moji': 'ブ', 'spell': 'bu'},
#     {'moji': 'プ', 'spell': 'pu'},
#     {'moji': 'ゲ', 'spell': 'ge'},
#     {'moji': 'ゼ', 'spell': 'ze'},
#     {'moji': 'デ', 'spell': 'de'},
#     {'moji': 'ベ', 'spell': 'be'},
#     {'moji': 'ペ', 'spell': 'pe'},
#     {'moji': 'ゴ', 'spell': 'go'},
#     {'moji': 'ゾ', 'spell': 'zo'},
#     {'moji': 'ド', 'spell': 'do'},
#     {'moji': 'ボ', 'spell': 'bo'},
#     {'moji': 'ポ', 'spell': 'po'}
#     ]

# katayoonn = [
#     {'moji': 'キャ', 'spell': 'kya'},
#     {'moji': 'ギャ', 'spell': 'gya'},
#     {'moji': 'シャ', 'spell': 'sha'},
#     {'moji': 'ジャ', 'spell': 'ja'},
#     {'moji': 'チャ', 'spell': 'cha'},
#     {'moji': 'ニャ', 'spell': 'nya'},
#     {'moji': 'ヒャ', 'spell': 'hya'},
#     {'moji': 'ビャ', 'spell': 'bya'},
#     {'moji': 'ピャ', 'spell': 'pya'},
#     {'moji': 'ミャ', 'spell': 'mya'},
#     {'moji': 'リャ', 'spell': 'rya'},
#     {'moji': 'キュ', 'spell': 'kyu'},
#     {'moji': 'ギュ', 'spell': 'gyu'},
#     {'moji': 'シュ', 'spell': 'shu'},
#     {'moji': 'ジュ', 'spell': 'ju'},
#     {'moji': 'チュ', 'spell': 'chu'},
#     {'moji': 'ニュ', 'spell': 'nyu'},
#     {'moji': 'ヒュ', 'spell': 'hyu'},
#     {'moji': 'ビュ', 'spell': 'byu'},
#     {'moji': 'ピュ', 'spell': 'pyu'},
#     {'moji': 'ミュ', 'spell': 'myu'},
#     {'moji': 'チュ', 'spell': 'ryu'},
#     {'moji': 'キョ', 'spell': 'kyo'},
#     {'moji': 'ギョ', 'spell': 'gyo'},
#     {'moji': 'ショ', 'spell': 'sho'},
#     {'moji': 'ジョ', 'spell': 'jo'},
#     {'moji': 'チョ', 'spell': 'cho'},
#     {'moji': 'ニョ', 'spell': 'nyo'},
#     {'moji': 'ヒョ', 'spell': 'hyo'},
#     {'moji': 'ビョ', 'spell': 'byo'},
#     {'moji': 'ピョ', 'spell': 'pyo'},
#     {'moji': 'ミョ', 'spell': 'myo'},
#     {'moji': 'リョ', 'spell': 'ryo'}
#     ]

# moji_type = [
#     {'type' : 'hiragana', 'data' : hiragana, 'name': '平假名'}, 
#     {'type' : 'hirataku', 'data' : hirataku, 'name': '平假名濁音'},
#     {'type' : 'hirayoonn', 'data' : hirayoonn, 'name': '平假名拗音'}, 
#     {'type' : 'katagana', 'data' : katagana, 'name': '片假名'}, 
#     {'type' : 'katataku', 'data' : katataku, 'name': '片假名濁音'},
#     {'type' : 'katayoonn', 'data' : katayoonn, 'name': '片假名拗音'},
#     {'type' : 'allhira', 'data' : hiragana + hirataku + hirayoonn, 'name': '平假名全'},
#     {'type' : 'allkata', 'data' : katagana + katataku + katayoonn, 'name': '片假名全'},
#     {'type' : 'all', 'data' : hiragana + hirataku + hirayoonn + katagana + katataku + katayoonn, 'name': '全部'}
#     ]

# @app.route('/test_index/<name>', methods=['GET', 'POST'])
# def test_index(name):
#     if request.method == 'GET':
#         args = request.args.get('args')
#         return render_template('test_index.html', **locals())
#     elif request.method == 'POST':
#         firstname = request.values.get('firstname', '')
#         lastname = request.values.get('lastname', '')
#         return render_template('test_index.html', **locals())
#     else:
#         return 'method not allow'


# class Moji:
#     def __init__(self) -> None:
#         self.all_type = moji_type
#         self.now_type = self.all_type[0]
#         self.jpa_list = self.all_type[0]['data']
#         self.moji = None
    
#     def get_moji(self, change):
#         if change:
#             self.moji = random.choice(self.jpa_list)
#             return self.moji
#         else:
#             return self.moji
    
#     def change_type(self, moji_t):
#         for x in self.all_type:
#             if x['type'] == moji_t:
#                 self.now_type = x
#                 self.jpa_list = x['data']
#                 break


# moji_c = Moji()


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     moji_type = moji_c.all_type
#     now_type = moji_c.now_type
#     if request.method == 'GET':
#         image_name = 'all001.webp'
#         moji = moji_c.get_moji(change=True)
#         return render_template('index.html', **locals())
    
#     if request.method == 'POST':
#         answer = request.values.get('spell', '')
#         moji = moji_c.get_moji(change=False)
#         if not moji:
#             return redirect(url_for('index'))
#         correct_answer = moji['spell']
#         if answer == correct_answer:
#             message = '答對'
#         else:
#             message = f'答錯，正確答案為 {correct_answer}'
        
#         return render_template('index.html', **locals())


# @app.route('/change', methods=['POST'])
# def change():
#     data = request.data.decode("utf-8")
#     data = json.loads(data)
#     moji_t = data.get('type', 'hiragana')
#     moji_c.change_type(moji_t)
#     return 'OK'
