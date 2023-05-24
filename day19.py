#referred to AOC reddit pages

#part 1

import re
with open('day19.txt', 'r') as file:
    day19_data = file.readlines()
    bprints = [bprint.strip() for bprint in day19_data] 
bprint_int = list()

for bprint in bprints:
    ints = [int(ii) for ii in re.findall(r'\d+', bprint)]
    bprint_int.append(ints)

def qass(state):
    tmins, (robots, iv, mined) = state
    return 1000 * mined[3] + 100 * mined[2] + 10 * mined[1] + mined[0]

def rfs(costs, robots, ntmins, maxqueue = 30000):
    queue = list()
    queue.append((0, (robots, (0, 0, 0, 0), (0, 0, 0, 0))))
    maxgsmined = 0
    d = 0
    while queue: 
        tmins, (robots, oldiv, mined) = queue.pop(0)
        if tmins > d:
            queue.sort(key = qass, reverse = True)
            queue = queue[:maxqueue]
            d = tmins
        if tmins == ntmins:
            maxgsmined = max(maxgsmined, mined[3])
            continue 
        newiv = tuple([oldiv[ii] + robots[ii] for ii in range(4)])
        new_mined = tuple([mined[ii] + robots[ii] for ii in range(4)])
        queue.append((tmins + 1, (robots, newiv, new_mined)))
        for ii in range(4): 
            cost_robot = costs[ii]
            if all([oldiv[jj] >= cost_robot[jj] for jj in range(4)]):
                new_robots = list(robots)
                new_robots[ii] += 1
                new_robots = tuple(new_robots)
                newivstate = tuple([newiv[jj] - cost_robot[jj] for jj in range(4)])
                queue.append((tmins + 1, (new_robots, newivstate, new_mined)))
    return maxgsmined

maxtmins = 24 
sumquality = 0

for bprintid, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in bprint_int:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = rfs(cost_per_robot, (1, 0, 0, 0), maxtmins, maxqueue = 1000)
    sumquality += num_mined * bprintid

print(sumquality)

#part 2

maxtmins = 32 
product_geodes = 1

for bprintid, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in bprint_int[:3]:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = rfs(cost_per_robot, (1, 0, 0, 0), maxtmins, maxqueue = 10000)
    product_geodes *= num_mined

print(product_geodes)

