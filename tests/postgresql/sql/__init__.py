# coding: utf-8
import os

import psycopg2
from sql_importer import init

host = os.environ.get('POSTGRES_HOST', 'db')
connection = psycopg2.connect("host={host} user=postgres".format(host=host))
init(os.path.dirname(__file__), globals(), connection, sql_type='postgresql')
