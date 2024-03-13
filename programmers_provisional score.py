def solution(our_score, score_list):
    # 결과를 저장할 리스트를 함수 내부에서 초기화
    answer = []
    # our_score와 score_list의 길이가 같다고 가정하고 비교
    for i in range(len(our_score)):
        if our_score[i] == score_list[i]:
            answer.append("Same")
        else:
            answer.append("Different")

    return answer

# 사용자 입력 처리
numbers_input = input("문의하는 학생들 번호: ")
# 입력받은 문자열을 공백으로 구분하여 정수 리스트로 변환
numbers = list(map(int, numbers_input.split()))

# 예시 데이터: 가채점한 점수와 실제 성적
our_score = [95, 85, 75]  # 예시 가채점 점수
score_list = [95, 80, 75]  # 예시 실제 성적

# 함수 호출
answer = solution(our_score, score_list)
print(answer)
