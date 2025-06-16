import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import random

height = 120
width = 120
aDiffRate = 1
bDiffRate = 0.5
feedRate = 0.192
killRate = 0.192
dT =1 # 2 makes bizare spirally dna patterns
dx = 1
aChem = 0
bChem = 0
initBConc = 8
epochs = 540
avgConc = 0



grid = np.zeros((height,width), dtype=np.bool)
next_state = np.zeros((height,width), dtype=np.bool)
##for i in range(initBConc): #This is the number of time an initial amount of chemical B is placed
##    bConc[random.randint(10,width-10),random.randint(10,height-10)] = 1
x=16
y=39
pulsar_offsets = [
    (0, 2), (0, 3), (0, 4), (0, 8), (0, 9), (0, 10),
    (2, 0), (3, 0), (4, 0), (2, 5), (3, 5), (4, 5), (2, 7), (3, 7), (4, 7), (2, 12), (3, 12), (4, 12),
    (5, 2), (5, 3), (5, 4), (5, 8), (5, 9), (5, 10),
    (7, 2), (7, 3), (7, 4), (7, 8), (7, 9), (7, 10),
    (8, 0), (9, 0), (10, 0), (8, 5), (9, 5), (10, 5), (8, 7), (9, 7), (10, 7), (8, 12), (9, 12), (10, 12),
    (12, 2), (12, 3), (12, 4), (12, 8), (12, 9), (12, 10)
]

for dx, dy in pulsar_offsets:
    grid[x + dx, y + dy] = 1



for i in range(40,65,4):
  x = i
  y = 50
#glider
  grid[x, y] = 1
  grid[x + 1, y + 1] = 1
  grid[x + 2, y - 1] = 1
  grid[x + 2, y] = 1
  grid[x + 2, y + 1] = 1

x=60
y=70
grid[x, y] = 1
grid[x + 1, y + 1] = 1
grid[x + 2, y - 1] = 1
grid[x + 2, y] = 1
grid[x + 2, y + 1] = 1

x=65
y=75
grid[x, y] = 1
grid[x + 1, y + 1] = 1
grid[x + 2, y - 1] = 1
grid[x + 2, y] = 1
grid[x + 2, y + 1] = 1

x=85
y=75
grid[x, y] = 1
grid[x + 1, y + 1] = 1
grid[x + 2, y - 1] = 1
grid[x + 2, y] = 1
grid[x + 2, y + 1] = 1

x = 30
y = 30
#toad
grid[x, y] = 1
grid[x, y + 1] = 1
grid[x, y + 2] = 1
grid[x + 1, y - 1] = 1
grid[x + 1, y] = 1
grid[x + 1, y + 1] = 1

x=30
y=70
#LWSS
offsets = [(0, 1), (0, 3), (1, 0), (2, 0), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
for dx, dy in offsets:
    grid[x + dx, y + dy] = 1

x=40
y=20

offsets = [(0, 1), (0, 3), (1, 0), (2, 0), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
for dx, dy in offsets:
    grid[x + dx, y + dy] = 1

x=70
y=30


offsets = [(0, 4), (0, 5), (1, 4), (1, 5), (10, 4), (10, 5), (10, 6), (11, 3), (11, 7),
           (12, 2), (12, 8), (13, 2), (13, 8), (14, 5), (15, 3), (15, 7), (16, 4), (16, 5),
           (16, 6), (17, 5), (20, 2), (20, 3), (20, 4), (21, 2), (21, 3), (21, 4), (22, 1),
           (22, 5), (24, 0), (24, 1), (24, 5), (24, 6), (34, 2), (34, 3), (35, 2), (35, 3)]
for dx, dy in offsets:
    grid[x + dx, y + dy] = 1


def upscale(grid, factor):
    """
    Upscale a grid by a specified factor. Each cell in the grid is represented as a factor x factor block.

    :param grid: The grid to be upscaled.
    :param factor: The scaling factor.
    :return: An upscaled grid.
    """
    return np.repeat(np.repeat(grid, 4, axis=0), factor, axis=1)

# Your existing Game of Life setup and logic here
# ...

def count_neighbours(x, y):
    neighbors = [
        (x-1, y-1), (x-1, y), (x-1, y+1),
        (x, y-1),             (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
    ]
    count = 0
    for i, j in neighbors:
        if 0 <= i < height and 0 <= j < width:
            count += grid[i, j]
    return count


for reps in range(epochs):
    next_state.fill(0)  # Reset next_state at the beginning of each epoch
    for i in range(1, height-1):
        for j in range(1, width-1):
            live_neighbours = count_neighbours(i, j)
            if grid[i, j] == 1 and live_neighbours in [2, 3]:
                next_state[i, j] = 1  # Live cell remains alive
            elif grid[i, j] == 0 and live_neighbours == 3:
                next_state[i, j] = 1  # Dead cell becomes alive

    grid = np.copy(next_state)  # Update the grid state

    # Upscale and convert the grid for visualization
    upscaled_grid = upscale(grid, 4)  # Upscale each cell to 4x4 pixels
    printstate = upscaled_grid * 255
    print("1")
    cv2.imwrite(f'D:/Users/Jack Critchley/Desktop/GrayScott/saved_img_{reps}.png', printstate)
