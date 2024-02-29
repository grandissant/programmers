s = input("영문자를 입력하세요:")

def solution(s):
    string = s.lower()#대문자 소문자 구분없이 처리하기 위해 강제 소문자 변환

    if string.count('p') == string.count('y'):#p와 y의 수를 세고 비교
        return True
    else:
        return False

solution(s)
