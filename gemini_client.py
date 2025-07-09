# ml/gemini_client.py
from google.oauth2 import service_account
import vertexai
from vertexai.language_models import ChatModel

# ✅ 서비스 계정 키 경로 설정
KEY_PATH = "C:/Users/302-28/Downloads/gemini-chat-test-465401-63bca77895c0.json"

# ✅ 서비스 계정 자격 증명 객체 생성
creds = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# ✅ Vertex AI 초기화
vertexai.init(
    project="gemini-chat-test",
    location="us-central1",
    credentials=creds,
)

# ✅ 모델 준비 (chat-bison 또는 gemini-pro 등)
try:
    chat_model = ChatModel.from_pretrained("chat-bison")  # 또는 "gemini-pro"
except Exception as e:
    print(f"[ERROR] 모델 로딩 실패: {e}")
    chat_model = None  # 추후 함수에서 None 체크

# ✅ 질문을 던지고 응답을 받는 함수
def ask_gemini(prompt: str) -> str:
    if chat_model is None:
        return "Gemini 모델 초기화에 실패했습니다. 관리자에게 문의하세요."

    try:
        chat = chat_model.start_chat()
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        print(f"[ERROR] Gemini 호출 실패: {e}")
        return "Gemini 응답 중 오류가 발생했습니다."

