import os
from cassapp.commands.csv_to_db_points import fill_points


if __name__ == "__main__":
    folder_path = os.path.abspath('./travel_logs')
    fill_points(folder_path)