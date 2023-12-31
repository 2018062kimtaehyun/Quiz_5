def 주민등록번호_유효성_검사(주민등록번호):
    if len(주민등록번호) != 13 or not 주민등록번호.isdigit():
        return False

    곱하는_값 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    주민등록번호 = list(map(int, 주민등록번호))
    검사숫자 = 주민등록번호[-1]  # 주민등록번호의 마지막 자리

    합계 = sum(곱하는_값[i] * 주민등록번호[i] for i in range(12))
    나머지 = 합계 % 11
    계산된_검사숫자 = (11 - 나머지) % 10  # 나머지가 0인 경우를 처리하기 위해 % 10 사용

    return 계산된_검사숫자 == 검사숫자

# 주민등록번호 입력
주민등록번호 = input("주민등록번호를 입력하세요 (13자리): ")

if 주민등록번호_유효성_검사(주민등록번호):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")
