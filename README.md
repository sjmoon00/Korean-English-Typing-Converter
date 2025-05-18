# 한/영 타자 변환기 (Korean/English Typing Converter)

텍스트의 한글과 영문 타이핑을 상호 변환해주는 간단한 유틸리티입니다. 잘못된 키보드 레이아웃으로 입력한 텍스트를 올바른 형태로 변환합니다.

## 기능

- **영타 → 한글**: 영문으로 타이핑한 텍스트를 한글로 변환 (예: `dkssud` → `안녕`)
- **한글 → 영타**: 한글로 타이핑한 텍스트를 영문으로 변환 (예: `ㅗ디ㅣㅐ` → `hello`)
- **텍스트 자동 선택 변환**: 선택한 텍스트를 자동으로 인식,ㅣ 변환하여 대체

## 설치 방법

### 요구 사항

- Python 3.11
- [uv 패키지 관리자](https://docs.astral.sh/uv/)
- [PowerToys](https://learn.microsoft.com/ko-kr/windows/powertoys/install)

### 설치 단계

1. 이 저장소를 클론합니다:
```bash
git clone https://github.com/sjmoon00/Korean-English-Typing-Converter.git
```

2. 프로젝트 실행에 필요한 의존성과 가상환경을 설정합니다:
```bash
uv sync
```

3. 실행 파일로 변환합니다:
```bash
pyinstaller --noconsole --onedir ./src/main.py 
```
실행파일은 dist폴더 내부에 존재합니다.

4. 실행 파일의 바로가기를 만들고 바탕화면 또는 `C:\Users\<YourUser>\AppData\Roaming\Microsoft\Windows\Start` 폴더에 이동합니다. 
## 사용 방법

### 선택 텍스트 자동 변환 (main.py)

1. 변환하려는 텍스트를 선택합니다.
2. 스크립트를 PowerToys로 실행합니다
3. 선택한 텍스트가 자동으로 변환되어 원래 위치에 대체됩니다.

## 단축키 설정 (권장)

원활한 사용을 위해 Powertoys를 통해 사용하기를 권장합니다.

### Windows
1. PowerToys run을 활성화 합니다.
2. 실행 파일로 변환 후 생성된 exe파일을 검색합니다.
3. 엔터를 누르면 실행.

### macOS / Linux
- 따로 고려하지 않았습니다.
- 정상적인 동작을 보장하지 않습니다.


## 라이선스

MIT

## 기여하기

기여는 언제나 환영합니다! 이슈를 등록하거나 풀 리퀘스트를 보내주세요.

## 참고자료
- [한영타변환기 Alfred Workflow 개발기](https://pozafly.github.io/tools/alfred-korean-english-converter/)
- [한영타변환기 원본](https://theyt.net/wiki/%ED%95%9C%EC%98%81%ED%83%80%EB%B3%80%ED%99%98%EA%B8%B0)
- 
