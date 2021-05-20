#!/usr/bin/python3

### Get date
from datetime import date

### Get time
from datetime import datetime

### For making the api call
import requests

### For mySQL functions
import mysql.connector

### For script delay
import time

### Process the json api response
import json

### Analyze the har file
from haralyzer import HarPage

### Get configuration from environment variables
import os
tg_host     = os.getenv('MYSQL_DB_HOST', "Value does not exist")
tg_db       = os.getenv('MYSQL_DATABASE', "Value does not exist")
tg_port     = os.getenv('MYSQL_DB_PORT', "Value does not exist")
tg_user     = os.getenv('MYSQL_USER', "Value does not exist")
tg_password = os.getenv('MYSQL_PASSWORD', "Value does not exist")
# tg_api_key  = os.getenv('TG_API_KEY', "Value does not exist")

tg_website_name = os.getenv('TG_WEBSITE_NAME', "Value does not exist")
tg_website_url  = os.getenv('TG_WEBSITE_URL', "Value does not exist")

mydb = mysql.connector.connect(port=tg_port, host=tg_host,user=tg_user,password=tg_password, database=tg_db)
cursor = mydb.cursor()

api_key = os.getenv('TG_API_KEY', "Value does not exist")
sql_websites = "SELECT * FROM tg_websites"
cursor.execute(sql_websites)
records = cursor.fetchall()
for row in records:
    clientid = str(row[0])
    name = str(row[1])
    c_url = str(row[2])
    print(clientid, name, c_url)