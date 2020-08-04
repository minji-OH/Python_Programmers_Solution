import itertools
n = len(number)
idx = list(range(n))
del_idx = list(itertools.combinations(idx, k))
T_idx = [0]*len(del_idx)
R_number = [0]*len(del_idx)
lst = [int(i) for i in number]

for i in range(len(del_idx)):
    T_idx[i] = list(set(idx).difference(del_idx[i]))

# 이제 여기에서 T_idx 리스트에 담긴 인덱스를 포함한 숫자배열을 조합하고, 그 중에 제일 큰 놈을 return하면 되는데
# 그걸 못하겠네..
