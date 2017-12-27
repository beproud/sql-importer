# coding: utf-8
import os

import psycopg2
from sql_importer import init

connection = psycopg2.connect("host=db user=postgres")
init(os.path.dirname(__file__), globals(), connection, sql_type='postgresql')
