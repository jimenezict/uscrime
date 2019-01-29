import pandas as pd
import math
from cassandra.cluster import Cluster, BatchStatement, ConsistencyLevel
cluster = Cluster()
session = cluster.connect('crime')

# Simple sql limiting to 10
session.execute("DROP KEYSPACE crime")
session.execute("CREATE KEYSPACE crime WITH replication = {'class':'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE crime")
session.execute("""CREATE TABLE crime_2016 ( 
    state text,
    city   text, 
    population int,
    violent           int, 
    murder            int, 
    rape1          int, 
    rape2         int, 
    robery        int, 
    aggreavated  int, 
    property_       int, 
    burglary          int, 
    larceny         int, 
    vehicle_theft    int,
    arson int,
    PRIMARY KEY (state,city) 
) """)

cluster.shutdown()