#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol import Version
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class RegisterRMRequest(MessageTypeAware):

    def __init__(self, application_id=None, transaction_service_group=None, extra_data=None):
        self.version = Version.CURRENT
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.extra_data = extra_data

        self.resource_ids = None

    def get_type_code(self):
        return MessageType.TYPE_REG_RM


class RegisterRMResponse(MessageTypeAware):

    def __init__(self, result=True):
        self.result = result

        self.version = Version.CURRENT
        self.identified = result
        self.extra_data = None

    def get_type_code(self):
        return MessageType.TYPE_REG_RM_RESULT
