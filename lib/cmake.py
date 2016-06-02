""" Ansible module for building CMake projects.

"""
from __future__ import print_function

from ansible.module_utils.basic import AnsibleModule


__all__ = "main",


def main():
    """ Execute the module.

    """
    module = AnsibleModule({})
    module.fail_json(msg="not implemented")  # calls exit(1)


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(main())
