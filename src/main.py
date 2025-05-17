import pyautogui
import pyperclip
import time
from convert import convert



def get_selected_text_and_replace_with_converted():
    # 현재 선택된 텍스트를 클립보드로 복사
    original_clipboard = pyperclip.paste()  # 기존 클립보드 내용 저장

    # Ctrl+C를 자동으로 누름
    pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.1)  # 클립보드에 내용이 복사될 때까지 잠시 대기

    # 클립보드에서 선택된 텍스트 가져오기
    selected_text = pyperclip.paste()

    if selected_text:
        # 텍스트 변환 (여기서는 convert 함수 사용)
        converted_text = convert(selected_text)

        # 변환된 텍스트를 클립보드에 복사
        pyperclip.copy(converted_text)

        # Ctrl+V를 자동으로 눌러 변환된 텍스트로 대체
        pyautogui.hotkey('ctrl', 'v')

        # 작업 완료 후 기존 클립보드 내용 복원
        # time.sleep(0.1)
        pyperclip.copy(original_clipboard)

        return True
    else:
        print("선택된 텍스트가 없습니다.")
        return False


# 메인 함수를 다음과 같이 수정
def main():
    try:
        success = get_selected_text_and_replace_with_converted()
        if success:
            print("텍스트가 성공적으로 변환되었습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
