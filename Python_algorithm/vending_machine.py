# 투입된 금액을 확인하고, 거스름돈을 돌려주는 문제
# 이때 거스름돈의 단위를 최대로 한다.

# 가능한 거스름돈 단위
change_list = [10000, 5000, 1000, 500, 100, 50, 10, 1]

buying = True

def change_calc(unit, change):
    # change 가능한 단위를 돌기
    unit_count = change // unit
    left = change % unit
    return left, unit_count


while buying:
    try:
        # 투입된 금액과 물건의 금액을 확인하여 거스름돈 계산
        insert_price = int(input("INSERT MONEY : "))
        product_price = int(input("PRODUCT MONEY : "))
        change = insert_price - product_price
        return_change = []
        
        if change < 0:
            print("Please insert more money.")
            continue
        else:
            change_avaliable = []
            for i in change_list:
                if change > i:
                    change_avaliable.append(i)
                else:
                    return_change.append(0)

            for unit in change_avaliable:
                left, unit_count = change_calc(unit, change)
                change = change - (unit * unit_count)
                return_change.append(unit_count)
        
        print("남은 잔돈은 10000원짜리 %d개, 5000원짜리 %d개, 1000원짜리 %d개, 500원짜리 %d개, 100원짜리 %d개, 50원짜리 %d개, 10원짜리 %d개, 1원짜리 %d개 입니다."
            %(return_change[0], return_change[1], return_change[2], return_change[3], 
            return_change[4], return_change[5], return_change[6], return_change[7]))
            
    except ValueError:
        print("잘못된 입력입니다. 프로그램을 종료합니다.")
        break