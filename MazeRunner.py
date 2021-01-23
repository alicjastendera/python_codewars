def maze_runner(maze, directions):
    point = [(index, row.index(2)) for index, row in enumerate(maze) if 2 in row]
    for move in directions:
        if move == "N":
            point = [(point[0][0] - 1, point[0][1])]
        if move == "S":
            point = [(point[0][0] + 1, point[0][1])]
        if move == "W":
            point = [(point[0][0], point[0][1] - 1)]
        if move == "E":
            point = [(point[0][0], point[0][1] + 1)]

        try:
            value = maze[point[0][0]][point[0][1]]
        except:
            return "Dead"

        if point[0][0] < 0 or point[0][1] < 0:
            return "Dead"
        if value == 3:
            return "Finish"
        if value == 1 :
            return "Dead"
    return "Lost"
