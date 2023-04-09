import pygame

board = \
    [[8, 0, 4, 0, 0, 2, 0, 0, 0],
     [6, 0, 0, 1, 0, 9, 0, 0, 0],
     [0, 0, 7, 3, 6, 0, 0, 0, 0],
     [0, 3, 0, 0, 0, 0, 9, 0, 0],
     [0, 2, 0, 0, 1, 0, 0, 6, 0],
     [0, 0, 1, 0, 0, 0, 0, 3, 0],
     [0, 0, 0, 0, 3, 7, 4, 0, 0],
     [0, 0, 0, 5, 0, 8, 0, 0, 6],
     [0, 0, 0, 9, 0, 0, 2, 0, 5]]


class Board:
    def __init__(self):
        self.board = \
    [[8, 0, 4, 0, 0, 2, 0, 0, 0],
     [6, 0, 0, 1, 0, 9, 0, 0, 0],
     [0, 0, 7, 3, 6, 0, 0, 0, 0],
     [0, 3, 0, 0, 0, 0, 9, 0, 0],
     [0, 2, 0, 0, 1, 0, 0, 6, 0],
     [0, 0, 1, 0, 0, 0, 0, 3, 0],
     [0, 0, 0, 0, 3, 7, 4, 0, 0],
     [0, 0, 0, 5, 0, 8, 0, 0, 6],
     [0, 0, 0, 9, 0, 0, 2, 0, 5]]

    def return_instance(self):
        return self.board


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode([540, 540])
        self.surface.fill((225, 225, 225))
        pygame.display.flip()
        self.board_instance = Board()
        self.new_board = self.board_instance.return_instance()
        print(self.new_board)

    def display(self, bo):

        for i in range(len(bo)):
            pygame.draw.line(self.surface, (0, 0, 0), (i * 60, 0), (i * 60, 540), 1)

            if i % 3 == 0 and i != 0:
                pygame.draw.line(self.surface, (0, 0, 0), (0, ((i//3)*180)), (540, ((i//3)*180)), 3)

            for j in range(len(bo[0])):
                pygame.draw.line(self.surface, (0, 0, 0), (0, j * 60), (540, j * 60), 1)
                font = pygame.font.SysFont('calibri', 22)
                if self.new_board[i][j] != 0:
                    final_score = font.render(f"{bo[i][j]}", True, (255, 0, 0))
                else:
                    final_score = font.render(f"{bo[i][j]}", True, (0, 0, 0))
                self.surface.blit(final_score, (j * 60 + 25, i * 60 + 25))

                if j % 3 == 0 and j != 0:
                    pygame.draw.line(self.surface, (0, 0, 0), (((j // 3) * 180) + 1, 0), (((j // 3) * 180) + 1, 540), 3)
        pygame.display.flip()

    def valid(self,bo, num, pos):
        # check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # check column
        for i in range(len(bo[0])):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve(self, bo):
        find = self.find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(bo, i, (row, col)):
                bo[row][col] = i
                self.surface.fill((225, 225, 225))
                game.display(board)

                if self.solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if (bo[i][j]) == 0:
                    return i, j

        return None


if __name__ == '__main__':
    game = Game()
    game.solve(board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
