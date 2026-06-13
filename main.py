# 파일이름 :
# 작 성 자 :
expense_data = [] 
current_budget = 0
initial_budget = 0
danger_ratio = 0.0
FILE_NAME = "expense_record.csv"

def load_data():
    global current_budget
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                date, category, amount = line.strip().split(',')
                expense_data.append([date, category, int(amount)])
                current_budget -= int(amount)
        print("📁 기존 지출 내역을 성공적으로 불러왔습니다.")
    except FileNotFoundError:
        print("⚠️ 기존에 저장된 지출 내역 파일이 없습니다. 새로운 가계부를 시작합니다.")

def save_data():
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for record in expense_data:
            file.write(f"{record[0]},{record[1]},{record[2]}\n")
    print("💾 지출 내역이 파일에 안전하게 저장되었습니다.")

def display_menu():
    print("\n" + "="*30)
    print(" 1. 상세 지출 내역 등록")
    print(" 2. 지출 요약 및 상태 분석")
    print(" 3. 수동으로 데이터 저장하기")
    print(" 0. 프로그램 종료")
    print("="*30)

def add_expense():
    global current_budget
    
    date = input("지출 날짜를 입력하세요 (예: 11/05): ")
    category = input("지출 카테고리를 입력하세요 (예: 식비, 교통비): ")
    
    try:
        amount = int(input("지출 금액을 숫자로만 입력하세요 (원): "))
        if amount < 0:
            print("음수는 지출로 등록할 수 없습니다.")
            return
            
        expense_data.append([date, category, amount])
        current_budget -= amount
        print(f"✅ [{date} / {category} - {amount}원] 지출이 정상적으로 등록되었습니다.")
    except ValueError:
        print("🚨 [오류] 금액은 문자가 아닌 '숫자'로만 입력해야 합니다! 메뉴로 돌아갑니다.")

def evaluate_budget_status(remain, initial, danger_rate):
    ratio = remain / initial
    if remain < 0:
        return "🚨 [경고] 예산을 초과했습니다! 파산 상태입니다."
    elif ratio <= danger_rate:
        return "⚠️ [주의] 잔여 예산이 위험 수준입니다! 과소비를 자제하세요."
    else:
        return "✅ [안전] 예산을 잘 관리하고 있습니다. 훌륭해요!"

def show_statistics():
    print("\n=== [상세 지출 내역 및 요약 통계] ===")
    valid_count = len(expense_data)
    
    if valid_count > 0:
        print("-" * 40)
        print("번호 | 날짜   | 카테고리 | 금액")
        print("-" * 40)
        
        total_expense = 0
        max_expense = 0
        
        for i, record in enumerate(expense_data,
