from functools import wraps
from flask import current_app, request, jsonify


def require_api_key(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_app.config.get('REQUIRE_API_KEY'):
            api_key = request.headers.get('X-API-KEY') or request.args.get('api_key')
            if not api_key or api_key != current_app.config.get('BACKEND_API_KEY'):
                return jsonify({'error': 'Unauthorized access'}), 401
        return fn(*args, **kwargs)
    return wrapper
