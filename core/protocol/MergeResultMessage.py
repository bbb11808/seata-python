#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class MergeResultMessage(MessageTypeAware):

    def __init__(self):
        self.msgs = []

    def get_type_code(self):
        return MessageType.TYPE_SEATA_MERGE_RESULT