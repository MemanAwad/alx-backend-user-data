#!/usr/bin/env python3
"""AUTH module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    '''hash password that return bytes'''
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)
