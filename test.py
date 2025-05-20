import mysql.connector

db_config = {
    "host": "127.0.0.1",
    "database": "pbbuddyhitanshu",
    "user": "root",
    "password": "Hitanshu"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM sop_variables LIMIT 5")
print(cursor.fetchall())
cursor.close()
conn.close()
