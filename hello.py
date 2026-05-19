# 이전 기록 불러오기
print("=== 이전 기록 ===")
try:
    with open("체온기록.txt", "r", encoding="utf-8") as 파일:
        print(파일.read())
except:
    print("이전 기록 없음\n")

# 새로 입력받기
기록 = []
for i in range(1, 4):
    시간 = input(str(i) + "번째 측정 시간: ")
    체온 = float(input("체온: "))
    기록.append({"시간": 시간, "체온": 체온})

# 파일에 저장 (이어쓰기)
with open("체온기록.txt", "a", encoding="utf-8") as 파일:
    for 측정 in 기록:
        if 측정["체온"] >= 38.0:
            상태 = "병원 가세요!"
        elif 측정["체온"] >= 37.5:
            상태 = "미열이에요"
        else:
            상태 = "정상이에요"
        줄 = 측정["시간"] + " / " + str(측정["체온"]) + "도 / " + 상태 + "\n"
        파일.write(줄)

print("저장 완료!")
pip install openpyxl