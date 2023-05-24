#part 1
#referred to AOC reddit pages

with open("day15.txt") as file:
    day15_data = file.read().strip().split("\n")

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
beacons = []

for line in day15_data:
    parts = line.split(" ")
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    sensors.append((sx, sy))
    beacons.append((bx, by))

n = len(sensors)
distances = []

for i in range(n):
    distances.append(distance(sensors[i], beacons[i]))

m = 2000000
inters = []

for i, s in enumerate(sensors):
    dx = distances[i] - abs(s[1] - m)
    if dx <= 0:
        continue
    inters.append((s[0] - dx, s[0] + dx))
canx = []
for bx, by in beacons:
    if by == m:
        canx.append(bx)
minx = min([i[0] for i in inters])
maxx = max([i[1] for i in inters])
res = 0
for x in range(minx, maxx + 1):
    if x in canx:
        continue
    for left, right in inters:
        if left <= x <= right:
            res += 1
            break
print(res)

#part 2

with open("day15.txt") as file:
    day15_data = file.read().strip().split("\n")

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors = []
beacons = []

for line in day15_data:
    parts = line.split(" ")
    sx = int(parts[2][2:-1])
    sy = int(parts[3][2:-1])
    bx = int(parts[8][2:-1])
    by = int(parts[9][2:])
    sensors.append((sx, sy))
    beacons.append((bx, by))

n = len(sensors)
distances = []

for i in range(n):
    distances.append(distance(sensors[i], beacons[i]))

pos_lines = []
neg_lines = []

for i, s in enumerate(sensors):
    d = distances[i]
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

pos = None
neg = None

for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        a, b = pos_lines[i], pos_lines[j]
        if abs(a - b) == 2:
            pos = min(a, b) + 1
        a, b = neg_lines[i], neg_lines[j]
        if abs(a - b) == 2:
            neg = min(a, b) + 1

x, y = (pos + neg) // 2, (neg - pos) // 2
res = x * 4000000 + y

print(res)

