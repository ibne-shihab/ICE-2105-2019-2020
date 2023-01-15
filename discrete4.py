V = 4
INF=999999999999
def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min( dist[i][j] ,dist[i][k] + dist[k][j])
    printSolution(dist)  

def printSolution(dist):
	print("Following matrix shows the shortest distances between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if (dist[i][j] == INF):
				print("%7s" % ("INF"), end=" ")
			else:
				print("%7d\t" % (dist[i][j]), end=' ')
			if j == V-1:
				print()
if __name__ == "__main__":""
graph = [[7, 5, INF, INF],
         [7, INF, INF, 2],
         [INF, 3, INF, INF],
         [4, INF, 1, INF]
         ]

floydWarshall(graph)