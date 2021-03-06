#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from rm.datasource.sql.struct.KeyType import KeyType


class Row(object):

    def __init__(self):
        self.fields = []

    def add(self, field):
        self.fields.append(field)

    def primary_keys(self):
        keys = []
        for i in range(len(self.fields)):
            f = self.fields[i]
            if f.key_type == KeyType.PRIMARY_KEY:
                keys.append(f)
        return keys

    def non_primary_keys(self):
        keys = []
        for i in range(len(self.fields)):
            f = self.fields[i]
            if f.key_type != KeyType.PRIMARY_KEY:
                keys.append(f)
        return keys