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
  x = sha256.hexdigest('hello world')
  assert x == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'


def test_hello_data():
  data_file = '../data/data1.txt'
  data = pkgutil.get_data(__name__, data_file).decode('ascii').strip()
  assert data == 'hello world'
  x = sha256.hexdigest(data)
  assert x == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'


def test_empty_string():
  x = sha256.hexdigest('')
  assert x == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


def test_0():
  x = sha256.hexdigest('0')
  assert x == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'


def test_1():
  x = sha256.hexdigest('1')
  assert x == '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'


def test_max_32_byte_value():
  max_value = 'ff' * 32
  assert len(max_value) == 64  # 2 hex chars = 1 byte
  x = sha256.hexdigest(max_value)
  assert x == 'df0790f236013511e91fa4532fb7761f62320a51a3868dabf4a13fe5f53e3263'


def test_a():
  x = sha256.hexdigest('a')
  assert x == 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'


def test_abc():
  x = sha256.hexdigest('abc')
  assert x == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'


def test_alphabet():
  x = sha256.hexdigest('abcdefghijklmnopqrstuvwxyz')
  assert x == '71c480df93d6ae2f1efad1447c66c9525e316218cf51fc8d9ed832f2daf18b73'


def test_alphanumeric():
  x = sha256.hexdigest('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
  assert x == 'db4bfcbd4da0cd85a60c3c37d3fbd8805c77f15fc6b1fdfe614ee0a7c8fdb4c0'


def test_lorem_ipsum():
  x = sha256.hexdigest('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
  assert x == 'a58dd8680234c1f8cc2ef2b325a43733605a7f16f288e072de8eae81fd8d6433'


def test_32_bytes():
  input = 'A 32-byte string [filler text__]'
  assert len(input) == 32
  x = sha256.hexdigest(input)
  assert x == '68f38dcc9edb5c831ea250a5a41bf2aa2a041fbbb8cd6a59567cb3e44109dab5'


def test_64_bytes():
  input = 'A string with a length of exactly 64 bytes. [filler text ......]'
  assert len(input) == 64
  x = sha256.hexdigest(input)
  assert x == '61fd7af55707d90f58ccf73bbf89dec2dcd388131048900a17e62ef6f7efcfc9'


def test_fox_1():
  x = sha256.hexdigest('The quick brown fox jumps over the lazy dog')
  assert x == 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592'


def test_fox_1():
  x = sha256.hexdigest('The quick brown fox jumps over the lazy cog')
  assert x == 'e4c4d8f3bf76b692de791a173e05321150f7a345b46484fe427f6acc7ecc81be'



