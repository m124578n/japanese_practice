from flask import Blueprint, render_template, redirect, url_for, request
from .model import User, Record
from app.JP_Moji import Moji
from app.dbs import db
import json

bp = Blueprint('user', __name__)


@bp.route('/', methods=['GET', 'POST'])
def new_user():
    user = User(now_moji_type='hiragana', active=False)
    db.session.add(user)
    db.session.commit()    
    return redirect(url_for('user.user_index', userid=user.id))



@bp.route('/moji/<userid>', methods=['GET', 'POST'])
def user_index(userid):
    user = User.query.filter_by(id=userid).first()
    user = User.query.filter_by(id=userid).update({'active': True})
    db.session.commit()
    user = User.query.filter_by(id=userid).first()
    
    if not user:
        return redirect(url_for('user.new_user'))
    if not user.active:
        return redirect(url_for('user.new_user'))
    
    moji_c = Moji(user.now_moji_type)
    moji_type = moji_c.all_type
    now_type = moji_c.now_type
    
    if request.method == 'GET':
        moji = moji_c.get_moji(change=True)
        record = Record(moji_data=moji['moji'] , moji_spell=moji['spell'], user_id=user.id)
        db.session.add(record)
        db.session.commit()
        return render_template('user/index.html', **locals())
    
    if request.method == 'POST':
        answer = request.values.get('spell', '')
        record = Record.query.filter_by(user_id=user.id).order_by(Record.id.desc()).first()
        if not record:
            return redirect(url_for('user.user_index', userid=user.id))
        correct_answer = record.moji_spell
        correct_answer_data = record.moji_data
        if answer == correct_answer:
            message = f'答對，{correct_answer_data} 就是 {correct_answer}'
        else:
            message = f'答錯，{correct_answer_data} 正確答案為 {correct_answer}'
        
        moji = moji_c.get_moji(change=True)
        record = Record(moji_data=moji['moji'] , moji_spell=moji['spell'], user_id=user.id)
        db.session.add(record)
        db.session.commit()
        return render_template('user/index.html', **locals())


@bp.route('/moji/change/<userid>', methods=['POST'])
def change(userid):
    data = request.data.decode("utf-8")
    data = json.loads(data)
    moji_t = data.get('type', 'hiragana')
    user = User.query.filter_by(id=userid).update({'now_moji_type': moji_t})
    db.session.commit()
    return 'OK'