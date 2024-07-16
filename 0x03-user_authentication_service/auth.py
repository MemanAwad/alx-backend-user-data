#!/usr/bin/env python3
"""AUTH module"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        '''hash password that return bytes'''
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password_bytes, salt)

    def register_user(self, email: str, password: str) -> User:
        '''method that register users'''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            passw = self._hash_password(password)
            user = self._db.add_user(email, passw)
            return user
