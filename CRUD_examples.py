import pandas as pd
import math
from cassandra.cluster import Cluster, BatchStatement, ConsistencyLevel
cluster = Cluster()
session = cluster.connect('crime')

# Simple sql limiting to 10
# df = session.execute("select * from crime_2016 limit 10")
# Simple sql limiting filter by the state of "NEW YORK"
df = session.execute("select * from crime_2016 where state = 'NEW YORK' limit 10")
#df = session.execute("select * from crime_2016 where city = 'New York'")

for row in df:
    print(row)

cluster.shutdown()