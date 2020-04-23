from cassandra.cluster import Cluster

cluster = Cluster(['cas1', 'cas2'], port=9042)
session = cluster.connect()