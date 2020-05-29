import os
import csv
import json
import boto3
import click
import dotenv
import psycopg2
import psycopg2.extras
from glob import glob
from pprint import pprint
from loguru import logger

dotenv.load_dotenv()

@click.command()
@click.option('--data_file_path', type=str, required=True, help='absolute path of dir containing files and meta files')
def main(data_file_path):

    SCHEMA_NAME = os.getenv('db_schema')
    CONN_STRING = "dbname={0} host={1} port={2} user={3} password={4} connect_timeout=300".format(
        os.getenv('db_name'),
        os.getenv('db_host'),
        os.getenv('db_port'),
        os.getenv('db_user'),
        os.getenv('db_pass'),
        )
    S3 = boto3.resource(
        's3', 
        aws_access_key_id=os.getenv('aws_access_key_id'),
        aws_secret_access_key=os.getenv('aws_secret_access_key'),
        region_name=os.getenv('region_name'),
        )

    # check for meta file
    tables_dict = {}
    meta_files = []
    for _file in glob(os.path.join(data_file_path, '*metadata.csv')):
        meta_files.append(_file)
    # for tables in meta
    for meta_file in meta_files:
        with open(meta_file) as r:
            csv_reader = csv.reader(r)
            headers = None
            for row in csv_reader:
                if headers is None:
                    headers = row
                    continue
                table_name = row[1]
                if table_name not in tables_dict:
                    tables_dict[table_name] = {}
                tables_dict[table_name]['filename'] = row[0]
                tables_dict[table_name]['abs_filename'] = os.path.join('/'.join(meta_file.split('/')[:-1]), row[0])
                if 'columns' not in tables_dict[table_name]:
                    tables_dict[table_name]['columns'] = []
                tables_dict[table_name]['columns'].append({
                    'name': row[2],
                    'type': row[3] if row[3] != 'int' else 'BIGINT',
                    'size': row[4],
                })
    # print(json.dumps(tables_dict, indent=2))

    # generate and execute table creation script
    for table, table_data in tables_dict.items():
        table_creation_sql = 'DROP TABLE IF EXISTS {0}.{1}; CREATE TABLE {0}.{1} (\n'.format(
            SCHEMA_NAME,
            table
        )
        for column in table_data['columns']:
            table_creation_sql += '"{}" {}{},\n'.format(
                column['name'],
                column['type'],
                '({})'.format(column['size']) if column['size'] not in ('', None) else '',
            )
        table_creation_sql = table_creation_sql.rstrip(',\n')
        table_creation_sql += '\n);'
        # print(table_creation_sql)
        with psycopg2.connect(CONN_STRING) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                logger.debug(table_creation_sql)
                cursor.execute(table_creation_sql)
    
        # upload file to s3
        logger.info('uploading file to s3 bucket: {}'.format(table_data['filename']))
        logger.info('size: {} bytes'.format(os.stat(table_data['abs_filename']).st_size))
        S3.Object(
            os.getenv('bucket_name'), 
            'tmp/{0}'.format(
                table_data['filename']
                )).put(Body=open(table_data['abs_filename'], 'rb')
            )

        # generate and execute copy command
        table_load_sql = 'COPY {}.{}\n('.format(
            SCHEMA_NAME,
            table
        )
        for column in table_data['columns']:
            table_load_sql += '"{}",'.format(
                column['name'],
            )
        table_load_sql = table_load_sql.rstrip(',')
        table_load_sql += ')\n'
        table_load_sql += 'FROM \'s3://{}/tmp/{}\'\n'.format(
            os.getenv('bucket_name'),
            table_data['filename'],
        )
        table_load_sql += 'CREDENTIALS \'aws_access_key_id={};aws_secret_access_key={}\'\n'.format(
            os.getenv('aws_access_key_id'),
            os.getenv('aws_secret_access_key'),
        )
        table_load_sql += '''
        DATEFORMAT 'auto' TIMEFORMAT 'auto'
        REGION '{}'
        FORMAT AS csv
        TRUNCATECOLUMNS
        delimiter ','
        ACCEPTINVCHARS IGNOREHEADER 1 EMPTYASNULL BLANKSASNULL NULL AS 'NULL'
        ;'''.format(
            os.getenv('aws_region')
        )
        with psycopg2.connect(CONN_STRING) as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                logger.debug(table_load_sql)
                cursor.execute(table_load_sql)
    

if __name__ == '__main__':
    main()