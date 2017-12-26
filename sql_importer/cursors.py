# -*- coding:utf-8 -*-


def dict_cursor(cursor):
    for row in cursor:
        out = {}
        for i, col in enumerate(cursor.description):
            out[col[0]] = row[i]
        yield out


def query_dict(connection, sql, params={}):
    cur = connection.cursor()
    cur.execute(sql, params)
    cur = dict_cursor(cur)
    return cur
