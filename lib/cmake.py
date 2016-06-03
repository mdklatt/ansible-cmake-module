""" Ansible module for building CMake projects.

"""
from __future__ import print_function

from ansible.module_utils.basic import AnsibleModule


__all__ = "main",


_ARGS_SPEC = {
    # MUST use list for choices.
    "build_type": {
        "default": "Debug",
        "choices": ["Debug", "Release", "RelWithDebInfo", "MinSizeRel"],
    },
    "binary_dir": {},
    "source_dir": {},
    "target": {},
    "executable": {"default": "cmake"},
    "clean_first": {"default": False, "type": "bool"},
    "vars": {"type": "dict"},
}


def main():
    """ Execute the module.

    """
    module = AnsibleModule(_ARGS_SPEC, supports_check_mode=False)
    module.exit_json(changed=False, **module.params)  # calls sys.exit(0)


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(main())
