def solution(n):
    water = "수박"
    answer = water * (n//2) + water[0:n%2]
    return answer