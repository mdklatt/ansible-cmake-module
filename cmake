#!/usr/bin/python
""" Ansible module for building CMake projects.

"""
from __future__ import print_function

from json import dumps


__all__ = "main",


def main():
    """ Execute the module.

    """
    print(dumps({"failed": True, "msg": "not implemented"}))
    return 1


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(main())
