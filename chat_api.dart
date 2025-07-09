import 'dart:convert';
import 'package:http/http.dart' as http;

class ChatApiService {
  static const String _apiUrl = 'http://192.168.0.135:5000/gemini/ask';  // 재민아이 IP

  static Future<String> sendMessage(String userMessage) async {
    try {
      final response = await http.post(
        Uri.parse(_apiUrl),
        headers: {"Content-Type": "application/json"},
        body: jsonEncode({"message": userMessage}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['reply'] ?? "응답 없음";
      } else {
        return "AI 서버 오류: ${response.statusCode}";
      }
    } catch (e) {
      return "서버 연결 실패: $e";
    }
  }
}
