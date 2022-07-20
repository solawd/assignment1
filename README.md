## Install Requirements
Run `pip install -r requirements.txt` to install the libraries needed for the project

## Setup
Ensure that there is a local instance of postgres running with the following in place:
1. A database named `sparkifydb`
2. The dabase should be accesible with by a user named `student` with pasword `student`

## Run project
Run `python etl.py` to load data from the `data` folder into the DB