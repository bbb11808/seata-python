#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from rm.datasource.sql.struct.TableRecords import TableRecords


class MySQLInsertExecutor(object):


    def __int__(self, cursor_proxy, cursor_callback, sql_recoginzer):
        self.cursor_proxy = cursor_proxy
        self.cursor_callback = cursor_callback
        self.sql_recoginzer = sql_recoginzer

    def before_image(self):
        return TableRecords.empty(self.get_table_meta())

    def after_image(self, before_image):
        pass

    def execute(self, args):
        pass

    def get_table_meta(self):
        self.sql_recoginzer.get_table_name()
        pass


