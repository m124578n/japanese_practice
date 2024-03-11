from flask import (
    Blueprint, 
    render_template, 
    redirect, 
    url_for, 
    request, 
    make_response,
    jsonify
    )
from .model import TimerUser, TimerRecord, TimerRank
from app.JP_Moji import TimerMoji
from app.dbs import db
import json

bp = Blueprint('timer', __name__)



@bp.route('/timer/', methods=['GET', 'POST'])
def new_timer():
    moji_type = TimerMoji.get_all_type()
    if request.method == 'GET':
        return render_template('timer/index.html', **locals())
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        data = json.loads(data)
        name_t = data.get('name')
        moji_type_t = data.get('moji_type')
        time_t = data.get('time')
        user = TimerUser(name=name_t, time=time_t, moji_type=moji_type_t)
        db.session.add(user)
        db.session.commit()
        data = {'user': user.id}
        response = make_response(jsonify(data), 200)
        return response


@bp.route('/timer/<userid>', methods=['GET', 'POST'])
def timer(userid):
    user = TimerUser.query.filter_by(id=userid).first()
    if not user:
        return redirect(url_for('timer.new_timer'))
    moji_c = TimerMoji(user)

    if request.method == 'GET':
        moji = moji_c.get_moji(change=True)
        record = TimerRecord(
            moji_data=moji['moji'], 
            moji_spell=moji['spell'], 
            timer_user_id=userid
            )
        db.session.add(record)
        db.session.commit()
        return render_template('timer/timer.html', **locals())
    
    if request.method == 'POST':
        data = request.data.decode("utf-8")
        data = json.loads(data)
        answer = data.get('spell', '')
        correct_answer = moji_c.moji['spell']
        correct_answer_data = moji_c.moji['moji']
        is_correct = answer == correct_answer
        record_id = moji_c.moji['id']
        record = TimerRecord.query.filter_by(id=record_id).update({"answer": answer, "is_correct": is_correct})
        db.session.commit()

        moji = moji_c.get_moji(change=True)
        record = TimerRecord(
            moji_data=moji['moji'], 
            moji_spell=moji['spell'], 
            timer_user_id=userid
            )
        db.session.add(record)
        db.session.commit()
        data = {
            'moji': moji['moji']
            }
        return make_response(jsonify(data), 200)
    
@bp.route('/timer/<userid>/records/', methods=['GET'])
def get_all_practice_records(userid):
    records = TimerRecord.query.filter_by(timer_user_id=userid).order_by(TimerRecord.id.desc()).all()
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