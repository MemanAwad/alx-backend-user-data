#!/usr/bin/env python3
""" Module of basic_auth
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    '''BasicAuth class'''
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        '''extract_base64_authorization_header method'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        prefix = "Basic "
        if authorization_header.startswith(prefix):
            return authorization_header[len(prefix):]
        else:
            return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        '''encode the text'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, ValueError):
            return None
