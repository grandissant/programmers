def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        answer = [-1]
        return answer