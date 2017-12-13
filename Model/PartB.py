import random
from Model.Med_MCplay import Med_Test


class partb():
    def __init__(self, lvla, lvlb, times):
        from View.Board_GUI import chalWindow
        self.chalWindow = chalWindow()
        self.lvla = lvla
        self.lvlb = lvlb
        self.times = times
        """
        board
        """
        self.board = list('---------')

    #         print(self.lvla,self.lvlb)
    #         print(self.board)

    def single_game(self, board):
        board = self.board[:]
        m = board.count('-')
        while m > 0:
            if m % 2 == 1:
                # print(self.lvla) ##
                if self.lvla == 'easy':
                    self.easy(board)
                    m = board.count('-')
                elif self.lvla == 'medium':
                    self.medium(board)
                    m = board.count('-')
                elif self.lvla == 'hard':
                    self.hard(board)
                    m = board.count('-')

            if (m % 2 == 0) & (m != 0):
                # print(self.lvlb) ##
                if self.lvlb == 'easy':
                    self.easy(board)
                    m = board.count('-')
                elif self.lvlb == 'medium':
                    self.medium(board)
                    m = board.count('-')
                elif self.lvlb == 'hard':
                    self.hard(board)
                    m = board.count('-')

                            # print(board)
        if self.isWinner(board) == 1:
            state = 'w';
        elif self.isDraw(board) == 1:
            state = 'd';
        # elif Med_Test.isDraw(self, board) == 1:
        #     state = 'd';
        elif self.isLost(board) == 1:
            state = 'l';
        # print(state)
        return state

    def selection(self, board, n):
        """
        This is the selection. turn the move selected into effect.
        """
        if board[n] == '-':
            m = board.count('-')
            if m % 2 == 0:
                board[n] = '0'
            else:
                board[n] = 'X'
                #     else:
                #         print("The position has already been occupied")
        return board

    def easy(self, board):
        pc = [i for i, j in enumerate(board) if j == '-']
        move = random.choice(pc)
        self.selection(board, move)
        #         board = self.selection(board, move)
        #         board.pop(0)
        #         m = board.count('-')
        # print(board)##
        return board

    def medium(self, board):
        pc = [i for i, j in enumerate(board) if j == '-']
        (w2, l2, d2) = Med_Test.MC_trail(self, self.board, pc,1000, [0] * 9, [0] * 9, [0] * 9)
        # print(w2,l2,d2)
        move = Med_Test.auto_selection(self, w2, l2, d2)
        while move not in pc:
            move = Med_Test.auto_selection(self, w2, l2, d2)
        # move = random.choice(pc)
        self.selection(board, move)
        #         board.pop(0)
        #         m = board.count('-')
        # print(board)##
        return board

    def hard(self, board):
        pc = [i for i, j in enumerate(board) if j == '-']

        # pc = self.chooseRandomMoveFromList(self.board)
        """
        here is the bug
        """
        from Model.Hard_MCplay import Hard_Test
        self.Hard_Test=Hard_Test()
        (w2, l2, d2) = self.Hard_Test.MC_trail(self.board, pc, 1000, [0] * 9, [0] * 9, [0] * 9)
        move =self.Hard_Test.auto_selection(w2, l2, d2)

        while move not in pc:
            move = self.Hard_Test.auto_selection(w2, l2, d2)

        # move = random.choice(pc)
        self.selection(board, move)
        #         board.pop(0)
        #         m = board.count('-')
        # print(board)##
        return board


    def isWin(self, board):
        """
        GIven a board checks if it is in a winning state.
        Arguments:
              board: a list containing X,O or -.
        Return Value:
               True if board in winning state. Else False
        """
        #  check if any of the rows has winning combination
        for i in range(3):
            if (
                            len(set(board[i * 3:i * 3 + 3])) is 1 and
                            board[i * 3] is not '-'
            ):
                return True

        # check if any of the Columns has winning combination
        for i in range(3):
            if (
                            (board[i] is board[i + 3]) and
                            (board[i] is board[i + 6]) and
                            board[i] is not '-'
            ):
                return True

        # 2,4,6 and 0,4,8 cases
        # diagonal
        if (
                            board[0] is board[4] and
                            board[4] is board[8] and
                        board[4] is not '-'
        ):
            return True

        if (
                            board[2] is board[4] and
                            board[4] is board[6] and
                        board[4] is not '-'
        ):
            return True

        return False
    #
    def isWinner(self, board):
        """
            This is to define the status of "isWin" (for X).

            >>> bb=['X', 'X', 'X', '-', 'X', 'O', '-', 'O', 'O']
            >>> print(isWin(bb))
            True
            """
        if (
                        self.isWin(board) is True and
                            board.count('-') % 2 == 0
        ):
            return True

        return False

    def isDraw(self, board):
        """
        This is to define the status of "isDraw".

        >>> bb=['X', 'X', 'O', 'O', 'X', 'X', 'X','O', 'O']
        >>> print(isDraw(bb))
        True
        """
        if (
                        self.isWin(board) is False and
                        board.count('-') == 0
        ):
            return True

        return False

    def isLost(self, board):
        if (
                        self.isWin(board) is True and
                            board.count('-') % 2 == 1
        ):
            return True

        return False

    def notFinished(self, board):
        """
            This is to define the status of "notFinish".

            >>> b=['X', 'X', 'O', 'X', '-', '-', '-', '-', 'O']
            >>> print(notFinish(b))
            False
            """
        if (
                        self.isWin(board) is False and
                        board.count('-') != 0
        ):
            return True

        return False

    def MC_games(self):
        #         times=self.times
        st_list = []
        x = 0
        #         print(self.times)
        while x < self.times:
            s = self.single_game(self.board)
            st_list.append(s)
            x += 1

        # print(st_list)
        #         print(st_list.count('w'),st_list.count('d'),st_list.count('l'))
        win = st_list.count('w') / self.times
        draw = st_list.count('d') / self.times
        lose = st_list.count('l') / self.times
        return win,draw,lose


