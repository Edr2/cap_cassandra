from init_db import session

def save_point(longitude: float, latitude: float, point_date: float, event_name: str) -> bool:
    query_insert = "INSERT INTO infected_points (zone_id, point_date, longitude, latitude, range_time)"\
                        "VALUES (?, ?, ?, ?, ?)"
    prepared = session.prepare(query_insert)

    session.execute(prepared, (zone_id, timepoint, longitude, latitude, range_time))

if __name__ == '__main__':
    folder_path = os.path.abspath('./travel_logs')
    fill_points(folder_path)