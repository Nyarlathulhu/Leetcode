# RELATED TOPICS:
# Array | Hash Table | String | Breadth-First Search

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        next_num = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        queue = collections.deque([("0000", 0)])
        visited = {"0000"} | set(deadends)
        while queue:
            code, step = queue.popleft()
            if code == target:
                return step
            for i in range(len(code)):
                for n in next_num[code[i]]:
                    new_code = code[:i] + n + code[i+1:]
                    if new_code not in visited:
                        visited.add(new_code)
                        queue += [(new_code, step + 1)]
        return -1
    
