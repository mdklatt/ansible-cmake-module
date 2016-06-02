""" Test suite for the the cmake module.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the module is actually
being tested. If the library is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from json import loads

import pytest
from cmake import main


def test_cmake(capsys):
    """ Test the cmake script.

    """
    assert 1 == main()
    stdout, _ = capsys.readouterr()
    assert {"failed": True, "msg": "not implemented"} == loads(stdout)
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))

