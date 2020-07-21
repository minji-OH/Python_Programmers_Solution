"""
citations를 내림차순 정렬
각 항목은 자기자신 이상 인용된 항목이 [인덱스+1]개 이상있음.
ciations[i] 가 (i+1)이 되는 최초의 i를 출력하면 됨

예외로 [5, 5, 5, 5]같은 경우, h인덱스가 없어서 0이 나와야 함
"""

# 근데 틀렸대
# 런타임에러는 없음.
# 11, 16번만

def solution(citations):
    citations.sort(reverse=True)
    i = 0
    while True:
        if i >= len(citations):
            answer = 0
            break
        elif citations[i] <= i+1:
            answer = citations[i]
            break
        else:
            i += 1
    return answer

citations = [5, 5, 5, 5]
print(solution(citations))