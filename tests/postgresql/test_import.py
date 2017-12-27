# coding: utf-8

import pytest


@pytest.fixture
def sql():
    from . import sql as _sql
    return _sql


def test_insert(sql):
    sql.insert.execute(name='apple', price=100)
    sql.insert.execute(name='orange', price=50)
    expected = [{'name': 'apple', 'price': 100}, {'name': 'orange', 'price': 50}]
    actual = list(sql.select.query())
    assert expected == actual


def test_delete(sql):
    sql.insert.execute(name='apple', price=100)
    sql.insert.execute(name='orange', price=50)
    sql.delete.execute(name='apple')
    expected = [{'name': 'orange', 'price': 50}]
    actual = list(sql.select.query())
    assert expected == actual


def test_update(sql):
    sql.insert.execute(name='apple', price=100)
    sql.update.execute(name='apple', price=300)
    expected = [{'name': 'apple', 'price': 300}]
    actual = list(sql.select.query())
    assert expected == actual
