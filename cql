DROP KEYSPACE crime;
CREATE KEYSPACE crime 
WITH replication = {'class':'SimpleStrategy', 'replication_factor': 1};
USE crime;
CREATE TABLE crime_2016 ( 
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
    PRIMARY KEY ((state, city),population) 
) 
WITH CLUSTERING ORDER BY (population DESC);
