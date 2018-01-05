It enables SQL files to be imported as python modules.

.. image:: https://circleci.com/gh/beproud/sql-importer.svg?style=svg
    :target: https://circleci.com/gh/beproud/sql-importer

Requirements
============
- Python 2.7
- Python 3.6

Install
=======

.. code:: bash

  $ pip install sql-importer

Usage
=====
- You have to make `__init__.py` at the same directory which sql files have been placed on.
- And write like the following to the `__init__.py`:

  .. code:: python

     ## if using django:
     # from django.db import connection

     import os
     from sql_importer import init
     init(os.path.dirname(__file__), globals(), connection, sql_type='postgresql')

- That's all, you can import sql files (removed `.sql` suffix) as python modules.

  - Example: `testing/sql/sum_sales.sql` exists.

  .. code:: SQL

    SELECT SUM(price) AS sum_sales FROM sales
    WHERE
      sales_from >= :'sales_from'
      AND sales_to < :'sales_to'
    ;

  .. code:: python

    from datetime import date
    from testing import sql
    sql.sum_sales.query(sales_from=date(2017, 5, 22), sales_to=date(2017, 12, 26))

  - `sql` object has 2 methods, both method execute the sql and receive variables as keyword arguments.

    :query: It returns records. it expects only what has one or more results like `select` query.
    :execute: It returns number of records affected by the SQL.

- Now `sql_type` argument allows `postgresql`.

  - If you want to use the other sql_type, please make the issue on https://github.com/beproud/sql-importer .

Demo
====

start up
--------

.. code:: bash

  $ git clone git@github.com:beproud/sql-importer.git
  $ cd sql-importer
  $ docker-compose up


preparation
-----------

.. code:: bash

  $ docker exec -it sqlimporter_app_1 /bin/bash
  # python -m venv venv # only first time
  # source venv/bin/activate

Try
---

.. code:: bash

  (venv) # ls tests/postgresql/sql
  __init__.py  __init__.pyc  __pycache__	clear.sql  create_table.sql  delete.sql  drop_table.sql  insert.sql  select.sql  update.sql

   (venv) # python

.. code:: python

  >>> from tests.postgresql import sql
  >>> sql.
  sql.clear         sql.create_table  sql.drop_table    sql.init(         sql.os            sql.select
  sql.connection    sql.delete        sql.host          sql.insert        sql.psycopg2      sql.update

  >>> sql.create_table.execute()
  -1
  >>> sql.insert.execute(name='apple', price=100)
  1
  >>> list(sql.select.query())
  [{'name': 'apple', 'price': 100}]
  >>> sql.delete.execute(name='orange')
  0
  >>> sql.delete.execute(name='apple')
  1
  >>> list(sql.select.query())
  []

Unittest
--------

.. code:: bash

  (venv) # tox


- This library is tested by only latest `postgresql`.

Contributors
============
- aodag ( https://github.com/aodag )
- crohaco ( https://github.com/righ )

Links
=====
- https://github.com/beproud/sql-importer
- https://pypi.python.org/pypi/sql-importer
