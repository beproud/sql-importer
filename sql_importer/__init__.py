# -*- coding:utf-8 -*-

""" This is a hook for importing sql files. """

import os
import re

from .cursors import query_dict
from . import loaders


def init(basedir, exports, connection, sql_type="postgresql", import_ext=".sql"):
    loader = getattr(loaders, sql_type).SQLLoader(basedir)
    for sql_file in os.listdir(basedir):
        name, ext = os.path.splitext(sql_file)
        if ext != import_ext:
            continue
        sql = loader.load_sql(name)
        exports[name] = SQLFunction(sql, connection, name)


def find_placeholders(sql):
    """ SQL中の ``%(name)s`` 形式のプレースホルダーを探しだして名前のイテレータを返す"""
    return (m.groupdict()["varname"]
            for m in re.finditer(r'%\((?P<varname>\w+)\)s', sql))


class SQLFunction(object):
    def __init__(self, sql, connection, name, preprocessor=None):
        self.sql = sql
        self.connection = connection
        self.preprocessor = preprocessor
        self.name = name

    def check_args(self, var_names, kwargs):
        for v in var_names:
            if v not in kwargs:
                raise TypeError('keyword argument "%s" is not found' % v)

    def query(self, **kwargs):
        sql = self.sql
        if self.preprocessor:
            sql = self.preprocessor(self.sql, kwargs)
        var_names = list(find_placeholders(sql))
        self.check_args(var_names, kwargs)
        return query_dict(self.connection, sql, kwargs)

    def execute(self, **kwargs):
        sql = self.sql
        if self.preprocessor:
            sql = self.preprocessor(self.sql, kwargs)
        var_names = list(find_placeholders(sql))
        self.check_args(var_names, kwargs)
        cur = self.connection.cursor()
        cur.execute(sql, kwargs)
        return cur.rowcount
