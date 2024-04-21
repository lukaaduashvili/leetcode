class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = []
        for i in range(numCourses):
            adj_list.append([])

        for i in range(len(prerequisites)):
            curr_node = prerequisites[i][0]
            req_node = prerequisites[i][1]

            neighbors = adj_list[curr_node]
            neighbors.append(req_node)

        visited = set()

        def dfs(curr):
            if curr in visited:
                return False

            if adj_list[curr] == []:
                return True

            visited.add(curr)

            for course in adj_list[curr]:
                if not dfs(course):
                    return False
            adj_list[curr] = []
            visited.remove(curr)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True