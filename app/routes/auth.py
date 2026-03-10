from flask import Blueprint, jsonify, request

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400

    # Stub: always return a token for demo
    return jsonify({
        'token': 'admin-demo-token',
        'user': {'email': email, 'role': 'admin'},
    })


@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logged out'})
