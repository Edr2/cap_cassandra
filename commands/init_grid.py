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

width_devide_num = round(width_points_distance / GRID_BY)
height_devide_num = round(height_points_distance / GRID_BY)

cols = np.linspace(bottom_left[1], bottom_right[1], num=width_devide_num)
rows = np.linspace(bottom_left[0], top_left[0], num=height_devide_num)

def get_zone_id(longitude: float, latitude: float) -> str:
    col_num = str(np.searchsorted(cols, longitude))
    row_num = str(np.searchsorted(rows, latitude))

    return col_num + '-' + row_num

if __name__ == "__main__":
    print(get_zone_id(34.7730261824675, 32.0759398737466))