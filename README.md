# 💡 꼬맨틀 힌트 도우미 `v0.2`

[업데이트_일지📃](https://github.com/dragon0622/semantle-ko-hint/wiki/%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8-%EC%9D%BC%EC%A7%80)

## 🔗 사이트 주소
[https://dragon0622.github.io/semantle-ko-hint/](https://dragon0622.github.io/semantle-ko-hint/)

매일 업데이트되는 **꼬맨틀(Semantle-ko)**의 정답을 기반으로 글자 수, 초성 등의 단계별 힌트를 제공하는 웹 서비스입니다. 
관리자의 수동 조작 없이 **GitHub Actions를 통해 매일 새벽 01:00(KST)에 자동으로 최신 힌트를 갱신**합니다.

## 🚀 주요 기능

- **자동 데이터 수집**: GitHub Actions가 매일 새벽 정해진 시간에 꼬맨틀에서 데이터를 추출합니다.
- **단계별 힌트 제공**: (변경-예정)
  - 힌트 1: 정답의 총 글자 수
  - 힌트 2: 정답의 초성 확인
  - 힌트 3: 길이 힌트 및 유도 문구
- **정답 보안**: 정답 데이터를 `Base64`로 암호화하여 저장소 내 파일(`data.json`)을 열어보아도 정답이 즉시 노출되지 않도록 보호합니다.
- **날짜 동기화**: 오늘 날짜의 힌트가 준비되지 않은 경우 사용자에게 알림을 표시합니다.

## 🛠 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS)
- **Backend Automation**: Python (Requests)
- **CI/CD**: GitHub Actions
- **Data Storage**: JSON (with Base64 Encoding)

## 📂 프로젝트 구조

- `index.html`: 사용자에게 힌트를 보여주는 메인 UI 페이지
- `update_hint.py`: 정답을 추출하고 데이터를 가공하는 파이썬 스크립트
- `data.json`: 현재 활성화된 힌트 데이터가 저장되는 파일
- `.github/workflows/auto_update.yml`: 매일 새벽 자동 실행을 담당하는 워크플로우

## ⚙️ 자동화 프로세스 (Workflow)

1. **Schedule**: 매일 01:00 KST (16:00 UTC) 워크플로우 실행
2. **Extraction**: Python 스크립트가 꼬맨틀 API 호출
3. **Encryption**: 추출된 정답을 Base64로 인코딩하여 보안 강화
4. **Deployment**: 업데이트된 `data.json`을 저장소에 자동 커밋 및 푸시
5. **Service**: 사용자가 페이지 접속 시 최신 데이터를 불러와 힌트 노출

---
*본 프로젝트는 오로지 저의 편의를 위해 제작되었습니다.*
