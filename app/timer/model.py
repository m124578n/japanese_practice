from app.dbs import db
import sqlalchemy as sa
from datetime import datetime


class TimerUser(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(30), nullable=False)
    time = sa.Column(sa.Integer, nullable=False)
    moji_type = sa.Column(sa.String(30), nullable=False)
    records = db.relationship('TimerRecord', backref='records', lazy=True)
    rank = db.relationship('TimerRank', backref='rank', lazy=True)


class TimerRecord(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    moji_data = sa.Column(sa.String(5), nullable=False)
    moji_spell = sa.Column(sa.String(5), nullable=False)
    answer = sa.Column(sa.String(5), nullable=True)
    is_correct = sa.Column(sa.Boolean, nullable=True)
    timer_user_id = sa.Column(sa.Integer, sa.ForeignKey('timer_user.id'), nullable=False)


class TimerRank(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    timer_user_id = sa.Column(sa.Integer, sa.ForeignKey('timer_user.id'), nullable=False)
    WPM = sa.Column(sa.Integer, nullable=False)
    amount = sa.Column(sa.Integer, nullable=False)
    accurary = sa.Column(sa.Float, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)

    