"""
<풀이방법>
문자열을 1개 단위로 잘랐을 때부터 "len(s)//2"개 단위로 잘랐을 때까지 모든 경우를 살펴봄
모든 경우 중에서 제일 짦은 문자열 길이 출력
문자열 슬라이싱 사용
한 점을 잡고 그 이후의 두번째 점을 왔다갔다 하면서 슬라이싱을 할거라.. 이중포믄 돌려야될 듯
"""


def solution(s):
    lnth = []  # 모든 단위로 잘랐을 때의 문자열 길이를 담을 리스트
    rslt = ""  # 모든 단위로 잘랐을 때의 문자열을 담을 변수

    # 문자열 길이가 1인 경우
    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):  # 문자열 길이의 절반 이하인 i만큼만 단위를 확인함
        cnt = 1
        std = s[:i]  # 비교기준(std) 설정: 처음에는 제일 앞부터 정해진 길이만큼 자름

        for j in range(i, len(s), i):  # j는 i부터 len(s)까지 i배수만큼으로 설정
            if s[j:j + i] == std:  # 비교대상이 비교기준(std)과 같으면
                cnt += 1  # 횟수에 1 추가

            else:  # 비교대상이 비교기준(std)과 다르면
                if cnt == 1:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략한다고 하니..cnt1이면 문자열만 추가할거라 cnt는 걍 비움
                    cnt = ""
                rslt += str(cnt) + std  # 횟수(숫자)를 문자값으로 바꾸고 비교기준(std)과 합해서 result로 보냄
                std = s[j:j + i]  # 새로운 비교기준(std) 설정
                cnt = 1  # 횟수 1로 설정하고 두번째 for문 계속 돌아감

        if cnt == 1:
            cnt = ""
        rslt += str(cnt) + std
        lnth.append(len(rslt))  # 최종 result의 길이를 length 리스트에 추가
        rslt = ""  # result값 비우고 첫번째 for문 계속 돌아감

    return min(lnth)  # 리스트에서 최소값이 답