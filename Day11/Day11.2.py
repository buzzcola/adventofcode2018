import itertools
serial_number = 18

def power_level((x,y), serial_number):
    rack_id = x + 10
    start = ((rack_id * y) + serial_number) * rack_id
    digit = 0 if start < 100 else int(str(start)[-3])
    return digit - 5

grid_size = 300
points = [(x,y) for y, x in itertools.product(range(1,grid_size + 1), range(1,grid_size + 1))]
sums = {}

for (x,y) in points:
    left_sum = 0 if x == 1 else sums[(x-1,y)]
    top_sum = 0 if y == 1 else sums[(x, y-1)]
    top_left_sum = 0 if (x == 1 or y == 1) else sums[(x-1, y-1)]
    score = power_level((x,y), serial_number)
    sums[(x,y)] = score + left_sum + top_sum - top_left_sum

(best_point, best_score, best_size) = (None, None, None)
for sample_size in range(4,301):
    samples = [p for p in points if p[0] <= grid_size - sample_size + 1 and p[1] <= grid_size - sample_size + 1]
    for point in samples:
        (left, top, right, bottom) = (point[0], point[1], point[0] + sample_size - 1, point[1] + sample_size - 1)
        score = sums[(right, bottom)] - sums[(left, bottom)] - sums[(right, top)] + sums[(left, top)]
        if not best_score or score > best_score:
            (best_point, best_score, best_size) = (point, score, sample_size)
            print '(%s, %s, %s): score = %s' % (point[0], point[1], best_size, best_score)
