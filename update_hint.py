import requests
import base64
import json
import os
from datetime import datetime, timedelta
from google.genai import Client

def get_ai_hints(answer_word):
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"level1": "API 키가 설정되지 않았습니다.", "level2": "..."}

    client = Client(api_key=api_key)

    prompt = f"""
[시스템 설정]
당신은 '단어 유추 게임'의 지능형 힌트 출제자입니다. 사용자가 정답 단어를 직접 보지 않고도 단계별로 추론할 수 있도록 매력적인 수수께끼를 만들어야 합니다.

[입력 단어]
정답: "{answer_word}"

[출력 규칙]
1. 정답 단어를 힌트 내용에 절대 직접적으로 언급하지 마세요.
2. 아래의 구조에 맞춰 한국어로 작성하세요.
3. 반드시 JSON 형식으로만 응답하세요.
4. 반드시 30자 이내로 작성하세요.

[힌트 단계별 가이드라인]
level1 (추상적): 단어의 본질, 철학적 의미, 혹은 그것이 세상에 없다면 어떨지에 대한 은유적인 묘사. (가장 어려움)
level2 (언어적): 이 단어가 포함된 아주 유명한 속담, 관용구, 노래 가사, 영화 제목 등을 활용한 결정적 단서.

[응답 형식]
{{
"level1": "...",
"level2": "..."
}}
"""

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_text)
    except Exception as e:
        print(f"AI 생성 중 오류: {e}")
        return {"level1": "AI 힌트를 생성할 수 없습니다.", "level2": "서버 통신 오류"}

                
def get_hint():
    try:
        # 1. 오늘 정보 가져오기
        today_res = requests.get("https://semantle-ko.newsjel.ly/today", timeout=10)
        today_data = today_res.json()
        p_num = today_data['answer_id']
        
        # 2. 정답 데이터 가져오기
        score_res = requests.get(f"https://semantle-ko.newsjel.ly/top_scores/{p_num}", timeout=10)
        score_data = score_res.json()
        ans = score_data['key'] # 정답 단어 추출

        hints = get_ai_hints(ans)

        # 3. 암호화 (Base64)
        encoded_ans = base64.b64encode(ans.encode('utf-8')).decode('utf-8')
        
        # 4. 저장할 데이터 구성 (한국 시간 기준)
        kst_now = datetime.utcnow() + timedelta(hours=9)
        result = {
            "ans": encoded_ans,
            "updated": kst_now.strftime("%Y-%m-%d %H:%M:%S"),
            "level1": hints.get('level1'),
            "level2": hints.get('level2')
        }

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
            
        print(f"성공: {ans} 정답 추출 및 AI 힌트 생성 완료")
    except Exception as e:
        print(f"오류 발생: {e}")
        exit(1)

if __name__ == "__main__":
    get_hint()
