import oracledb
import os
from dotenv import load_dotenv

oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_0")

load_dotenv()
connection = oracledb.connect(
    user=os.getenv("ORACLE_USER"),
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=os.getenv("ORACLE_DSN"))

print("Successfully connected to Oracle Database")

cursor = connection.cursor()
for result in cursor.execute("SELECT * FROM LAYER1"):
    print(result)