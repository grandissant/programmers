#이용료를 알기위한 변수값 받기
price = int(input("price:"))
count = int(input("count:"))
money = int(input("money:"))

def solution(price,count,money):
    cost = 0

    #use = price * count #이용료 구하기

    for i in range(1, count + 1):
        cost += price * i # 이용금액을 계산하여 이용료를 합한다

    change = money - cost #잔돈 계산

    # 금액이 모자라면 모자란 값을 return 또는 금액이 부족하지 않으면 0을 return
    if change < 0:
        return -change
    else:
        return 0
answer = solution(price,count,money)
print(answer)
