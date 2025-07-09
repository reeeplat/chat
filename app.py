# C:\Users\302-28\25_07_08_backend\app.py 또는 C:\Users\sptzk\Desktop\backend\app.py

from flask import Flask
from flask_cors import CORS
from models import db
from config import Config
from routes.auth_routes import auth_bp
from routes.predict_routes import predict_bp  # ✅ 예측 라우트
from routes.gemini_routes import gemini_bp  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)             # 모든 Origin 허용
    db.init_app(app)      # DB 초기화

    # ✅ 라우트 등록
    app.register_blueprint(auth_bp, url_prefix='/auth')   # ex) /auth/login
    app.register_blueprint(predict_bp) 
    app.register_blueprint(gemini_bp, url_prefix="")                   # ex) /predict 등 (prefix 없음)

    # ✅ 테스트용 루트 페이지
    @app.route('/')
    def home():
        return '✅ Flask 서버 정상 작동 중'

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        print("✅ 데이터베이스 테이블 초기화 완료")

        

    # ✅ 0.0.0.0으로 외부 접속 가능하게 설정
    app.run(debug=True, host='0.0.0.0', port=5000)

