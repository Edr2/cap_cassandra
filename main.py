from cassandra.cluster import Cluster


if __name__ == "__main__":
    cluster = Cluster(['cas1', 'cas2'], port=9042)
    session = cluster.connect()

    session.execute("CREATE KEYSPACE IF NOT EXISTS test_keyspace WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 }")
    session.execute('USE test_keyspace')

    session.execute("CREATE TABLE IF NOT EXISTS users (username text,name text,age int,PRIMARY KEY(username));")
    session.execute("INSERT INTO users(username,name,age) VALUES ('aali24','Ali Amin',34);")
    session.execute("INSERT INTO users(username,name,age) VALUES ('jack01','Jack David',23);")
    session.execute("INSERT INTO users(username,name,age) VALUES ('ninopk','Nina Rehman',34);")
    

    rows = session.execute('SELECT * FROM users')
    for row in rows:
        print(row.age,row.name,row.username)