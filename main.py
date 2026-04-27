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



print("=== 스마트 캠퍼스 가계부 V1.0 ===")

user_name = input("사용자 이름을 입력하세요: ")
initial_budget = int(input("이번 달 목표 총예산을 입력하세요 (원): "))
danger_ratio = float(input("위험 경고 기준 비율을 소수점으로 입력하세요 (예: 20% -> 0.2): "))

current_budget = initial_budget 
expense_list = [] 

print(f"\n--- {user_name}님의 지출 내역 입력 (최대 5회 입력 가능, 0 입력 시 종료) ---")

for i in range(1, 6):
    expense = int(input(f"[{i}번째] 지출 금액을 입력하세요 (0: 조기 종료, 음수: 무시): "))

    if expense == 0:
        print("입력을 조기 종료합니다.")
        break  
    elif expense < 0:
        print("음수는 지출로 등록할 수 없습니다. 건너뜁니다.")
        continue  
    else:
        expense_list.append(expense) 
        current_budget -= expense    

valid_count = len(expense_list)

if valid_count > 0:
    total_expense = sum(expense_list)
    max_expense = max(expense_list)
    remain_ratio = current_budget / initial_budget

    print(f"\n=== [지출 요약 통계] ===")
    print(f"등록된 총 지출 건수: {valid_count}건")
    print(f"가장 큰 단일 지출 금액: {max_expense}원")
    print(f"총 지출 금액: {total_expense}원")
    print(f"남은 예산: {current_budget}원 (잔여 비율: {remain_ratio*100:.1f}%)")

    if current_budget < 0:
        print("🚨 [경고] 예산을 초과했습니다! 파산 상태입니다.")
    elif remain_ratio <= danger_ratio and remain_ratio >= 0:
        print("⚠️ [주의] 잔여 예산이 위험 수준입니다! 과소비를 자제하세요.")
    else:
        print("✅ [안전] 예산을 잘 관리하고 있습니다. 훌륭해요!")
else:
    print("\n기록된 유효한 지출 내역이 없습니다.")