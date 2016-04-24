""" Test suite for the the cmake module.

The script can be executed on its own or incorporated into a larger test suite.
However the tests are run, be aware of which version of the module is actually
being tested. If the library is installed in site-packages, that version takes
precedence over the version in this project directory. Use a virtualenv test
environment or setuptools develop mode to test against the development version.

"""
from json import loads
from os.path import dirname
from os.path import join
from subprocess import check_output
from subprocess import CalledProcessError

import pytest


def test_cmake(capsys):
    """ Test the cmake script.

    """
    root = dirname(dirname(__file__))
    with pytest.raises(CalledProcessError) as exinfo:
        check_output(join(root, "cmake").split())
    err = exinfo.value
    assert 1 == err.returncode
    assert {"failed": True, "msg": "not implemented"} == loads(err.output)
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))

