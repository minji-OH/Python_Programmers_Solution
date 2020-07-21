"""
예제는 풀리는데
런타임 에러 + 시간초과

heap 모듈을 어떻게 쓰는지 모르겠음
"""

def solution(scoville, K):
    answer = 0
    while True:
        if min(scoville) >= K:
            break
        else:
            scoville.sort()
            scoville[0] = scoville[1]*2 + scoville[0]
            del scoville[1]
            answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))