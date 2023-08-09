#!/usr/bin/env python3
""" Authentication for the Simple API"""

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method that returns a boolean """
        return False

    def authorization_header(self, request=None) -> str:
        """pubic method that returns a string"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """method that returns a TypeVar"""
        return None
