#referred to AOC reddit pages

limit = 100000
total_space = 70000000
space = 30000000

lines = []
with open("day07.txt") as file:
    day7_data = file.readlines()

day07_data=[]
for line in day7_data:
    day07_data.append(line[:-1])

curr_dir = {}
root = {}
files = []
for l in day07_data:
    if l.startswith("$"):
        if "cd" in l:
            dir = l[5:]
            if dir == "/":
                curr_dir = root
                files = []
            elif dir == "..":
                curr_dir = files.pop()
            else:
                curr_dir[dir] = {}
                files.append(curr_dir)
                curr_dir = curr_dir[dir]
    else:
        size, file = l.split()
        if not size.startswith("dir"):
            curr_dir[file] = int(size)


# part1
def part1(dir):
    if isinstance(dir, int):
        return dir, 0
    size = 0
    result = 0
    for subdir in dir.values():
        s, r = part1(subdir)
        size += s
        result += r
    if size <= limit:
        result += size
    return size, result


print(part1(root)[1])

# part2
delete_space = part1(root)[0] - (total_space - space)


def part2(dir):
    result = 99999999999999
    if part1(dir)[0] >= delete_space:
        result = part1(dir)[0]
    for subdir in dir.values():
        if not isinstance(subdir, int):
            result = min(result, part2(subdir))
    return result


print(part2(root))
