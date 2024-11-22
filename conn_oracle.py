import os

import oracledb
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("ORACLE_USER")
password = os.getenv("ORACLE_PASSWORD")
hostname = os.getenv("ORACLE_HOSTNAME")
sid = os.getenv("ORACLE_SID")

print(username, password, hostname, sid)

connection = oracledb.connect(user=username, password=password, host=hostname, sid=sid)

cursor = connection.cursor()


query = """
SELECT * FROM  RECIPE

"""
iterador = cursor.execute(query)
for result in iterador:
    print(result)


connection.commit()

cursor.close()

connection.close()
