"""Class module to practice searching algorithms on various data structures"""

import logging
from guppy import hpy
import resource

# set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

h = hpy()
h.heap()
print(h.doc)
print(h.heap())


