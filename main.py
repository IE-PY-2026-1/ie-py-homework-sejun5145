# 파일이름 :
# 작 성 자 :
print("=" * 45)
print(" 💰 스마트 캠퍼스 가계부 V1.0 💰 ")
print("=" * 45)

# 1. 데이터 입력 (변수 4개 사용, str 및 int 자료형)
user_name = input("사용자 이름을 입력하세요: ")
total_budget = int(input("이번 달 목표 예산을 입력하세요(원): "))
expense_category = input("지출 카테고리를 입력하세요 (예: 식비, 교통비): ")
expense_amount = int(input("오늘 지출한 금액을 입력하세요(원): "))

# 2. 데이터 처리 (산술 연산 및 float 자료형 생성)
# 남은 예산 계산 (뺄셈)
remaining_budget = total_budget - expense_amount

# 예산 소진율 계산 (나눗셈 및 곱셈, 결과는 float)
used_ratio = (expense_amount / total_budget) * 100

# 3. 결과 출력 (f-string 활용 및 서식 지정)
print("\n" + "=" * 45)
print(f"▶ {user_name}님의 가계부 입력 결과 ◀")
print("-" * 45)
# :, 를 사용하여 금액에 천 단위 구분에 쉼표를 찍어줍니다.
print(f" - 한 달 목표 예산: {total_budget:,}원")
print(f" - 지출 카테고리  : {expense_category}")
print(f" - 오늘 지출 금액 : {expense_amount:,}원")
print("-" * 45)
print(f" ✅ 남은 예산    : {remaining_budget:,}원")
# {:.2f} 를 사용하여 소수점 둘째 자리까지만 깔끔하게 출력합니다.
print(f" 📊 예산 소진율  : {used_ratio:.2f}%")
print("=" * 45)
