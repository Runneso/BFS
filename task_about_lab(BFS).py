def BFS(pole, queue):
    if not queue:
        return
    point = queue.pop(0)
    row, col = point
    if col - 1 >= 0 and pole[row][col - 1] == 0:
        pole[row][col - 1] = pole[row][col] + 1
        queue.append((row, col - 1))
    if row - 1 >= 0 and pole[row - 1][col] == 0:
        pole[row - 1][col] = pole[row][col] + 1
        queue.append((row - 1, col))
    if col + 1 < len(pole[0]) and pole[row][col + 1] == 0:
        pole[row][col + 1] = pole[row][col] + 1
        queue.append((row, col + 1))
    if row + 1 < len(pole) and pole[row + 1][col] == 0:
        pole[row + 1][col] = pole[row][col] + 1
        queue.append((row + 1, col))
    BFS(pole, queue)


def solve(pole, exitpoint):
    row, col = exitpoint
    if pole[row][col] == 0:
        return [(row, col)]
    if col - 1 >= 0 and pole[row][col - 1] == pole[row][col] - 1:
        return solve(pole, (row, col - 1)) + [(row, col)]
    if row - 1 >= 0 and pole[row - 1][col] == pole[row][col] - 1:
        return solve(pole, (row - 1, col)) + [(row, col)]
    if col + 1 < len(pole[0]) and pole[row][col + 1] == pole[row][col] - 1:
        return solve(pole, (row, col + 1)) + [(row, col)]
    if row + 1 < len(pole) and pole[row + 1][col] == pole[row][col] - 1:
        return solve(pole, (row + 1, col)) + [(row, col)]


if __name__ == "__main__":
    lab = []
    n = int(input())
    for i in range(n):
        row = str(input()).split(" ")
        row = list(map(int, row))
        lab.append(row)
    pole = []
    for row in lab:
        pole.append(row.copy())
    BFS(pole, [(0, 0)])
    pole[0][0] = 0
    for row in pole:
        s = " ".join(map(str, row)).replace("-1", "□")
        print(s)
    print(solve(pole, (5, 5)))

# lab
# 0 -1 -1 0 0 0
# 0 0 0 0 -1 0
# -1 0 -1 0 0 -1
# 0 0 0 -1 0 -1
# 0 -1 0 -1 0 0
# 0 0 0 -1 0 0
