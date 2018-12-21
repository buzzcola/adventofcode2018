from collections import Counter


def parse_scan(line):
    is_x = line[0] == "x"
    start, range = line.split(", ")
    start = int(start.split("=")[1])
    range1, range2 = range[2:].split("..")
    return is_x, start, int(range1), int(range2)


def get_bounds(scans):
    min_x = 9999
    max_x = 0
    min_y = 9999
    max_y = 0

    for is_x, s, t1, t2 in scans:
        if is_x:
            min_x = min(s, min_x)
            max_x = max(s, max_x)
            min_y = min(t1, min_y)
            max_y = max(t2, max_y)
        else:
            min_x = min(t1, min_x)
            max_x = max(t2, max_x)
            min_y = min(s, min_y)
            max_y = max(s, max_y)

    return min_x, max_x, min_y, max_y


# searches x values in a given direction until it hits a wall or overflows
# if it overflows, add the overflow point as a new water source
def search(x, y, dir, grid, sources):
    while True:
        below = grid[y + 1][x]
        cur = grid[y][x]
        # if we hit a wall, go back 1 and return no overflow
        if cur == '#':
            x -= dir
            return x, False
        # if the tile below is empty, then we have overflown and we have
        # created a new water source
        if below == '.':
            sources.append((x, y))
            return x, True
        # if the current tile and the tile below is a stream, then we have
        # overflown into an existing stream, no need to add a new source
        if cur == '|' and below == '|':
            return x, True
        x += dir


def solve(lines):
    scans = [parse_scan(line) for line in lines]

    min_x, max_x, min_y, max_y = get_bounds(scans)

    # add buffer x values for overflows on edge buckets
    min_x -= 1
    max_x += 1

    # build empty grid
    grid = []
    for y in range(max_y + 1):
        row = []
        for x in range(max_x - min_x + 1):
            row.append('.')
        grid.append(row)

    # populate the buckets
    for is_x, s, t1, t2 in scans:
        for r in range(t1, t2 + 1):
            x = s if is_x else r
            y = r if is_x else s
            grid[y][x - min_x] = '#'

    # get initial water source
    ix, iy = 500 - min_x, 0

    # create a queue of water sources
    sources = [(ix, iy)]
    while sources:
        # get the latest water source and ensure that it hasn't been replaced
        # with still water
        x, y = sources.pop()
        if grid[y][x] == '~':
            continue

        # follow the stream down by incrementing the y variable. Once we hit a
        # wall we then fill it up a level at a time by searching for a wall or
        # an overflow both left and right. If there were no overflows, fill
        # with still water, else fill with moving water
        y += 1
        while y <= max_y:
            cell = grid[y][x]
            if cell == '.':
                grid[y][x] = '|'
                y += 1
            elif cell == '#' or cell == '~':
                y -= 1
                left, left_overflow = search(x, y, -1, grid, sources)
                right, right_overflow = search(x, y, 1, grid, sources)
                is_overflow = left_overflow or right_overflow
                for x_ in range(left, right + 1):
                    grid[y][x_] = '|' if is_overflow else '~'
            elif cell == '|':
                break

    # DEBUG: Output flow to file
    # f = open("test_out.txt", "w")
    # for row in grid:
    #     f.write(''.join(row) + '\n')

    counts = Counter(cell for row in grid[min_y:] for cell in row)
    print(counts['~'] + counts['|'])
    print(counts['~'])


INPUT = open("input").read()
solve(INPUT.split("\n"))