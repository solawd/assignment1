## Project Summary
This project loads data from 2 types of files :
1. files containing song information
2. log files containing user activity

The loaded information is then fed into a postgres database to help in analysing information about what songs users are listening to.

## Files
1. `create_tables.py` is used to create all the relational tables and the constraints necessary for storing the songs related data. (Tables will be deleted if they exist already)
2. `sql_queries.py` contains the SQL queries related to creation of tables and inserting and fetching of data
3. `etl.py` contains the logic for fetching the data from the files and populating the database with them

## How to run
#### Install Requirements
Run `pip install -r requirements.txt` to install the libraries needed for the project

#### Setup
Ensure that there is a local instance of postgres running with the following in place:
1. A database named `sparkifydb`
2. The dabase should be accesible with by a user named `student` with pasword `student`

#### Run project
Run `python create_tables.py` to create the needed tables. 
Run `python etl.py` to load data from the `data` folder into the DB