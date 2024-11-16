from log import db
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    referral_code = db.Column(db.String(10), unique=True, nullable=False, default=lambda: str(uuid.uuid4())[:10])
    referrer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    referees = db.relationship('User', backref=db.backref('referrer', remote_side=[id]), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

