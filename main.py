import mysql.connector

def define_env(env):
    print("--- define_env started ---")

    import mysql.connector
    db_config = {
        "host": "127.0.0.1",
        "database": "pbbuddyhitanshu",
        "user": "root",
        "password": "Hitanshu"
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT variable_name, variable_value FROM sop_variables WHERE is_active = 1")

    # Set variables under env.variables['vars']
    env.variables['vars'] = {}
    for row in cursor.fetchall():
        env.variables['vars'][row['variable_name']] = row['variable_value']

    cursor.close()
    conn.close()
    print("--- define_env finished ---")
