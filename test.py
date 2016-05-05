
import pymysql
import msvcrt
import time
import re
import random

# initiates variables for pymysql connection
connection = pymysql.connect(host="localhost",
user="root",
password="island",
db="quizbowl",
charset="utf8",
cursorclass=pymysql.cursors.DictCursor)

# initiates the cursor and then selects just questions from table and stores them in result.
cursor = connection.cursor()
sql_command = "SELECT Question, Answer FROM `terp 2 packet 1` ORDER BY rand()"
cursor.execute(sql_command)
rows = cursor.fetchall()
