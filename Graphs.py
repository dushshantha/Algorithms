import collections

def can_team_a_beat_team_b(matches, team_a, team_b):

    def build_graph():
        graph = collections.defaultdict(set)

        for match in matches:
            graph[match[0]].add(match[1])
        print(graph)
        return graph

    def isReachable(graph, curr, dest, visited = set()):
        if curr == dest:
            return True
        
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)

        return any(isReachable(graph, team, dest, visited) for team in graph[curr])
    
    return isReachable(build_graph(), team_a, team_b)

if __name__ == "__main__":
    matches = [[1,3], [1,4], [3,5], [2, 7]]
    print(can_team_a_beat_team_b(matches, 1, 7))
