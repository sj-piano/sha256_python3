# Description

A pure Python 3 implementation of the SHA256 hash algorithm.






# Sample commands


```bash

python3 cli.py

python3 cli.py --help

python3 cli.py --task hello

python3 cli.py --task hello --log-level=info

python3 cli.py --task hello --log-level=debug

python3 cli.py --task get_python_version

python3 cli.py --task get_sha256 --data "hello world"

python3 cli.py --task get_sha256 --file sha256/data/data1.txt

```


Tests:

```bash

# Run all tests, including submodule tests.
pytest3

# Run all tests in a specific test file
pytest3 sha256/test/test_hello.py

# Run tests with relatively little output
pytest3 --quiet sha256/test/test_hello.py

# Run a single test
pytest3 sha256/test/test_hello.py::test_hello

# Print log output in real-time during a single test
pytest3 --capture=no --log-cli-level=INFO sha256/test/test_hello.py::test_hello

# Note: The --capture=no option will also cause print statements within the test code to produce output.

```



Code style:


```bash

pycodestyle example_python3_package/code/hello.py

pycodestyle --filename=*.py

pycodestyle --filename=*.py --statistics

pycodestyle --filename=*.py --exclude sha256/submodules

```

Settings for pycodestyle are stored in the file `tox.ini`.




# Development

Developed with:
- Ubuntu 16.04 on WSL on Windows 10
- Python 3.5.2
- pytest 6.1.2



# Background

Original package:  
https://github.com/thomdixon/pysha2

> pysha2 is a pure Python implementation of the FIPS 180-2 secure hash standard.

Author: Thom Dixon

Ported to Python 3 by Nicholas Piano.

Re-structured into its current package layout by StJohn Piano.











