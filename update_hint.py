import requests
import base64
import json
from datetime import datetime, timedelta

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

        # 3. 암호화 (Base64)
        encoded_ans = base64.b64encode(ans.encode('utf-8')).decode('utf-8')
        
        # 4. 저장할 데이터 구성 (한국 시간 기준)
        kst_now = datetime.utcnow() + timedelta(hours=9)
        result = {
            "ans": encoded_ans,
            "updated": kst_now.strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
            
        print(f"성공: {ans} 추출 완료")
    except Exception as e:
        print(f"오류 발생: {e}")
        exit(1)

if __name__ == "__main__":
    get_hint()
