from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    max_gap = -1

    for combi in combinations_with_replacement(range(11), n): 
        info2 = [0] * 11

        for i in combi:
            info2[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info2[idx] == 0: 
                continue
            elif info[idx] >= info2[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:  
            if lion - apeach > max_gap:  
                max_gap = gap
                answer = info2
    return answer
