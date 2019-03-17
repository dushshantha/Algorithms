def populateQueue(nodes):
    g = {}

    for node in nodes:
        if not node[0] in g:
            g[node[0]] = [node[1]]
        else:
            g[node[0]].append(node[1])
        
        if not node[1] in g:
            g[node[1]] = [node[0]]
        else:
            g[node[1]].append(node[0])
    return g

def bfs(g, start):
    q = []
    visited = []
    ret = []
    q.append(start)
    n = start

    while(len(q) > 0): 
        n = q.pop(0)
        if(n != None and not n in visited):
            ret.append(n)
            for c in g[n]:
                q.append(c)
        visited.append(n)
    return ret

def shortestPath(g, start, end):
    q = []
    visited = []
    path = []
    q.append(start)
    n = start
    lengths = [1]
    level = 0
    ret = 999

    while(len(q) > 0):
        i = lengths[level]
        print(q)
        
        while i > 0:
            i -= 1
            n = q.pop(0)
            if i == 0:
                level += 1

            if( n != None and not n in visited):
                path.append(n)
                if n == end:
                    ret = min(ret, level)
                for c in g[n]:
                    q.append(c)
                lengths.append(len(g[n]))
            visited.append(n)
        
    return ret

def shortestPathDistance(g, start, end):
    q = []
    edge_distance = 1
    lengths = {}

    q.append(start)
    lengths[start] = 0

    while q:
        parent = q.pop(0)
        for item in g[parent]:
            if item == end:
                return lengths[parent] + edge_distance
            if item not in lengths:
                lengths[item] = lengths[parent] + edge_distance
                q.append(item)

    return -1

def getShortestPath(g, start, end):
    q = [start]
    parentOf = {}
    parentOf[start] = None

    while q:
        parent = q.pop(0)
  
        for child in g[parent]:
            if child not in parentOf:
                parentOf[child] = parent
                q.append(child)
                if child == end:
                    return getPath(child, parentOf)
            
    return []

def getPath(end, parentOf):
    ret = [end]
    parent = parentOf[end]
    while parent:
        ret.append(parent)
        parent = parentOf[parent]
    
    return ret[::-1]


def dfs(g, start, path, visited):
    if start in visited:
        return path
    path.append(start)
    visited.append(start)

    for child in g[start]:
        dfs(g, child, path, visited)
    return path

def countClusters(nodes):
    g = populateQueue(nodes)
    count = 0
    visited = []
    clusters = []
    for i in g.keys():
        cluster = dfs(g,i,[],visited)
        if len(cluster) >= 2:
            clusters.append(cluster)
            count += 1
    print(clusters)
    return count

if __name__ == "__main__":
    nodes = [[1,2], [1,3], [2,6], [2,5], [3,4], [4,6],[7,8], [7,9], [10,11]]
    g = populateQueue(nodes)
    print(g)
    print(bfs(g, 1))
    print(dfs(g,1,[],[]))
    print('Clusters :', countClusters(nodes))
    print('Shortest Path Between 1, 6')
    print(shortestPath(g, 1, 6))
    print('Shortest Path Between 1, 4')
    print(shortestPath(g, 1, 4))

    print('Shortest Path Between 1, 6')
    print(shortestPathDistance(g, 1, 6))
    print(getShortestPath(g,1,6))
    print('Shortest Path Between 1, 4')
    print(shortestPathDistance(g, 1, 4))
    print(getShortestPath(g,1,4))
    print('Shortest Path Between 1, 8')
    print(shortestPathDistance(g, 1, 8))
    print(getShortestPath(g,1,8))




    