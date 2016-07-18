""" Test suite for the the cmake module.

The script can be executed on its own or incorporated into a larger test suite.
The ANSIBLE_LIBRARY environment variable must include lib/, and pytest must be
run with `--ansible-host-pattern=localhost`.

"""
from os.path import abspath
from os.path import dirname
from os.path import join
from subprocess import call

import pytest


def test_module(tmpdir, ansible_module):
    """ Test the module functionality.

    """
    params = {
        "executable": "cmake",
        "build_type": "Debug",
        "source_dir": dirname(abspath(__file__)),
        "binary_dir": tmpdir.strpath
    }
    result = ansible_module.cmake(**params)
    assert not result["localhost"].get("failed", False)
    cmd = join(result["localhost"]["binary_dir"], "test_app")
    assert 0 == call([cmd])
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))

