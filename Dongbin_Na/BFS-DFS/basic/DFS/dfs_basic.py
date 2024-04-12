# DFS 메서드 정의
def dfs(graph, v, visited) :
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * 9
dfs(graph, 1, visited)


def dfs_stack(graph, start):
    visited = [False] * len(graph)  # 방문 여부를 확인하는 리스트
    stack = [start]  # 스택 초기화, 시작 노드를 포함시킴, 가장 초기 시작 노드 : 1

    while stack:  # 스택에 아직 처리할 노드가 남아있는 동안 실행
        v = stack.pop()  # 스택에서 하나의 노드를 꺼냄
        if not visited[v]:  # 해당 노드를 방문하지 않았다면
            visited[v] = True  # 방문 처리
            print(v, end=' ')  # 방문 노드 출력
            # 방문하지 않은 인접 노드를 스택에 추가
            for i in reversed(graph[v]):  # 노드를 방문 순서대로 처리하기 위해 역순으로 순회
                if not visited[i]:
                    stack.append(i)
print()

# 그래프 예시
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]



dfs_stack(graph, 1)