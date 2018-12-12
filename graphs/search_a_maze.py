WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
    # Perform dfs
    def search_maze_helper(curr):
        # check that curr is valid spot
        if not (0 <= curr.x < len(maze) and 0 <= curr.y < len(maze[curr.x]) and maze[curr.x][curr.y] == WHITE):
            return False
        path.append(curr)
        maze[curr.x][curr.y] = BLACK

        if curr == e:
            return True

        if any(
            map(search_maze_helper,
                (Coordinate(curr.x - 1, curr.y),
                 Coordinate(curr.x + 1, curr.y),
                 Coordinate(curr.x, curr.y - 1),
                 Coordinate(curr.x, curr.y + 1)))):
                 return True

        del path[-1]
        return False

    path = []
    if not search_maze_helper(s):
        return []
    return path
