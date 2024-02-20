n = int(input("자연수 n:")) #나누고 싶은 값

def solution(n):
    for i in range(1,n): # 1부터 n-1번째 까지 반복하기
        if n%i == 1: #n을 나누어 나머지가 1이면
            answers = i #나머지가 1이 나오게 한 i값을 answer에 저장
            return answers #최솟값을 받기에 첫 i값을 받으면 반환

answer = solution(n)
print(answer)
