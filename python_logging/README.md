# python logging
----------------

uses the python logging module to handle print statements and log files. Instead
of everything getting printed to the screen all the time, only prints messages
that reach a set level of urgency. Also allows messages of intermediate urgency
levels to be written to a file instead of the screen. Initial template created
with gemini with tweaks and annotations added by me.

Basic concepts:
 - a logger has levels associated with it (DEBUG, INFO, WARNING, ERROR, and
   CRITICAL)
 - the logger has handlers associated with it. Each handler has a set level
 associated with it as well as what to do (print to screen, write to file, etc.)
 - messages get executed in the code under normal conditionals. Each message has
 content and an urgency level. If any handlers match the urgency level, those
 handlers execute.

Basic process is as follows:
 - import python's logging module
 - create a logger and name it with logger=logging.getLogger(your_logger_name)
 - create a formatted string with logging.setFormatter(printf string)
 - make a handler with logging.streamHandler
 - set the level of the handler and add the formatted string to it
 - add the handler to your logger
 - repeat for whatever handlers you want
 - create a message with logger.info, logger.error, logger.warning, etc. Your
   handlers will automatically execute based on whether they meet the
   corresponding level threshold.
