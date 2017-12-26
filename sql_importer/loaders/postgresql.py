# -*- coding:utf-8 -*-

import os
import re
import io


class SQLLoader(object):
    """SQLファイルからSQLを読み込み、プレースホルダ―の形式変換を行う

    PostgreSQLのPSQLクライアントが利用するマクロ展開を
    DB API 2.0のプレースホルダ―形式に変換します
    パラメータ部分の変換を目的としているため、テーブル名部分の変換には対応していません。

    * ``:name`` -> %(name)s に変換
    * ``:'name'`` -> %(name)s に変換

    :param sql_base_path: str SQLファイルを検索するベースディレクトリパス
    """

    def __init__(self, sql_base_path):
        self.sql_base_path = sql_base_path

    def sql_file_path(self, name):
        """ SQLファイル名の取得 内部利用前提です。
        :param name: str ".sql"拡張子を除くファイル名
        :return: str ファイルパス
        """
        return os.path.join(self.sql_base_path, name + ".sql")

    def replace_placeholder(self, sql):
        """ プレースホルダ―の変換
        :param sql: str 変換対象のSQL文
        :return: str プレースホルダ―変換後のSQL文
        """
        sql = re.sub(r":'(\w+)'", r"%(\1)s", sql)
        sql = re.sub(r"(?<!:):([A-Za-z][0-9A-Za-z_]+)", r"%(\1)s", sql)
        return sql

    def load_sql(self, name, encoding='utf-8'):
        """ SQLの読み込み
        :param name: str SQLファイル名(.sql拡張子を除く)
        :return: str ファイルから読み込んだSQL文(プレースホルダ―変換済)
        """
        with io.open(self.sql_file_path(name), encoding=encoding) as f:
            sql = f.read()
            return self.replace_placeholder(sql)
