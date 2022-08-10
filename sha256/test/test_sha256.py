# Imports
import pytest
import pkgutil




# Relative imports
from .. import code
from .. import util
from .. import submodules




# Shortcuts
from ..code import sha256




# Setup for this file.
@pytest.fixture(autouse=True, scope='module')
def setup_module(pytestconfig):
  # If log_level is supplied to pytest in the commandline args, then use it to set up the logging in the application code.
  log_level = pytestconfig.getoption('log_cli_level')
  if log_level is not None:
    log_level = log_level.lower()
    code.setup(log_level = log_level)
    submodules.setup(log_level = log_level)




# ### SECTION
# Basic checks.


def test_hello():
  x = sha256.hash('hello world')
  assert x == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'


def test_hello_data():
  data_file = '../data/data1.txt'
  data = pkgutil.get_data(__name__, data_file).decode('ascii').strip()
  assert data == 'hello world'
  x = sha256.hash(data)
  assert x == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'


def test_empty_string():
  x = sha256.hash('')
  assert x == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


def test_a():
  x = sha256.hash('a')
  assert x == 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'


def test_abc():
  x = sha256.hash('abc')
  assert x == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'


def test_alphabet():
  x = sha256.hash('abcdefghijklmnopqrstuvwxyz')
  assert x == '71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73'


def test_alphanumeric():
  x = sha256.hash('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
  assert x == 'db4bfcbd4da0cd85a60c3c37d3fbd8805c77f15fc6b1fdfe614ee0a7c8fdb4c0'


def test_lorem_ipsum():
  x = sha256.hash('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
  assert x == 'a58dd8680234c1f8cc2ef2b325a43733605a7f16f288e072de8eae81fd8d6433'



