str1 = input("부분 문자열을 입력하세요:")
str2= input("문자열을 입력하세요:")

def solution(str1, str2):
    answer = 0
    if str1 in str2:#str2안에 str1이 포함되어있으면
        return 1
    else:
        return 0
    
print(solution(str1, str2))