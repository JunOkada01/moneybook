from flask import Flask
from flask_cors import CORS
from .main import main as main_blueprint
from .config import DevelopmentConfig  # 相対インポートに変更

def create_app():
    app = Flask(__name__)
    
    # CORS設定
    CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    
    # Configuration - from_objectの引数を修正
    app.config.from_object(DevelopmentConfig)  # 直接クラスを指定
    
    # Register Blueprints
    app.register_blueprint(main_blueprint)
    
    return app