def caesar(s, n):


    lower_list = "abcdefghijklmnopqrstuvwxyz"#소문자 알파벳 리스트
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#대문자 알파벳 리스트

    result = []#변환된 알파벳을 저장

    for i in s:#암호화 할 s만큼 i를 반복
        if i == " ":#i가 공백이면
            result.append(" ")#공백을 삽입
        elif i.islower() is True:#i가 소문자이면
            newstring = lower_list.find(i) + n#문자열 반환
            result.append(lower_list[newstring % 26])#알파벳을 순환하여 변환된 알파벳을 저장
        else:
            newstring = upper_list.find(i) + n
            result.append(upper_list[newstring % 26])
    return "".join(result)#리스트안의 문자열을 연결

s = "Hello World"
n = 3
en = caesar(s, n)
print(en)
