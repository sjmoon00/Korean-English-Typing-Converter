import pyperclip
import sys

# 키 매핑 정의
ENG_KEY = "rRseEfaqQtTdwWczxvgkoiOjpuPhynbml"
KOR_KEY = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ"
CHO_DATA = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG_DATA = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG_DATA = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"


def is_eng(query):
    """영문자인지 확인"""
    if not query:
        return False
    pattern = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return query[0] in pattern


def make_hangul(cho, jung, jong):
    """초성, 중성, 종성을 조합하여 한글 문자 생성"""
    code = 0xac00 + cho * 21 * 28 + jung * 28 + jong + 1
    return chr(code)


def eng_type_to_kor(src):
    """영타를 한글로 변환"""
    res = ""
    if not src:
        return res

    n_cho = -1
    n_jung = -1
    n_jong = -1

    for i in range(len(src)):
        ch = src[i]
        p = ENG_KEY.find(ch)

        if p == -1:  # 영자판이 아님
            # 남아있는 한글이 있으면 처리
            if n_cho != -1:
                if n_jung != -1:  # 초성+중성+(종성)
                    res += make_hangul(n_cho, n_jung, n_jong)
                else:  # 초성만
                    res += CHO_DATA[n_cho]
            else:
                if n_jung != -1:  # 중성만
                    res += JUNG_DATA[n_jung]
                elif n_jong != -1:  # 복자음
                    res += JONG_DATA[n_jong]

            n_cho = -1
            n_jung = -1
            n_jong = -1
            res += ch

        elif p < 19:  # 자음
            if n_jung != -1:
                if n_cho == -1:  # 중성만 입력됨, 초성으로
                    res += JUNG_DATA[n_jung]
                    n_jung = -1
                    n_cho = CHO_DATA.find(KOR_KEY[p])
                else:  # 종성이다
                    if n_jong == -1:  # 종성 입력 중
                        n_jong = JONG_DATA.find(KOR_KEY[p])
                        if n_jong == -1:  # 종성이 아니라 초성이다
                            res += make_hangul(n_cho, n_jung, n_jong)
                            n_cho = CHO_DATA.find(KOR_KEY[p])
                            n_jung = -1
                    elif n_jong == 0 and p == 9:  # ㄳ
                        n_jong = 2
                    elif n_jong == 3 and p == 12:  # ㄵ
                        n_jong = 4
                    elif n_jong == 3 and p == 18:  # ㄶ
                        n_jong = 5
                    elif n_jong == 7 and p == 0:  # ㄺ
                        n_jong = 8
                    elif n_jong == 7 and p == 6:  # ㄻ
                        n_jong = 9
                    elif n_jong == 7 and p == 7:  # ㄼ
                        n_jong = 10
                    elif n_jong == 7 and p == 9:  # ㄽ
                        n_jong = 11
                    elif n_jong == 7 and p == 16:  # ㄾ
                        n_jong = 12
                    elif n_jong == 7 and p == 17:  # ㄿ
                        n_jong = 13
                    elif n_jong == 7 and p == 18:  # ㅀ
                        n_jong = 14
                    elif n_jong == 16 and p == 9:  # ㅄ
                        n_jong = 17
                    else:  # 종성 입력 끝, 초성으로
                        res += make_hangul(n_cho, n_jung, n_jong)
                        n_cho = CHO_DATA.find(KOR_KEY[p])
                        n_jung = -1
                        n_jong = -1
            else:  # 초성 또는 (단/복)자음이다
                if n_cho == -1:  # 초성 입력 시작
                    if n_jong != -1:  # 복자음 후 초성
                        res += JONG_DATA[n_jong]
                        n_jong = -1
                    n_cho = CHO_DATA.find(KOR_KEY[p])
                elif n_cho == 0 and p == 9:  # ㄳ
                    n_cho = -1
                    n_jong = 2
                elif n_cho == 2 and p == 12:  # ㄵ
                    n_cho = -1
                    n_jong = 4
                elif n_cho == 2 and p == 18:  # ㄶ
                    n_cho = -1
                    n_jong = 5
                elif n_cho == 5 and p == 0:  # ㄺ
                    n_cho = -1
                    n_jong = 8
                elif n_cho == 5 and p == 6:  # ㄻ
                    n_cho = -1
                    n_jong = 9
                elif n_cho == 5 and p == 7:  # ㄼ
                    n_cho = -1
                    n_jong = 10
                elif n_cho == 5 and p == 9:  # ㄽ
                    n_cho = -1
                    n_jong = 11
                elif n_cho == 5 and p == 16:  # ㄾ
                    n_cho = -1
                    n_jong = 12
                elif n_cho == 5 and p == 17:  # ㄿ
                    n_cho = -1
                    n_jong = 13
                elif n_cho == 5 and p == 18:  # ㅀ
                    n_cho = -1
                    n_jong = 14
                elif n_cho == 7 and p == 9:  # ㅄ
                    n_cho = -1
                    n_jong = 17
                else:  # 단자음을 연타
                    res += CHO_DATA[n_cho]
                    n_cho = CHO_DATA.find(KOR_KEY[p])

        else:  # 모음
            if n_jong != -1:  # (앞글자 종성), 초성+중성
                # 복자음 다시 분해
                new_cho = -1  # (임시용) 초성

                if n_jong == 2:  # ㄱ, ㅅ
                    n_jong = 0
                    new_cho = 9
                elif n_jong == 4:  # ㄴ, ㅈ
                    n_jong = 3
                    new_cho = 12
                elif n_jong == 5:  # ㄴ, ㅎ
                    n_jong = 3
                    new_cho = 18
                elif n_jong == 8:  # ㄹ, ㄱ
                    n_jong = 7
                    new_cho = 0
                elif n_jong == 9:  # ㄹ, ㅁ
                    n_jong = 7
                    new_cho = 6
                elif n_jong == 10:  # ㄹ, ㅂ
                    n_jong = 7
                    new_cho = 7
                elif n_jong == 11:  # ㄹ, ㅅ
                    n_jong = 7
                    new_cho = 9
                elif n_jong == 12:  # ㄹ, ㅌ
                    n_jong = 7
                    new_cho = 16
                elif n_jong == 13:  # ㄹ, ㅍ
                    n_jong = 7
                    new_cho = 17
                elif n_jong == 14:  # ㄹ, ㅎ
                    n_jong = 7
                    new_cho = 18
                elif n_jong == 17:  # ㅂ, ㅅ
                    n_jong = 16
                    new_cho = 9
                else:  # 복자음 아님
                    new_cho = CHO_DATA.find(JONG_DATA[n_jong])
                    n_jong = -1

                if n_cho != -1:  # 앞글자가 초성+중성+(종성)
                    res += make_hangul(n_cho, n_jung, n_jong)
                else:  # 복자음만 있음
                    res += JONG_DATA[n_jong]

                n_cho = new_cho
                n_jung = -1
                n_jong = -1

            if n_jung == -1:  # 중성 입력 중
                n_jung = JUNG_DATA.find(KOR_KEY[p])
            elif n_jung == 8 and p == 19:  # ㅘ
                n_jung = 9
            elif n_jung == 8 and p == 20:  # ㅙ
                n_jung = 10
            elif n_jung == 8 and p == 32:  # ㅚ
                n_jung = 11
            elif n_jung == 13 and p == 23:  # ㅝ
                n_jung = 14
            elif n_jung == 13 and p == 24:  # ㅞ
                n_jung = 15
            elif n_jung == 13 and p == 32:  # ㅟ
                n_jung = 16
            elif n_jung == 18 and p == 32:  # ㅢ
                n_jung = 19
            else:  # 조합 안되는 모음 입력
                if n_cho != -1:  # 초성+중성 후 중성
                    res += make_hangul(n_cho, n_jung, n_jong)
                    n_cho = -1
                else:  # 중성 후 중성
                    res += JUNG_DATA[n_jung]
                n_jung = -1
                res += KOR_KEY[p]

    # 마지막 한글이 있으면 처리
    if n_cho != -1:
        if n_jung != -1:  # 초성+중성+(종성)
            res += make_hangul(n_cho, n_jung, n_jong)
        else:  # 초성만
            res += CHO_DATA[n_cho]
    else:
        if n_jung != -1:  # 중성만
            res += JUNG_DATA[n_jung]
        elif n_jong != -1:  # 복자음
            res += JONG_DATA[n_jong]

    return res


