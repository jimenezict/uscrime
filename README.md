# uscrime
This is a tutorial for those that wants to put his hand on a ETL for understanding Cassandra stacks.

Easy, let's use some crime statistics from the USA and let's analyze it a little bit.

But first of all
* Do you have Cassandra node already? here, how I learned and configured. Pease of cake.
* Nothig to complain, if you are here, it means that you have your IDE or Python environment. I was using 3.7 and PyCharm

About the files.
* CQL scripts for creating the keyspace and tables (it can be done from Python, as you wish, but this file will allow you to do it from the console)
* Keyspace_creation.py: As the one before but from Python
* CrimeList.xls: Raw data with the crimes
* Python with the ETL. Check out that some manipulations are done (guess which)
* CRUD_examples, indicates some CQL to consume the dataset from Cassandra database

Enjoy and don't hesitate to contact me in case of doubts.

Keep trying, keep learning, keep growing.

PD: in order to avoid you some console errors: install pandas, cassandra-drive and xlrd
