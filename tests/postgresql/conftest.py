# coding: utf-8
import pytest


@pytest.fixture(autouse=True, scope='module')
def init():
    from . import sql
    sql.drop_table.execute()
    sql.create_table.execute()


@pytest.fixture(autouse=True, scope='function')
def clear():
    from . import sql
    sql.clear.execute()
