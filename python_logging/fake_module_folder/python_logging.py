'''
uses the python logging module to handle print statements. Instead of everything
getting printed to the screen all the time, only prints messages that reach a
set level of urgency. Also allows messages of intermediate urgency levels to be
written to a file instead of the screen. Initial template created with gemini
with annotations added by me.
'''

import logging
import sys

# Setup Logger - the __name__ argument allows us to name our logger based on
#the module that it's being imported from.
logger = logging.getLogger(__name__)
#you can also manually name the logger - useful if calling the script with the
#logger directly, otherwise __name__ handles this automatically if importing:
#logger = logging.getLogger("AppLogger")

'''
Prevents the logs from being printed twice - apparently by default anything that
calls logging is sent to both the logger (established above) and a "Root
Logger". If the Root Logger has a StreamHandler attached, both my handler and
the root's handler will print. In this example the Root Logger doesn't seem to
have a StreamHandler attached, but I'm including the command anyway.
'''
logger.propagate = False  

'''
Define the Formatter - formats all log messages to conform to these settings.
This template adds a newline before and after every log message, and dictates
the content that will go in every log message. In this case content will be the
time, the name of the logger (named in logging.getLogger above), and the message
(created in every logger instance in the code). Viable options are reserved
keywords used by the Formatter, options include asctime, name, levelname,
message, and lineno. String formatting (% signs) is python's older printf
formatting.
old 
'''


# 3. Setup Handler - applies the format to every log string.
console_format = logging.Formatter('\n%(levelname)s: %(message)s\n')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

file_format = logging.Formatter('time: %(asctime)s | level: %(levelname)s | Source: %(name)s | message: %(message)s | line number: %(lineno)s')
file_handler = logging.FileHandler("error_log.txt")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

#an example path that I might want the logger to print
from pathlib import Path
file_path=Path('.').resolve()

# --- TESTING IT OUT ---
def run_sample_logs():
	logger.info(f"load_workbook(): Loading file - {file_path}")
	logger.error("Failed to connect to database!")   # Appears on Console AND in error_log.txt