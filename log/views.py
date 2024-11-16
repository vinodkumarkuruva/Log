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
    
    # Check for email uniqueness
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'Message': 'Email already exists try with Different One'}), 400

    # Check for mobile number uniqueness
    if User.query.filter_by(mobile=data['mobile']).first():
        return jsonify({'error': 'Mobile number already exists try with Different One'}), 400
    
    # Check for Password uniqueness
    if User.query.filter_by(mobile=data['password']).first():
        return jsonify({'error': 'Password already exists try with Different One'}), 400


    # Check for referral code validity (if provided)
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
    new_user.set_password(data['password'])  # Ensure passwords are hashed securely
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



@app.route('/referrals/user/<int:user_id>', methods=['GET'])
def get_user_and_referrals(user_id):
    # Retrieve the user by ID
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Prepare user details and their referrals
    user_details = {
        'name': user.name,
        'email': user.email,
        'mobile': user.mobile,
        'referral_code': user.referral_code,
        'registered_at': user.registered_at.strftime('%Y-%m-%d %H:%M:%S')
    }

    referrals = [
        {
            'id': referee.id,
            'name': referee.name,
            'email': referee.email,
            'registered_at': referee.registered_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for referee in user.referees
    ]

    return jsonify({
        'user': user_details,
        'referrals': referrals
    }), 200