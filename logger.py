# app/__init__.py
import logging

# Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.setLevel(logging.DEBUG)

# Add a file handler to log to a file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
logging.addHandler(file_handler)

# Add a console handler to log to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.addHandler(console_handler)
