import mysql.connector

def define_env(env):
    print("--- define_env is started now ---")

    db_config = {
        "host": "db4free.net",
        "database": "pbhitanshu",          # Must match your db4free username
        "user": "hitanshu",              # Your db4free username
        "password": "Warmachine",        # Your db4free password
        "port": 3306
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT variable_name, variable_value FROM sop_variables WHERE is_active = 1")

    env.variables['vars'] = {}
    for row in cursor.fetchall():
        env.variables['vars'][row['variable_name']] = row['variable_value']

    cursor.close()
    conn.close()
    print("--- define_env is finished now ---")
