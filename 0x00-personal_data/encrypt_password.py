#!/usr/bin/env python3
"""Password encryption module
"""
import bycrypt


def hash_password(password: str) -> str:
    """Encrypts a password

    Args:
