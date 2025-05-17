# 한/영 타자 변환기 (Korean/English Typing Converter)

텍스트의 한글과 영문 타이핑을 상호 변환해주는 간단한 유틸리티입니다. 잘못된 키보드 레이아웃으로 입력한 텍스트를 올바른 형태로 변환합니다.

## 기능

- **영타 → 한글**: 영문 키보드로 타이핑한 텍스트를 한글로 변환 (예: `dkssud` → `안녕`)
- **한글 → 영타**: 한글로 타이핑한 텍스트를 영문 키보드 입력으로 변환 (예: `ㅎㄷㄹㄹㅐ` → `hello`)
- **클립보드 지원**: 클립보드의 텍스트를 자동으로 변환하여 다시 클립보드에 복사
- **텍스트 선택 변환**: 선택한 텍스트를 자동으로 변환하여 대체

## 설치 방법

### 요구 사항

- Python 3.11 이상
- uv 패키지 관리자

### 설치 단계

1. 이 저장소를 클론합니다:
```bash
git clone https://github.com/yourusername/korean-english-converter.git
cd korean-english-converter
```

2. 가상 환경을 생성하고 활성화합니다:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. 필요한 패키지를 설치합니다:
```bash
uv pip install -r requirements.txt
```

## 사용 방법

### 클립보드 변환 사용 (convert.py)

1. 변환하려는 텍스트를 클립보드에 복사합니다.
2. 스크립트를 실행합니다:
```bash
python convert.py
```
3. 변환된 텍스트가 자동으로 클립보드에 저장됩니다.

### 선택 텍스트 자동 변환 (main.py)

1. 변환하려는 텍스트를 선택합니다.
2. 스크립트를 실행합니다:
```bash
python main.py
```
3. 선택한 텍스트가 자동으로 변환되어 원래 위치에 대체됩니다.

## 단축키 설정 (권장)

더 편리한 사용을 위해 운영 체제의 단축키 설정을 통해 `main.py` 스크립트를 특정 키 조합에 할당하는 것을 권장합니다:

### Windows
1. 스크립트를 실행하는 배치 파일(.bat)을 생성합니다.
2. 바로가기를 만들고 원하는 단축키를 지정합니다.

### macOS
1. Automator나 AppleScript를 사용하여 스크립트를 실행하는 워크플로우를 생성합니다.
2. 시스템 환경설정에서 키보드 단축키를 할당합니다.

### Linux
1. 시스템 설정에서 사용자 지정 단축키를 생성합니다.
2. 스크립트 실행 명령을 단축키에 할당합니다.

## 필요한 패키지

다음 패키지들이 필요합니다:
```
pyperclip
pyautogui
```

`requirements.txt` 파일을 생성하려면:
```bash
echo "pyperclip\npyautogui" > requirements.txt
```

## 라이선스

MIT

## 기여하기

기여는 언제나 환영합니다! 이슈를 등록하거나 풀 리퀘스트를 보내주세요.
