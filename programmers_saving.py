#####PCCE 기출문제 4번 / 저축#####
start = int(input())#첫 달 저축액
before = int(input())#70만원 이상을 모을 때 두 번째 달부터의 저축액
after = int(input())#100만원 이상을 모을 때 저축액

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1
print(month)