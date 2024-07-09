#!/usr/bin/env python3
""" Module of Users views
"""
from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''None - request will be the Flask request object'''
        return None
