"""
문제조건; 2명만 태울 수 있음

풀이방법;
제일 무게 적은 사람이랑 제일 무게 많은 사람 더한 게 limit 값을 넘어가는지 아닌지 판단하고 같이 태울 사람은 같이 태워버림
"""

def solution(people, limit):
    answer = 0
    i = 0
    j = len(people) - 1
    people.sort()

    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

    return answer