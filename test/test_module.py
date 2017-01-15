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


@pytest.fixture(scope="module")
def tmpdir(tmpdir_factory):
    """ Generate a test directory.

    """
    # Can't use the predefined tmpdir fixture because module scope is needed.
    return tmpdir_factory.mktemp("test_module")


def test_build(tmpdir, ansible_module):
    """ Test a normal build.

    """
    params = {
        "executable": "cmake",
        "build_type": "Debug",
        "source_dir": dirname(abspath(__file__)),
        "binary_dir": tmpdir.strpath,
    }
    result = ansible_module.cmake(**params)
    assert not result["localhost"].get("failed", False)
    cmd = join(result["localhost"]["binary_dir"], "test_app")
    assert 0 == call([cmd])
    return


def test_creates(tmpdir, ansible_module):
    """ Test a build using the creates option.

    This depends on the existence of the executable created by test_build().

    """
    params = {
        "executable": "cmake",
        "build_type": "Debug",
        "source_dir": dirname(abspath(__file__)),
        "binary_dir": tmpdir.strpath,
        "creates": tmpdir.join("test_app").strpath
    }
    result = ansible_module.cmake(**params)
    assert not result["localhost"].get("failed", False)
    assert not result["localhost"]["changed"]
    return


def test_clean(tmpdir, ansible_module):
    """ Test a build with a target.

    """
    params = {
        "executable": "cmake",
        "build_type": "Debug",
        "binary_dir": tmpdir.strpath,
        "target": "clean",
    }
    result = ansible_module.cmake(**params)
    assert not result["localhost"].get("failed", False)
    assert not tmpdir.join("test_app").check()  # make sure file is removed
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))

