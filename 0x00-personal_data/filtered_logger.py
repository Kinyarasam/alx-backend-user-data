#!/usr/bin/env python3
"""
0. Regex-ing
"""
import re
from typing import List, Union


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}
def filter_datum(fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """Obfuscate Log message fields.

    Args:
        fields (List[str]): The fields to obfuscate.
        redaction (str): The string to replace the fields with.
        message (str): The log line to process.
        separator (str): The character that separates the fields in the log line.

    Returns:
        str: The obfuscated log line.
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
