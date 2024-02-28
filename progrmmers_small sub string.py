t = input("숫자를 입력하세요: ")
p = input("숫자를 입력하세요: ")

def solution(t, p):
    answer = 0
    p_len = len(p)
    t_len = len(t)
    
    for i in range(t_len - p_len + 1): # t에서 p의 길이만큼의 부분 문자열을 순회
        # t의 부분 문자열을 직접 비교 대상으로 사용
        if int(t[i:i+p_len]) <= int(p):
            answer += 1
            
    return answer

print(solution(t, p))
