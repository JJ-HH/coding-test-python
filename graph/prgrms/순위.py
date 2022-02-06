def solution(n, results):
    PLAYERS = (1, n+1)
    wins = {k: set() for k in range(*PLAYERS)}
    losses = {k: set() for k in range(*PLAYERS)}

    for w, l in results:
        wins[w].add(l)
        losses[l].add(w)

    for _self in range(*PLAYERS):
        for lower_ranker in wins[_self]:
            losses[lower_ranker] |= losses[_self]
        for higher_ranker in losses[_self]:
            wins[higher_ranker] |= wins[_self]
            
    ranked = [i for i in range(*PLAYERS) if len(wins[i] | losses[i]) == n-1]
    return len(ranked)


if __name__=="__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, results))

    n = 5
    results = [[3, 1], [2, 3], [4, 3], [2, 4], [4, 3], [4, 5]]
    print(solution(n, results))
