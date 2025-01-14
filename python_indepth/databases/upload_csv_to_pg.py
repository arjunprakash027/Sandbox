"""
Author : Arjun Prakash
Last Edited : 12-01-25

A python cli script to upload a csv file into postgres
"""

import argparse
import csv
import psycopg2
from psycopg2 import sql
from pathlib import Path

def upload_to_pg(csv_file:str, db_url:str, table_name:str = 'random', schema_name:str='public'):
    
    conn: psycopg2.extensions.connection = psycopg2.connect(db_url)
    cursor: psycopg2.extensions.cursor = conn.cursor()

    csv_file: Path = Path(csv_file)
    with csv_file.open(mode='r') as file:
        reader: csv.reader = csv.reader(file)
        headers: list[str] = next(reader)

        create_schema: sql.Composed = sql.SQL(
            """
            CREATE SCHEMA IF NOT EXISTS {schema}
            """
        ).format(
            schema = sql.Identifier(schema_name)
        )
        cursor.execute(create_schema)

        # We have to create the table first and therefore 
        create_table_query: sql.Composed = sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS {schema}.{table_name} (
            {columns}
            )
            """
        ).format(
            schema = sql.Identifier(schema_name),
            table_name = sql.Identifier(table_name),
            columns = sql.SQL(", ").join(
                [sql.Identifier(header) + sql.SQL(" TEXT") for header in headers]
            )
        )

        #print(f"Executing query: {create_table_query.as_string(conn)}")
        cursor.execute(create_table_query)

        insert_query: sql.Composed = sql.SQL (
            """
            INSERT INTO {schema}.{table} ({fields})
            VALUES ({placeholders})
            """
        ).format(
            schema = sql.Identifier(schema_name),
            table = sql.Identifier(table_name),
            fields = sql.SQL(", ").join(map(sql.Identifier, headers)),
            placeholders = sql.SQL(", ").join(sql.Placeholder() for _ in headers),
        )
        
        for row in reader:
            cursor.execute(insert_query, row)
        
        conn.commit()
        #print(sql.SQL("INSERT INTO {whatever}").format(whatever=sql.SQL("inter into whatver ").join([sql.Identifier("kl"), sql.Identifier("kj")])).as_string(conn))
        #print(insert_query.as_string(conn))
            
        #conn.commit()



if __name__ == '__main__':
    csv_file = "/mnt/d/projects/personal_projects/Statistella_Data_Analytics_Competition/statistella/train.csv"
    db_url = 'postgresql://postgres:1234@192.168.29.231:5432/datasets'

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Upload a csv file to be uplaoded into postgres")
    parser.add_argument("--csv_path",help='Location of the csv file')
    parser.add_argument("--db_url",help='URL for the postgres database')
    parser.add_argument("--table_name",help='name of the table to put this csv file into')
    parser.add_argument("--schema_name",default='public',help='name of the schema where you want to put this table into')

    args: argparse.Namespace = parser.parse_args()
    
    upload_to_pg(csv_file=args.csv_path,
                 db_url=args.db_url,
                 table_name=args.table_name,
                 schema_name=args.schema_name)