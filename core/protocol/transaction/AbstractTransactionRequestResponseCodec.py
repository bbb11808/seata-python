#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.ByteBuffer import ByteBuffer
from core.protocol.AbstractResultMessageCodec import AbstractResultMessageCodec
from exception.TransactionExceptionCode import TransactionExceptionCode


class AbstractTransactionResponseCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        AbstractResultMessageCodec.encode(t, out_buffer)
        transaction_exception_code = t.transaction_exception_code
        out_buffer.put_int8(transaction_exception_code.value)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        AbstractResultMessageCodec.decode(t, in_buffer)
        t.transaction_exception_code = TransactionExceptionCode(in_buffer.get_int8())
