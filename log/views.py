from .models import User
from flask import request, jsonify
from log import app, db


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    required_fields = ['email', 'name', 'mobile', 'city', 'password']
    
    # Validate mandatory fields
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400
    
    # Check for referral code validity
    referrer = None
    if data.get('referral_code'):
        referrer = User.query.filter_by(referral_code=data['referral_code']).first()
        if not referrer:
            return jsonify({'error': 'Invalid referral code'}), 400
    # Create the new user
    new_user = User(
        email=data['email'],
        name=data['name'],
        mobile=data['mobile'],
        city=data['city'],
        referrer=referrer
    )
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully', 'referral_code': new_user.referral_code}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    # Validate input
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify({'user_id': user.id, 'email': user.email}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401
