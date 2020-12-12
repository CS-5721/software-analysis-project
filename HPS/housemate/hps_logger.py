import sys
import time
from django.conf import settings

# Trivial singleton example. Usage:

# import hps_logger
# logger = hps_logger.Logger.instance()
# logger.log("Something happened")

# You might use a singleton so you have a globally accessible
# logger instance with a given config.
# In this instance we output to stderr, but this singleton may be
# configured to output to any file, pipe or socket.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class Logger():
    __instance = None

    def __init__(self):
        # Disallow external instantiation
        if Logger.__instance != None:
            raise Exception("Please call instance() ")
        else:
            Logger.__instance = self

    def log(self, message):
        #if not settings.DEBUG:
        #    return
        now = time.asctime( time.localtime(time.time()) )
        # Printing self to demonstrate one instance is in use
        eprint(now, self, message, sep=" - ")

    def instance():
        if Logger.__instance == None:
            Logger()
        return Logger.__instance


