
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

DB_CONFIG = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'Asd45678910!',
    'port': 5432
}

SQL_FILE_PATH = r"c:\Users\junio\OneDrive\Área de Trabalho\FBD\API-Pinheiro\sql\create_database_complete.sql"

def create_database():
    print("Connecting to 'postgres' database to create 'arena_pinheiro'...")
    try:
        # Connect to default DB to create new DB
        conn = psycopg2.connect(dbname='postgres', **DB_CONFIG)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        
        # Check if DB exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'arena_pinheiro'")
        exists = cur.fetchone()
        
        if not exists:
            print("Database 'arena_pinheiro' does not exist. Creating...")
            cur.execute("CREATE DATABASE arena_pinheiro")
            print("Database 'arena_pinheiro' created successfully.")
        else:
            print("Database 'arena_pinheiro' already exists.")
            
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error creating database: {e}")
        return False

def run_sql_script():
    print("Connecting to 'arena_pinheiro' to run SQL script...")
    try:
        conn = psycopg2.connect(dbname='arena_pinheiro', **DB_CONFIG)
        cur = conn.cursor()
        
        print(f"Reading SQL file: {SQL_FILE_PATH}")
        with open(SQL_FILE_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        print("Executing SQL script...")
        cur.execute(sql_script)
        conn.commit()
        
        print("SQL script executed successfully. Tables created.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error executing SQL script: {e}")

if __name__ == "__main__":
    if create_database():
        run_sql_script()
