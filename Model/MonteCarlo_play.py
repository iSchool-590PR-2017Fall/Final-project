class rule:
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

    def isWinner(self, board):
        """
            This is to define the status of "isWin" (for X).

            >>> bb=['X', 'X', 'X', '-', 'X', 'O', '-', 'O', 'O']
            >>> print(isWin(bb))
            True
            """
        if (
                        rule.isWin(self,board) is True and
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
                        rule.isWin(self,board) is False and
                        board.count('-') == 0
        ):
            return True

        return False

    def isLost(self, board):
        if (
                        rule.isWin(self,board) is True and
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
                        rule.isWin(self,board) is False and
                        board.count('-') != 0
        ):
            return True

        return False

    def check_win(self, player):
        if rule.isWin(self.board):
            if player is 'X':
                return -1
            else:
                return 1

        c = self.board.count('-')
        if c is 0:
            return 0
        return 2
