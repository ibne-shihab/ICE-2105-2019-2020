def color_node(graph):
    color_map = {}
    for node in sorted(graph, key=lambda x: len(graph), reverse=True):
        neighbours_colors = set(color_map.get(neigh) for neigh in graph[node])
        color_map[node] = next(color for color in range(
            len(graph)) if color not in neighbours_colors)
    return color_map


graph = {'a': list('bcdg'), 'b': list('acde'), 'c': list('abefg'),
         'd': list('abeg'), 'e': list('bcdfgh'), 'f': list('ech'),
         'g':list('daech'),'h':list('gef')
         }

print(color_node(graph))
