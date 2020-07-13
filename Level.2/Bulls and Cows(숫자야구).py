"""
<풀이 방법>
1. 정확성만 보니까 효율성은 생각 안 할 것임
2. 1~9로 만들 수 있는 세자리수 조합(permutations, 중복 X) 만듦
3. 세 자리수 조합이 baseball 조건에 맞는지 판단
4. 맞으면 살려두고, 안 맞으면 버림
5. baseball의 모든 조건을 거름망처럼 적용시켜보고 살아남은 수의 개수를 세줌
"""

from itertools import permutations
import copy

def solution(baseball):
    # 1~9까지 만들 수 있는 세자리수 조합을 all(리스트)에 담음
    numbers = list(range(1, 10))
    all = list(permutations(numbers, 3))
    # strike, ball 값
    s, b = 0, 0
    # all을 복사해서 baseball 조건에 맞는 숫자만 살릴 예정
    basket = copy.deepcopy(all)

    # 질문의 수(=len(baseball))만큼 for문 돌릴 예정
    for i in range(len(baseball)):
        # 비교 편하게 하려고 숫자를 문자형으로 바꿈
        n_str = str(baseball[i][0])
        # 모든 조합(all)에서 하나씩 꺼내서 조건과 비교
        for j in all:
            # 세 자리수니까 k의 범위는 3
            for k in range(3):
                # strike 조건
                if int(n_str[k]) == j[k]:
                    s += 1
                # ball 조건
                if int(n_str[k]) in j:
                    b += 1
            # strike 조건과 ball 조건 모두 만족 못하면 버림
            # 위에 if문에서 b는 baseball의 strike와 ball을 모두 포함하기 때문에 더해야함
            if s != baseball[i][1] or b != (baseball[i][1]+ baseball[i][2]):
                # 조건 만족 못하는 숫자가 basket에 있으면 버림
                if j in basket:
                    basket.remove(j)
            # all의 j숫자의 다음 비교를 위해 s, b 초기화
            s, b = 0, 0

    # basket에 최종적으로 남은 수를 세면 끝
    return (len(basket))


"""
어렵다....어려워....떼잉...
"""