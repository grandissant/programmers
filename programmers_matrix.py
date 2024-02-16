def solution(arr1, arr2):
    answer = [] # arr1과 arr2의 행렬을 더해서 나온 값을 저장할 행렬 생성
   
    for i in range(len(arr1)): # arr1의 길이 만큼 반복하여서 answer의 리스트 값을 넣는다
        answer.append([])
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j] + arr2[i][j]) #리스트 값 삽입
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[4,5],[5,6]]

print(solution(arr1, arr2))