import numpy as np

maps = []

# random map
map = np.random.randint(6, size=(6, 5)).tolist()
maps.append(map)

# map_1 : U
map = [ [5, 4, 3, 2, 1],
        [4, 3, 2, 1, 0],
        [5, 4, 3, 2, 1],
        [5, 2, 5, 1, 0],
        [1, 1, 2, 5, 1],
        [1, 2, 5, 1, 0] ]
maps.append(map)

# map_2
# map_3
