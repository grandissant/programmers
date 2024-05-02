def solution(sizes):
    
    resized = [[max(size), min(size)] for size in sizes]#sizes에서 가장 큰 값과 가장 작은 값을 배치
    
    max_width = max(size[0] for size in resized)# 재배치된 명함 중 가장 긴 가로길이 찾기
    max_height = max(size[1] for size in resized)#재배치된 명함 중 가장 긴 세로 길이 찾기
   
    return max_width * max_height # 가장 긴 가로와 세로 길이의 곱 반환