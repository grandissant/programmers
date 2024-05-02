def solution(n):
    # 3부터 시작하여 n-1까지 반복
    for x in range(3, n):
        if n % x == 1:
            return x

# 입력 예시
print(solution(10))  # 결과는 3
print(solution(12))  # 결과는 11