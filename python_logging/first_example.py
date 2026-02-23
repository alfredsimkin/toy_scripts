'''
imports a logger and runs the code contained within. See python_logging in
fake_module_folder for an example
'''
import logging
import fake_module_folder.python_logging as pl



'''
configures what types of messages will be acted upon and which will be ignored.
Any messages above a set level will be acted upon. Message types are as follows:
DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50) - in this case
messages of level 20 or higher will be printed. In this example, INFO statements
will not execute but WARNING, ERROR, and CRITICAL ones will.
'''
#pl.logger.setLevel(logging.INFO)
pl.logger.setLevel(logging.WARNING)

#you can run the logging as a function within the logging module
#pl.run_sample_logs()

#or you can run it directly here:
pl.logger.info(f"this is some info, executed whenever our setLevel is not higher than info")
pl.logger.error(f"this is an error, executed whenever our setLevel is not higher than error")