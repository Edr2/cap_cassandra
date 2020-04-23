import numpy as np
from geopy.distance import distance

GRID_BY = 500 # meters

# Israel in rectangle (latitude, longitudes)
top_left = (33.262374, 33.918799)
top_right = (33.262374, 35.918799)
bottom_left = (29.362374, 33.918799)
bottom_right = (29.362374, 35.918799)

width_points_distance = distance(bottom_left, bottom_right).m
height_points_distance = distance(bottom_left, top_left).m

WIDTH_DEVIDE_NUM = round(width_points_distance / GRID_BY)
HEIGHT_DEVIDE_NUM = round(height_points_distance / GRID_BY)

cols = np.linspace(bottom_left[1], bottom_right[1], num=WIDTH_DEVIDE_NUM)
rows = np.linspace(bottom_left[0], top_left[0], num=HEIGHT_DEVIDE_NUM)

def get_zone_id(longitude: float, latitude: float) -> str:
    col_num = str(np.searchsorted(cols, longitude))
    row_num = str(np.searchsorted(rows, latitude))

    return col_num + '-' + row_num

def neighbors(x: float, y: float, append_x_y: bool=True) -> list:
    neighbors_list = [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= WIDTH_DEVIDE_NUM and
                                   -1 < y <= HEIGHT_DEVIDE_NUM and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= WIDTH_DEVIDE_NUM) and
                                   (0 <= y2 <= HEIGHT_DEVIDE_NUM))]
    if append_x_y:
        neighbors_list.append((x, y))

    return neighbors_list