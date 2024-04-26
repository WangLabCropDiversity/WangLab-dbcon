import getpass
import psycopg2


def database_connection(**kwargs):
    '''
    Establishes a connection to the database using the credentials provided in the DATABASE_CREDENTIALS section of the config_load.yml file.
    
    Args:
        config_load_file_name (str): Name of the configuration file.
        item_DATABASE_CREDENTIALS (str): Key specifying the database credentials in the configuration file.
        **kwargs: Additional parameters for the database connection.
            Example: dbname, user, password, host, port, etc.
    
    Returns:
        connection (psycopg2.extensions.connection): Connection object to the PostgreSQL database.
        cursor (psycopg2.extensions.cursor): Cursor object for executing SQL commands.
    '''

    # Prompt the user to enter the password if not provided in kwargs
    password = kwargs.get('password') or getpass.getpass("Enter the database password: ")

    # Construct the connection string
    DB_CONNECTION_STRING = ''
    for key, value in kwargs.items():
        if key != 'password':
            DB_CONNECTION_STRING += f'{key.lower()}={value} '

    # Add the password to the connection string
    DB_CONNECTION_STRING += f'password={password}'

    ### Open database connection
    try: 
        connection = psycopg2.connect(DB_CONNECTION_STRING)
        print("Connection created!")
    except psycopg2.Error as e: 
        print("Error: Could not make connection to the Postgres database")
        print(e)
        return None, None

    try: 
        cursor = connection.cursor()
        print("Cursor obtained!")
    except psycopg2.Error as e: 
        print("Error: Could not get cursor")
        print(e)
        connection.close()
        return None, None

    connection.set_session(autocommit=True)
    
    return connection, cursor


def describe_table(cursor, table_name):
    '''
    Retrieves and prints the structure of a given table.
    
    Args:
        cursor (psycopg2.extensions.cursor): Cursor object for executing SQL commands.
        table_name (str): Name of the table.
    '''

    try:

        sql = 'SELECT column_name, data_type FROM information_schema.columns WHERE table_name = ' + "'" + table_name  + "'" + ' ORDER BY ordinal_position'

        cursor.execute(sql)

        columns = cursor.fetchall()

        print('---------------------------------------')

        print('Table: ' + table_name)

        print('---------------------------------------')

        print('column_name | data_type')

        print('---------------------------------------')    

        for row in columns:

            print("{}".format(row[0]) + " | {}".format(row[1]))

    except psycopg2.Error as e: 
            
        print("Error: issue executing sql statement")
        print (e)