def kor_type_to_eng(src):
    """한글을 영타로 변환"""
    res = ""
    if not src:
        return res

    for i in range(len(src)):
        ch = src[i]
        n_code = ord(ch)
        n_cho = CHO_DATA.find(ch)
        n_jung = JUNG_DATA.find(ch)
        n_jong = JONG_DATA.find(ch)
        arr_key_index = [-1, -1, -1, -1, -1]

        if 0xac00 <= n_code <= 0xd7a3:  # 한글 음절
            n_code -= 0xac00
            arr_key_index[0] = n_code // (21 * 28)  # 초성
            arr_key_index[1] = (n_code // 28) % 21  # 중성
            arr_key_index[3] = (n_code % 28) - 1  # 종성
        elif n_cho != -1:  # 초성 자음
            arr_key_index[0] = n_cho
        elif n_jung != -1:  # 중성
            arr_key_index[1] = n_jung
        elif n_jong != -1:  # 종성 자음
            arr_key_index[3] = n_jong
        else:  # 한글이 아님
            res += ch
            continue

        # 실제 Key Index로 변경
        if arr_key_index[1] != -1:  # 중성이 있으면
            if arr_key_index[1] == 9:  # ㅘ
                arr_key_index[1] = 27
                arr_key_index[2] = 19
            elif arr_key_index[1] == 10:  # ㅙ
                arr_key_index[1] = 27
                arr_key_index[2] = 20
            elif arr_key_index[1] == 11:  # ㅚ
                arr_key_index[1] = 27
                arr_key_index[2] = 32
            elif arr_key_index[1] == 14:  # ㅝ
                arr_key_index[1] = 29
                arr_key_index[2] = 23
            elif arr_key_index[1] == 15:  # ㅞ
                arr_key_index[1] = 29
                arr_key_index[2] = 24
            elif arr_key_index[1] == 16:  # ㅟ
                arr_key_index[1] = 29
                arr_key_index[2] = 32
            elif arr_key_index[1] == 19:  # ㅢ
                arr_key_index[1] = 31
                arr_key_index[2] = 32
            else:
                arr_key_index[1] = KOR_KEY.find(JUNG_DATA[arr_key_index[1]])
                arr_key_index[2] = -1

        if arr_key_index[3] != -1:  # 종성이 있으면
            if arr_key_index[3] == 2:  # ㄳ
                arr_key_index[3] = 0
                arr_key_index[4] = 9
            elif arr_key_index[3] == 4:  # ㄵ
                arr_key_index[3] = 2
                arr_key_index[4] = 12
            elif arr_key_index[3] == 5:  # ㄶ
                arr_key_index[3] = 2
                arr_key_index[4] = 18
            elif arr_key_index[3] == 8:  # ㄺ
                arr_key_index[3] = 5
                arr_key_index[4] = 0
            elif arr_key_index[3] == 9:  # ㄻ
                arr_key_index[3] = 5
                arr_key_index[4] = 6
            elif arr_key_index[3] == 10:  # ㄼ
                arr_key_index[3] = 5
                arr_key_index[4] = 7
            elif arr_key_index[3] == 11:  # ㄽ
                arr_key_index[3] = 5
                arr_key_index[4] = 9
            elif arr_key_index[3] == 12:  # ㄾ
                arr_key_index[3] = 5
                arr_key_index[4] = 16
            elif arr_key_index[3] == 13:  # ㄿ
                arr_key_index[3] = 5
                arr_key_index[4] = 17
            elif arr_key_index[3] == 14:  # ㅀ
                arr_key_index[3] = 5
                arr_key_index[4] = 18
            elif arr_key_index[3] == 17:  # ㅄ
                arr_key_index[3] = 7
                arr_key_index[4] = 9
            else:
                arr_key_index[3] = KOR_KEY.find(JONG_DATA[arr_key_index[3]])
                arr_key_index[4] = -1

        # 영어 키로 변환
        for j in range(5):
            if arr_key_index[j] != -1:
                res += ENG_KEY[arr_key_index[j]]

    return res


def convert(query):
    """입력 텍스트에 따라 적절한 변환 함수 호출"""
    if is_eng(query):
        return eng_type_to_kor(query)
    else:
        return kor_type_to_eng(query)


def main():
    try:
        # 클립보드에서 텍스트 가져오기
        input_text = pyperclip.paste().strip()

        if not input_text:
            print("클립보드가 비어있습니다.")
            return

        # 변환 수행
        result = convert(input_text)

        # 변환 결과를 클립보드에 저장
        pyperclip.copy(result)

        # 어떤 변환을 수행했는지 출력
        if is_eng(input_text):
            print("영어 → 한글 변환 완료")
        else:
            print("한글 → 영어 변환 완료")

        print("결과가 클립보드에 복사되었습니다.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()