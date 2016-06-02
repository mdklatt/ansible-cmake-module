""" Test suite for the the cmake module.

The script can be executed on its own or incorporated into a larger test suite.
The ANSIBLE_LIBRARY environment variable must include lib/, and pytest must be
run with `--ansible-host-pattern=localhost`.

"""
import pytest


def test_cmake(ansible_module):
    """ Test the cmake module.

    """
    result = ansible_module.cmake()
    assert u"not implemented" == result["localhost"]["msg"]
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))

