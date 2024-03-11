from app.dbs import db
import sqlalchemy as sa


class User(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    now_moji_type = sa.Column(sa.String(30), nullable=False)
    records = db.relationship('Record', backref='records', lazy=True)


class Record(db.Model):
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    moji_data = sa.Column(sa.String(5), nullable=False)
    moji_spell = sa.Column(sa.String(5), nullable=False)
    answer = sa.Column(sa.String(5), nullable=True)
    is_correct = sa.Column(sa.Boolean, nullable=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)

