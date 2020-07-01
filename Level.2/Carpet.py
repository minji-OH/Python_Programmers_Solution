"""
<풀이 방법>
1. brown은 1줄
2. yellow가 1겹-2겹-3겹-... 일 때 brown을 한 줄로 감쌀 수 있는지 판단하면 됨
3. 감쌀 수 있으면 그 때의 가로/세로를 배열에 담으면 됨

(1) yellow가 1겹일 때
가 로: (yellow/1) + 2
세 로: 1+2
확인식: brown = 2*(yellow/1) + (1+2)*2

(2) yellow가 2겹일 때
가 로: (yellow/2) + 2
세 로 : 2+2
확인식: brown = 2*(yellow/2) + (2+2)*2
.
.
.
(i) yellow가 i겹일 때
가 로: (yellow/i) + 2
세 로: i+2
확인식: brown = 2*(yellow/i) + (i+2)*2
"""

def solution(brown, yellow):
    answer = []
    i=1
    while True:
        if 2*(yellow/i)+(i+2)*2 == brown:
            if (yellow/i+2) >= (i+2):
                answer.append(yellow/i+2)
                answer.append(i+2)
                break
        else:
            i += 1
    return answer