import random
import math
import matplotlib.pyplot as plt

NUM_PEOPLE = 50
AREA_SIZE = 100
RADIUS = 10
THRESHOLD = 5

people = []
for _ in range(NUM_PEOPLE):
    x = random.randint(0, AREA_SIZE)
    y = random.randint(0, AREA_SIZE)
    people.append((x, y))

danger_zones = []
for p in people:
    count = 0
    for q in people:
        if math.dist(p, q) <= RADIUS:
            count += 1
    if count >= THRESHOLD:
        danger_zones.append(p)

x, y = zip(*people)
if danger_zones:
    dx, dy = zip(*danger_zones)
else:
    dx, dy = [], []

plt.scatter(x, y)
plt.scatter(dx, dy, color="red")
plt.title("AI Event Safety Simulation")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()
