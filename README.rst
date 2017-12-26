it enables sql files to be imported as python modules.

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
- You have to make `__init__.py` at a directory which sql files have been placed on.
- And write like the following to the `__init__.py`:

  .. code:: python

     ## if using django:
     # from django.db import connection

     import os
     from sql_importer import initialize
     initialize(os.path.dirname(__file__), globals(), connection, sql_type='postgresql')

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
    sql.sum_sales.execute(sales_from=date(2017, 5, 22), sales_to=date(2017, 12, 26))

- Now `sql_type` argument allows `postgresql`.

  - If you want to use the other sql_type, please make the issue on https://github.com/beproud/sql-importer.

Contributors
============
- aodag ( https://github.com/aodag )
- crohaco ( https://github.com/righ )

Links
=====
- https://github.com/beproud/sql-importer
- https://pypi.python.org/pypi/sql-importer
