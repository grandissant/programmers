left = int(input("수를 입력하세요:"))
right = int(input("수를 입력하세요:"))



def solution(left, right):#약수의 갯수 구하기
   
    
    answer = 0#약수의 계산식을 할 변수

    for i in range(left,right+1,1):#left부터 right까지 반복
        count = 0#약수의 갯수
        for j in range(1, i+1, 1):#1부터 i의 수까지 반복
            if i % j == 0:#나누어 떨어지면
                count += 1#약수 갯수 세기

        if count % 2 == 0:#약수의 갯수가 짝수이면
            answer += i
        else:#약수의 갯수가 홀수이면
            answer -= i
        
    return answer

print(solution(left, right))


