# RELATED TOPICS:
# Array | Hash Table | Matrix

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(my_list, comp=['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            for i in range(len(my_list)):
                new_list = list(''.join(my_list[i]).replace('.', ''))
                my_set = set(new_list)
                if len(my_set) == len(new_list) and my_set.issubset(comp):
                    continue
                else:
                    return False
            return True
        
        def collectSubboxes(collects, box_size, left, right, target=board):
            collects.append(sum([target[n][m*box_size:(m+1)*box_size] for n in range(left*box_size, right*box_size)], []))
        
        rows = []
        cols = []
        sub_boxes = []
        
        for i in range(len(board)):
            rows.append([board[j][i] for j in range(len(board))])
            cols.append([board[i][j] for j in range(len(board))])
        
        box_size = 3
        for m in range(box_size):
            collectSubboxes(collects=sub_boxes, box_size=box_size, left=0, right=1)
            collectSubboxes(collects=sub_boxes, box_size=box_size, left=1, right=2)
            collectSubboxes(collects=sub_boxes, box_size=box_size, left=2, right=3)
        
        return isValid(rows) and isValid(cols) and isValid(sub_boxes)
  
