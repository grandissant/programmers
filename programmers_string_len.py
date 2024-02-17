
def solution(s): #문자열의 길이가 4 또는 6이고 숫자로 이루어져있는지 확인하는 함수
    if (len(s) == 4 or len(s) == 6) and s.isdigit():#isdigit함수 숫자로만 이루어져있는지 판별
        return True
    else:
        return False

print(solution("a234"))
print(solution("1234"))
