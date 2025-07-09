# routes/gemini_routes.py
from flask import Blueprint, request, jsonify  # ✅ Flask용으로 수정
from ml.gemini_client import ask_gemini  # Gemini 함수 import

# Flask용 Blueprint 생성
gemini_bp = Blueprint('gemini', __name__)

# POST 요청 처리
@gemini_bp.route("/gemini/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "message 필드는 필수입니다."}), 400

    reply = ask_gemini(message)
    return jsonify({"reply": reply})
