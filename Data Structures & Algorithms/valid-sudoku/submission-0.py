class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            my_set = set()
            new_set = set()
            for j in range(len(board[i])):
                if board[i][j] in my_set and board[i][j] != ".":
                    return False
                my_set.add(board[i][j])
                
                if board[j][i] in new_set and board[j][i] != ".":
                    return False
                new_set.add(board[j][i]) 

        k = 3
        for p in range(k):
            my_set = set()
            my_set1 = set()
            my_set2 = set()
            for i in range(k):
                
                for j in range(k):
                    if (board[i][j + k *p] in my_set and board[i][j + k *p] !=".") or (board[i+k][j + k *p] in my_set1 and board[i+k][j + k *p] != ".") or (board[i+k+k][j + k *p] in my_set2 and board[i+k+k][j + k *p] != "."):
                        print("D")
                        return False
                    print(board[i][j + k *p])
                    my_set.add(board[i][j + k *p])
                    my_set1.add(board[i+k][j + k*p])
                    my_set2.add(board[i+k+k][j + k*p])



        

        return True
