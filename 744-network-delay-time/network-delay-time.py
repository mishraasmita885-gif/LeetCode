
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        answer = max(dist[1:])

        return answer if answer != float('inf') else -1
