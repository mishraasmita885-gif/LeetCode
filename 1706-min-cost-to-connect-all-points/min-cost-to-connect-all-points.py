
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = [float('inf')] * n
        visited = [False] * n

        dist[0] = 0
        total = 0

        for _ in range(n):
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i

            visited[u] = True
            total += dist[u]

            for v in range(n):
                if not visited[v]:
                    cost = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])

                    dist[v] = min(dist[v], cost)

        return total
