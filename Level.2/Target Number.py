"""
<풀이방법>
'코드채점하고제출'을 해보니, 정확도 평가밖에 없어서 모든 경우의 수를 다 구해보면 되겠다 싶었음

1. numbers 리스트의 모든 항에 +/- 부호를 붙인 새로운 리스트(branch)를 만듦
2. branch 리스트의 각 항목이 짝꿍을 이룰 수 있는 모든 경우의수 구해서 -> 좋은 모듈이 있더군
3. 경우의 수를 모두 더한 새로운 리스트(branch_sum)을 만듦
4. branch_sum에서 target과 같은 수를 세주면 끝
"""

from itertools import product
def solution(numbers, target):
    branch = [(i, -i) for i in numbers]
    branch_sum = list(map(sum, product(*branch)))
    answer = branch_sum.count(target)
    return answer


#################################
## 모듈을 쓰지 않고 풀어본 모범답안
##         1. 재귀 사용         
#################################


def solution(numbers, target):
    cnt = 0

    def branches(idx=0):
        if idx < len(numbers):
            numbers[idx] *=1
            branches(idx+1)

            numbers[idx] *=-1
            branches(idx+1)

        elif sum(numbers) == target:
            nonlocal cnt
            cnt +=1
    branches()

    return cnt

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))



#################################
## 모듈을 쓰지 않고 풀어본 모범답안
##     2. 더 신기한 재귀 사용
#################################

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))



#################################
## 모듈을 쓰지 않고 풀어본 모범답안
##     3. 하나하나 만들어줌
#################################

def solution(n, t):
    answer = 0
    for i in range(2**len(n)):
        tmp = []
        for j in range(len(n)):
            if i & (2**j) == 0:
                tmp.append(n[j])
            else:
                tmp.append(-1*n[j])
        if sum(tmp) == t:
            answer += 1
    return answer



#################################
## 모듈을 쓰지 않고 풀어본 모범답안
##     4. for _ in 은 뭘까?
#################################

def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)