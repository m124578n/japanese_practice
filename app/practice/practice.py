from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    url_for, 
    request, 
    make_response,
    jsonify
    )
from .model import User, Record
from app.JP_Moji import Moji
from app.dbs import db
from app.utils import trans_list_to_str, clean_the_input_data
import json

bp = Blueprint('practice', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@bp.route('/practice/', methods=['POST'])
def new_practice():
    user = User(now_moji_type='hiragana')
    db.session.add(user)
    db.session.commit()

    data = {"user" : user.id}
    response = make_response(jsonify(data), 200)
    return response


@bp.route('/practice/<userid>', methods=['GET', 'POST'])
def practice(userid):
    user = User.query.filter_by(id=userid).first()
    if not user:
        return redirect(url_for('practice.index'))
    
    moji_c = Moji(user)
    moji_type = moji_c.all_type
    now_type = moji_c.now_type
    
    if request.method == 'GET':
        moji = moji_c.get_moji(change=True)
        record = Record(
            moji_data=moji['moji'], 
            moji_spell=trans_list_to_str(moji['spell']), 
            user_id=userid
            )
        db.session.add(record)
        db.session.commit()
        return render_template('practice/index.html', **locals())
    
    if request.method == 'POST':
        answer = request.values.get('spell', '')
        answer = clean_the_input_data(answer)
        correct_answer = moji_c.moji['spell']
        correct_answer_data = moji_c.moji['moji']
        is_correct = answer in correct_answer
        if is_correct:
            message = f'答對，{correct_answer_data} 就是 {trans_list_to_str(correct_answer)}'
        else:
            message = f'答錯，{correct_answer_data} 正確答案為 {trans_list_to_str(correct_answer)}'
        
        record_id = moji_c.moji['id']
        record = Record.query.filter_by(id=record_id).update({"answer": answer, "is_correct": is_correct})
        db.session.commit()
        moji = moji_c.get_moji(change=True)
        record = Record(
            moji_data=moji['moji'], 
            moji_spell=trans_list_to_str(moji['spell']),
            user_id=userid
            )
        db.session.add(record)
        db.session.commit()
        return render_template('practice/index.html', **locals())


@bp.route('/practice/<userid>/records/', methods=['GET'])
def get_all_practice_records(userid):
    records = Record.query.filter_by(user_id=userid).order_by(Record.id.desc()).all()
    all_results = []
    count = len(records)
    for record in records:
        if count == len(records):
            count -= 1
            continue
        temp = {}
        temp['count'] = count
        temp['moji_data'] = record.moji_data
        temp['moji_spell'] = record.moji_spell
        temp['answer'] = record.answer
        temp['is_correct'] = record.is_correct
        all_results.append(temp)
        count -= 1

    data = {"records" : all_results}
    response = make_response(jsonify(data), 200)
    return response


@bp.route('/moji/change/<userid>', methods=['POST'])
def change(userid):
    data = request.data.decode("utf-8")
    data = json.loads(data)
    moji_t = data.get('type', 'hiragana')
    user = User.query.filter_by(id=userid).update({'now_moji_type': moji_t})
    db.session.commit()

    data = {'user': userid}
    response = make_response(jsonify(data), 200)
    return response


