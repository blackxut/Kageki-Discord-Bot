from typing import Any, Dict, List, Tuple, Union
from dotenv import load_dotenv
from os import getenv
import mysql.connector
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
RowItemType = Any
RowType = Tuple[RowItemType, ...]  # a row as a variable-length tuple of values

# loeading env file 
load_dotenv(dotenv_path='.env')

# retrieve all the attributes needed
MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")

# MySQL Configuration
db_config = {"user": MYSQL_USER,"password": MYSQL_PASSWORD,"database": MYSQL_DATABASE}

def createConnector():
    """
    Method used to initialize a connection with the MySQL local server
    """
    try:
        # call the connect() method to start the connection
        connector = mysql.connector.connect(**db_config)
        return connector
    except mysql.connector.Error as err:
        # in any case of error, we print the issue
        print(f"Error while connecting to MySQL : {err}")
        # return None to raise no Error for the others methods
        return None

def requestQuery(query:str) -> List[Union[RowType, Dict[str, RowItemType]]]:
    connector = createConnector()
    if connector is None:
        return None
    try:
        # initialize a cursor to interact with the database
        cursor = connector.cursor()
        # execute the SQL query
        cursor.execute(query)
        # retrive all the result from the query
        return cursor.fetchall()
    except mysql.connector.Error as err:
        # in any case of error, we print the issue
        print(f"Error during the request : {err}")
        return None
    finally:
        # we close the cursor and connector at the end
        if connector.is_connected():
            cursor.close()
            connector.close()

# GETTERS

def getVersion():
    """
   Request the current version of MySQL used
    """
    return requestQuery("SELECT VERSION();")

def getLeaderboard():
    """
    Request the current Leaderboard stored in the table 'users'
    """
    return requestQuery("SELECT username, score FROM Users ORDER BY score;")

# SETTERS