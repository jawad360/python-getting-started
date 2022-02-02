# Doing like this would require to use helper prefix
# Eg helper.print_message
import logging

import helper

# Doing like this would not require to use helper prefix
# Functions can be directly used
# from helper import *

# Here we can directly use print_message
from helper import print_message, pi

# Aliases
import logging as log

logger = log.getLogger()
logger.error("Error happened")

helper.print_message()
print_message()
print(pi)
