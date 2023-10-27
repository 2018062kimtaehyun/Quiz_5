def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

# 함수를 정의하여 환기량을 계산하는 부분
def calculate_ventilation_volume(volume):
    ventilation_volume = volume * 20
    return ventilation_volume

length = float(input("가로 길이를 입력하세요: "))
width = float(input("세로 길이를 입력하세요: "))
height = float(input("높이를 입력하세요: "))

# 체적 계산
volume = calculate_volume(length, width, height)
print(f"해당 밀폐공간의 체적은 {volume} 입니다.")

# 환기량 계산
ventilation_volume = calculate_ventilation_volume(volume)
print(f"환기량은 {ventilation_volume}/hr 입니다.")
