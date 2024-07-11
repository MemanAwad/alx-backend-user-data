#!/usr/bin/env python3
""" Module of Users views
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    '''Auth class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''require auth method returns False - path'''
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True

        normalized_path = path.rstrip('/') + '/'
        if normalized_path in excluded_paths:
            return False
        elif normalized_path not in excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        '''returns None - request will be the Flask request object'''
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        else:
            return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        '''None - request will be the Flask request object'''
        return None

    def session_cookie(self, request=None):
        '''returns a cookie value from a request'''
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None

        return request.cookies.get(session_name)
