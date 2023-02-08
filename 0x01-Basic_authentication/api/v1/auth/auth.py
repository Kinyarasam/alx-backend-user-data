#!/usr/bin/env python3
"""Handle the management of the API authentication
"""
from flask import request
from typing import List, TypeVar
import re

class Auth:
    """Manage the Api authentication
    """

    def __init__(self):
        """Instantiation method
        """
        pass

    def require_auth(self, path:str, excluded_paths: List[str]) -> bool:
        """public method to be handled later.

        Args:
            path (str): Path
            excluded_paths (List[str]): List containing excluded paths

        Returns:
            bool: 
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header

        Args:
            request (any): Any request

        Returns:
            (str): The Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User

        Args:
            request (any): Any request

        Returns:
            (Typevar('User')): Flask request object of type User.
        """
        return None

