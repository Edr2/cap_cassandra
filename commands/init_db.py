from cassandra.cluster import Cluster

cluster = Cluster(['cas1', 'cas2'], port=9042)
session = cluster.connect()

# points: zone_id text | point_date timestamp | device_uuid text | longitude float | latitude float | range_time text
# ,PRIMARY KEY ((zone_id, range_time), point_date)
# Descriptions: range_time = 1 hour
#
# infected_points: zone_id text | point_date timestamp | longitude float | latitude float | range_time text,
# ,PRIMARY KEY ((zone_id, range_time), point_date) ) WITH CLUSTERING ORDER BY (point_date ASC)
# Descriptions: range_time = 1 day
# 
# SELECT * FROM infected_points WHERE zone_id = ? and timestamp = ?

if __name__ == "__main__":
    session.execute("CREATE KEYSPACE IF NOT EXISTS gps_keyspace WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 }")
    session.execute('USE gps_keyspace')

    session.execute("CREATE TABLE IF NOT EXISTS points (zone_id text, point_date timestamp, device_uuid text, longitude float, latitude float, range_time text, PRIMARY KEY ((zone_id, range_time), point_date));")
    session.execute("CREATE TABLE IF NOT EXISTS infected_points (zone_id text, point_date timestamp, longitude float, latitude float, range_time text, PRIMARY KEY ((zone_id, range_time), point_date)) WITH CLUSTERING ORDER BY (point_date ASC);")
else:
    session.execute('USE gps_keyspace')