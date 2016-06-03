""" Test suite for the the cmake module.

The script can be executed on its own or incorporated into a larger test suite.
The ANSIBLE_LIBRARY environment variable must include lib/, and pytest must be
run with `--ansible-host-pattern=localhost`.

"""
import pytest


@pytest.mark.parametrize("build", ("Debug", "Release", "RelWithDebInfo", "MinSizeRel"))
def test_args(ansible_module, build):
    """ Test module arguments.

    """
    # For now, this just tests that each build type is accepted
    params = {"build_type": build}
    result = ansible_module.cmake(**params)
    assert build == result["localhost"]["build_type"]
    return


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main(__file__))

