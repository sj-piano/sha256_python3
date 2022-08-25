# Imports
import logging




# Relative imports
from . import sha256




# ### Notes
# Importing a package essentially imports the package's __init__.py file as a module.




# Collect up the things that we want in the immediate namespace of this module when it is imported.
# This file allows a parent package to run this:
# import sha256_python3 as sha256
# sha256.hello()
# result_bytes = sha256.SHA256(ascii_input_string).digest()
# result_bytes = sha256.digest(ascii_input_string)
# result_bytes = sha256.digest(input_bytes)
# result_hex = sha256.hexdigest(ascii_input_string)
hello = sha256.code.hello.hello
validate = sha256.util.validate
configure_module_logger = sha256.util.module_logger.configure_module_logger
#submodules = sha256.submodules
SHA256 = sha256.code.sha256.SHA256
digest = sha256.code.sha256.digest
hexdigest = sha256.code.sha256.hexdigest




# Set up logger for this module. By default, it produces no output.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.ERROR)
log = logger.info
deb = logger.debug




def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
  # Configure logger for this module.
  sha256.util.module_logger.configure_module_logger(
    logger = logger,
    logger_name = __name__,
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
  deb('Setup complete.')
  # Configure modules further down in this package.
  sha256.setup(
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )

