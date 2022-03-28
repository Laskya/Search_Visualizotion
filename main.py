import pygame
from time import sleep

# Clicking R only when paused restarts the algorithm
# Clicking R when algorithm is reseted clears the grid
# SPACE pauses algorithm
# Left Click adds (start, end, wall) in this order if you delete start it will firstly create a start node
# Right Click deletes stuff
# Drawing is enabled when the algorithm has ended
# When there is no solution algorithm restarts

SIZE = 1280  # for later use
GRID_SIZE = SIZE - 200
CELL_WIDTH = 30
CELLS = GRID_SIZE // CELL_WIDTH
REAL_GRID_SIZE = GRID_SIZE + CELLS
WINDOW = pygame.display.set_mode((REAL_GRID_SIZE, REAL_GRID_SIZE))

SLEEP = 0.1  # seconds to wait between steps
WALL = (0, 0, 0)  # WALL
EMPTY = (255, 255, 255)  # EMPTY
CURRENT = (0, 51, 102)  # CURRENT NODE
START = (172, 207, 66)  # START
END = (172, 55, 18)  # END
NEIGHBOR = (76, 201, 240)  # NEIGHBOR BEING CHECKED
CHECKED = (128, 128, 128)  # CHECKED
PATH = (255, 255, 0)  # PATH
SET = (104, 95, 171)  # TO BE CHECKED


class Cell:
    def __init__(self, row, column):
        self.color = EMPTY
        self.row = row
        self.column = column
        self.g = float('inf')
        self.h = 0
        self.f = float('inf')
        self.neighbors = []

    def get_coord(self):
        return self.row, self.column

    def get_neighbors(self, grid):
        if self.row > 0 and grid[self.row - 1][self.column].color != WALL:
            self.neighbors.append(grid[self.row - 1][self.column])

        if self.column < CELLS - 1 and grid[self.row][self.column + 1].color != WALL:
            self.neighbors.append(grid[self.row][self.column + 1])

        if self.row < CELLS - 1 and grid[self.row + 1][self.column].color != WALL:
            self.neighbors.append(grid[self.row + 1][self.column])

        if self.column > 0 and grid[self.row][self.column - 1].color != WALL:
            self.neighbors.append(grid[self.row][self.column - 1])


def create_grid(rows, columns):
    grid = []
    for row in range(rows):
        grid.append([])
        for column in range(columns):
            grid[row].append(Cell(row, column))

    return grid


def draw_grid(grid):
    for row in grid:
        for cell in row:
            pygame.draw.rect(WINDOW, cell.color,
                             (cell.row * CELL_WIDTH + 1 * cell.row, cell.column * CELL_WIDTH + 1 * cell.column,
                              CELL_WIDTH, CELL_WIDTH))
    pygame.display.update()


def draw_cell(row, column, color):
    pygame.draw.rect(WINDOW, color,
                     (row * CELL_WIDTH + 1 * row, column * CELL_WIDTH + 1 * column, CELL_WIDTH,
                      CELL_WIDTH))
    pygame.display.update()


def draw_cell_static(grid, row, column, color):
    cell = grid[row][column]
    cell.color = color
    pygame.draw.rect(WINDOW, cell.color,
                     (cell.row * CELL_WIDTH + 1 * cell.row, cell.column * CELL_WIDTH + 1 * cell.column, CELL_WIDTH,
                      CELL_WIDTH))
    pygame.display.update()


def draw_path(current, came_from):
    while current in came_from:
        current = came_from[current]
        row, column = current.get_coord()
        draw_cell(row, column, PATH)


def reset_data(grid):
    for row in grid:
        for cell in row:
            cell.f = float('inf')
            cell.g = float('inf')


def reset_grid(grid):
    for row in grid:
        for cell in row:
            cell.color = EMPTY
            pygame.draw.rect(WINDOW, cell.color,
                             (cell.row * CELL_WIDTH + 1 * cell.row, cell.column * CELL_WIDTH + 1 * cell.column,
                              CELL_WIDTH, CELL_WIDTH))
    pygame.display.update()


