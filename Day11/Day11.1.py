import itertools, functools
serial_number = 4172

def power_level((x,y), serial_number):
    rack_id = x + 10
    start = ((rack_id * y) + serial_number) * rack_id
    digit = 0 if start < 100 else int(str(start)[-3])
    return digit - 5

grid_size = 300
points = ((x,y) for y, x in itertools.product(range(1,grid_size + 1), range(1,grid_size + 1)))
(best_point, best_score) = (None, None)

sample_size = 3
point_scan = (p for p in points if p[0] <= grid_size - sample_size + 1 and p[1] <= grid_size - sample_size + 1)
for point in point_scan:
    x_range = xrange(point[0], point[0] + sample_size)
    y_range = xrange(point[1], point[1] + sample_size)
    point_sample = ((x,y) for y, x in itertools.product(y_range, x_range))
    score = sum(power_level(p, serial_number) for p in point_sample)
    if not best_score or score > best_score:
        (best_point, best_score) = (point, score)

print 'point %s with score %s' % (best_point, best_score)