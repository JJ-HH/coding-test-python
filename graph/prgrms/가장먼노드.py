from collections import deque


def solution(n, edge):
    q = deque([1])
    to_visit = [False] + [True]*n
    graph ={k: set() for k in range(1, n+1)}
    for v1, v2 in edge:
        graph[v1].add(v2)
        graph[v2].add(v1)

    dist = [-1, 0] + [100000]*(n-1)

    while q:
        curr = q.popleft()
        if not to_visit[curr]:
            continue 
        to_visit[curr] = False
        for i in graph[curr]:
            if i in graph[curr] and to_visit[i] \
            and (new_d := dist[curr] + 1) < dist[i]:
                dist[i] = new_d
                q.append(i)
    
    print(dist)
    return dist.count(max(dist))


if __name__=="__main__":
    n = 6 
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
    print(solution(n, edge))
