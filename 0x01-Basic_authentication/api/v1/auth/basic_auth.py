#!/usr/bin/env python3
""" Module of basic_auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''BasicAuth class'''
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        '''extract_base64_authorization_header method'''
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        prefix = "Basic "
        if authorization_header.startswith(prefix):
            return authorization_header[len(prefix):]
        else:
            return None
