import os
import pymysql

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")        
PASSWORD = os.getenv("DB_PASSWORD")  
DB_NAME = os.getenv("DB_NAME")