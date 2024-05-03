def solution(n):
    sum = 0 #n의 약수들의 합
    for i in range(1,n+1): #i가 0이면 나눌수없으므로 1부터 시작
        if n % i == 0:
            sum += i
        
    return sum