import numpy as np

laser = [0.1, 0.2, 0.3, 0.4, 0.5]

laser_arr = np.array(laser)
result = np.count_nonzero(laser_arr >= 0.2)
print(result)