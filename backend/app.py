import os
import sys
from flask import Flask
from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from routes.platform_routes import bp as platform_bp
from routes.train_routes import bp as train_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    if app.config['REQUIRE_API_KEY'] and not app.config['BACKEND_API_KEY']:
        raise RuntimeError('BACKEND_API_KEY is required when REQUIRE_API_KEY is enabled')

    CORS(app)
    
    app.register_blueprint(platform_bp)
    app.register_blueprint(train_bp)
    
    @app.route('/health')
    def health():
        return {"status": "ok"}, 200
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
