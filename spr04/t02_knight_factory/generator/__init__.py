import logging
from .names import *
from .titles import *

logging.basicConfig(level = logging.DEBUG, format = '..::Knight Generator::.. %(process)s-%(levelname)s-%(message)s') #если код процесса будет не принят ораклом, поставить по умолчанию 8672 как в выводе пдф
logger = logging.getLogger(__name__)
