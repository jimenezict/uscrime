import pandas as pd
import math
from cassandra.cluster import Cluster, BatchStatement, ConsistencyLevel
cluster = Cluster(['10.0.2.15'],port=9042)
session = cluster.connect('crime')

crime = pd.ExcelFile('CrimeList.xls')
df1 = crime.parse('16tbl06',header = 3)
df = pd.DataFrame(df1)

previous_state = df["State"].iloc[0]
print(list(df.columns.values))

def normalizeInt(colValue):
    if (isinstance(colValue,float) and math.isnan(colValue)):
        return int(0)
    return int(colValue)

def insert_crime(df):
    sql_insert = """
        INSERT INTO crime_2016 (
            state,city,population,violent,murder,rape1,
            rape2,robery, aggreavated, property_, burglary, 
            larceny, vehicle_theft, arson
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)        
    """
    session.execute(sql_insert,df)

for index, row in df.iterrows():
    if isinstance(row['City'],str):
        if isinstance(row['State'],str):
            previous_state = row['State']
        data = [
            previous_state,
            row['City'],
            normalizeInt(row['Population']),
            normalizeInt(row['Violent\ncrime']),
            normalizeInt(row['Murder and\nnonnegligent\nmanslaughter']),
            normalizeInt(row['Rape\n(revised\ndefinition)1']),
            normalizeInt(row['Rape\n(legacy\ndefinition)2']),
            normalizeInt(row['Robbery']),
            normalizeInt(row['Aggravated\nassault']),
            normalizeInt(row['Property\ncrime']),
            normalizeInt(row['Burglary']),
            normalizeInt(row['Larceny-\ntheft']),
            normalizeInt(row['Motor\nvehicle\ntheft']),
            normalizeInt(row['Arson3'])
            ]
        print(str(index) + ":" +str(data))
        insert_crime(data)

cluster.shutdown()