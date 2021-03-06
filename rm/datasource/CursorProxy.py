#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class CursorProxy(object):

    def __init__(self, connection_proxy, target_cursor, target_sql=None):
        self.connection_proxy = connection_proxy
        self.target_sql = target_sql
        self.target_cursor = target_cursor

    @property
    def description(self):
        """
        * name
        * type_code
        display_size
        internal_size
        precision
        scale
        null_ok
        """
        return self.target_cursor.description

    @property
    def rowcount(self):
        return self.target_cursor.rowcount

    # override Cursor callproc
    def callproc(self, procname, parameters=None):
        return self.target_cursor.callproc(procname, parameters)

    # override Cursor close
    def close(self):
        return self.target_cursor.close()

    # override Cursor executor
    def execute(self, operation, parameters=None):
        self.target_sql = operation
        return self.target_cursor.execute(operation, parameters)

    # override Cursor executemany
    def executemany(self, operation, seq_of_parameters=None):
        return self.target_cursor.executemany(operation, seq_of_parameters)

    # override Cursor fetchone
    def fetchone(self):
        return self.target_cursor.fetchone()

    # override Cursor fetchmany
    def fetchmany(self, size=None):
        return self.target_cursor.fetchmany(size)

    # override Cursor fetchall
    def fetchall(self):
        return self.target_cursor.fetchall()

    # override Cursor nextset
    def nextset(self):
        return self.target_cursor.nextset()

    # override Cursor arraysize
    @property
    def arraysize(self):
        return self.target_cursor.arraysize

    # override Cursor setinputsizes
    def setinputsizes(self, sizes):
        return self.target_cursor.setinputsizes(sizes)

    # override Cursor setoutputsize
    def setoutputsize(self, size, column=None):
        return self.target_cursor.setinputsize(size, column)

    # connection
    @property
    def connection(self):
        return self.connection_proxy