def a_star(grid, start, end):
    reset_data(grid)
    draw_grid(grid)
    open_set = [start]
    came_from = {}
    start.f = get_h(start, end)
    start.g = 0
    old_current = 0
    old_neighbor = 0
    stop = False

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = True

                    while stop:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    stop = False
                                elif event.key == pygame.K_r:
                                    return True

        open_set = sorted(open_set, key=lambda cell: cell.f)

        current = open_set[0]
        open_set.pop(0)

        if old_neighbor and old_neighbor != end:
            sleep(SLEEP)
            draw_cell(old_neighbor.row, old_neighbor.column, SET)

        if old_current and old_current != start and old_current != end:
            sleep(SLEEP)
            draw_cell(old_current.row, old_current.column, CHECKED)

        if current != start and current != end:
            sleep(SLEEP)
            draw_cell(current.row, current.column, CURRENT)

        elif current == end:
            draw_path(end, came_from)
            draw_cell_static(grid, end.row, end.column, END)
            draw_cell_static(grid, start.row, start.column, START)
            return came_from

        current.get_neighbors(grid)

        for neighbor in current.neighbors:
            temp_g = current.g + 1

            if temp_g < neighbor.g:
                came_from[neighbor] = current
                neighbor.g = temp_g
                neighbor.f = temp_g + get_h(neighbor, end)
                if neighbor not in open_set:
                    open_set.append(neighbor)
                    sleep(SLEEP)
                    draw_cell(neighbor.row, neighbor.column, NEIGHBOR)

                    if old_neighbor and old_neighbor != end:
                        draw_cell(old_neighbor.row, old_neighbor.column, SET)
                    elif old_neighbor == end:
                        draw_cell_static(grid, end.row, end.column, END)
                    old_neighbor = neighbor

        old_current = current

    return True


def get_h(cell, end):
    row1, column1 = cell.get_coord()
    row2, column2 = end.get_coord()

    return abs(row1 - row2) + abs(column1 - column2)


def main():
    grid = create_grid(CELLS, CELLS)
    draw_grid(grid)
    first = True
    drawing = True
    start = None
    end = None

    while drawing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if start is not None and end is not None:
                        returned = a_star(grid, start, end)
                        if returned == True:
                            draw_grid(grid)
                        elif returned:
                            first = False


                elif event.key == pygame.K_r:
                    start = None
                    end = None
                    reset_grid(grid)

            if pygame.mouse.get_pressed()[0]:
                if not first:
                    draw_grid(grid)
                x, y = pygame.mouse.get_pos()
                column = y // (CELL_WIDTH + 1)
                row = x // (CELL_WIDTH + 1)
                if x < GRID_SIZE + CELLS and y < GRID_SIZE + CELLS:
                    if start is None and end != grid[row][column] and grid[row][column].color != WALL:  # START NODE
                        start = grid[row][column]
                        draw_cell_static(grid, row, column, START)
                    elif end is None and start != grid[row][column] and grid[row][column].color != WALL:  # END NODE
                        end = grid[row][column]
                        draw_cell_static(grid, row, column, END)
                    elif end != grid[row][column] and start != grid[row][column]:  # WALL
                        draw_cell_static(grid, row, column, WALL)

            elif pygame.mouse.get_pressed()[2]:  # RESETS BLOCK / RIGHT CLICK
                if not first:
                    draw_grid(grid)
                x, y = pygame.mouse.get_pos()
                if x < GRID_SIZE + CELLS and y < GRID_SIZE + CELLS:
                    column = y // (CELL_WIDTH + 1)
                    row = x // (CELL_WIDTH + 1)
                    draw_cell_static(grid, row, column, EMPTY)
                    if grid[row][column] == start:
                        start = None
                    elif grid[row][column] == end:
                        end = None


main()
