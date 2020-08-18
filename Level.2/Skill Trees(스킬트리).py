"""
<풀이 방법>
skill_trees의 원소를 하나하나씩 살펴봐야할 것 같음
 (1) skill의 자리수에 인덱스를 만들어서 인덱스 순서대로 skill_trees 원소에 들어갔는지 판단
 (2) 순서대로 안 들어갔으면 진행 중인 skill_trees 원소 버리고 다음 타자로 넘어감
 (3) 순서대로 잘 들어갔다면 answer에 1을 넣어서 세어줌
"""

def solution(skill, skill_trees):
    answer = 0

    for i, trees in enumerate(skill_trees):
        idx = 0
        for j in trees:      # skill_trees의 각 항목의 원소(?)를 순차적으로 살펴볼것임
            if j in skill:   # 각 항목의 원소(알파벳)가 skill안에 있는지 확인하고
                if skill[idx] == j:  # skill 원소가 skill_trees의 원소와 같으면
                    idx += 1         # 자리수에 하나를 더해서 loop를 돌 것
                else:
                    break            # 다르면 멈춰라
        else:                # skill의 순서대로 trees가 되어있으면 for문을 나오게 됨
            answer +=1       # 그러면 answer에 1 추가
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))