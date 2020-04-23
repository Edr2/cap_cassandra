import csv
import os
from datetime import datetime
from init_db import session
from tools import get_zone_id


def fill_points(folder_path: str):
    try:
        folder_path = os.path.abspath(folder_path)
        join = os.path.join
        files = [join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(join(folder_path, f))]

        for file_name in files:
            with open(file_name, 'r') as f:
                reader = csv.reader(f)

                next(reader)  # This skips the 1st in csv row which is the header.
                for record in reader:
                    if not record:
                        continue

                    record_i = iter(record)
                    timepoint = next(iter(record_i), None)
                    longitude = next(iter(record_i), None)
                    longitude = float(longitude)
                    latitude = next(iter(record_i), None)
                    latitude = float(latitude)
                    event_name = file_name.split('/')[-1]

                    if timepoint:
                        timepoint = datetime.fromtimestamp(float(timepoint[:10]))

                    zone_id = get_zone_id(longitude, latitude)
                    # one day
                    range_time = timepoint.strftime('%Y-%m-%d')


                    query_insert = "INSERT INTO infected_points (zone_id, point_date, longitude, latitude, range_time)"\
                        "VALUES (?, ?, ?, ?, ?)"
                    prepared = session.prepare(query_insert)

                    session.execute(prepared, (zone_id, timepoint, longitude, latitude, range_time))
            break
        return True
    except (Exception) as e:
        # should be logger here
        print(e)


if __name__ == '__main__':
    folder_path = os.path.abspath('./travel_logs')
    fill_points(folder_path)