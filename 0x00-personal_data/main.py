#!/usr/bin/env python3
"""
Main File
"""
import logging
import re


filter_datum = __import__('filtered_logger').filter_datum
RedactingFormatter = __import__('filtered_logger').RedactingFormatter
get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS


fields = ["password", "date_of_birth"]
messages = [
        "name=egg;email=eggmin@eggsample.com\
;password=eggcellent;data_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;\
date_of_birth=03/04/1993;"
        ]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))


message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord(
        "my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print('\n')
print("=" * 30)
print(formatter.format(log_record))

print('\n')
print("=" * 30)
print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))
