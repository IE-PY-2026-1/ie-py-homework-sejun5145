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




expense_list = []
current_budget = 0
initial_budget = 0
danger_ratio = 0.0

# [요구사항 2] 함수 1: 메인 메뉴 출력 함수
def display_menu():
    print("\n" + "="*30)
    print(" 1. 지출 내역 등록")
    print(" 2. 지출 요약 및 상태 분석")
    print(" 0. 프로그램 종료")
    print("="*30)

# [요구사항 2, 3, 5] 함수 2: 지출 등록 함수 (매개변수 사용, global 사용)
def add_expense(expense_amount):
    global current_budget  # 전역 변수 수정 권한 부여
    
    if expense_amount < 0:
        print("음수는 지출로 등록할 수 없습니다.")
    else:
        expense_list.append(expense_amount)
        current_budget -= expense_amount
        print(f"[{expense_amount}원] 지출이 정상적으로 등록되었습니다.")

# [요구사항 2, 3, 4] 함수 3: 예산 상태 판별 함수 (매개변수 사용, return 사용)
def evaluate_budget_status(remain, initial, danger_rate):
    ratio = remain / initial
    
    # 처리 결과를 return 문을 통해 반환
    if remain < 0:
        return "🚨 [경고] 예산을 초과했습니다! 파산 상태입니다."
    elif ratio <= danger_rate:
        return "⚠️ [주의] 잔여 예산이 위험 수준입니다! 과소비를 자제하세요."
    else:
        return "✅ [안전] 예산을 잘 관리하고 있습니다. 훌륭해요!"

# [요구사항 2] 함수 4: 통계 출력 함수 (내부에서 함수 3 호출)
def show_statistics():
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
        
        # return 값을 받아와서 출력
        status_message = evaluate_budget_status(current_budget, initial_budget, danger_ratio)
        print(status_message)
    else:
        print("\n기록된 지출 내역이 없습니다.")

# ==========================================
# 메인 프로그램 로직 (while 문 내부를 목차처럼 간결하게)
# ==========================================
print("=== 스마트 캠퍼스 가계부 V2.0 시작 ===")
user_name = input("사용자 이름을 입력하세요: ")
initial_budget = int(input("이번 달 목표 총예산을 입력하세요 (원): "))
danger_ratio = float(input("위험 경고 기준 비율을 소수점으로 입력하세요 (예: 20% -> 0.2): "))

current_budget = initial_budget  # 초기 예산 세팅

# [요구사항 1] while True 무한 루프 및 break 활용
while True:
    display_menu()
    choice = input("원하시는 메뉴 번호를 선택하세요: ")
    
    if choice == '1':
        amount = int(input("지출 금액을 입력하세요: "))
        add_expense(amount)  # 함수 호출
        
    elif choice == '2':
        show_statistics()  # 함수 호출
        
    elif choice == '0':
        print(f"\n{user_name}님의 가계부 프로그램을 안전하게 종료합니다. 이용해 주셔서 감사합니다!")
        break  # 사용자 '종료' 선택 시에만 break
        
    else:
        print("잘못된 입력입니다. 0, 1, 2 중에서 선택해 주세요.")


