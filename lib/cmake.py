""" Ansible module for building CMake projects.

"""
from __future__ import print_function

from os.path import abspath
from subprocess import Popen
from subprocess import PIPE


from ansible.module_utils.basic import AnsibleModule


__all__ = "main",


_ARGS_SPEC = {
    # MUST use list for choices.
    "build_type": {
        "default": "Debug",
        "choices": ["Debug", "Release", "RelWithDebInfo", "MinSizeRel"],
    },
    "binary_dir": {"required": True},
    "source_dir": {"default": None},
    "target": {},
    "executable": {"default": "cmake"},
    "vars": {"type": "dict"},
}


def main():
    """ Execute the module.

    """
    def cmake(args):
        """ Execute cmake command. """
        # Any output to STDOUT or STDERR must be captured.
        args = [module.params["executable"]] + list(args)
        process = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binary)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            module.fail_json(msg=stderr, stdout=stdout, rc=process.returncode)
        return

    module = AnsibleModule(_ARGS_SPEC, supports_check_mode=False)
    vars = {"CMAKE_BUILD_TYPE": module.params["build_type"]}
    try:
        vars.update(module.params["vars"])
    except TypeError:  # parameter is None
        pass
    binary = abspath(module.params["binary_dir"])
    if module.params["source_dir"]:
        config_args = []
        for var in vars.iteritems():
            config_args.extend(("-D", "=".join(var)))
        source = abspath(module.params["source_dir"])
        config_args.append(source)
        cmake(config_args)
    build_args = ["--build", binary]
    if module.params["target"]:
        build_args.extend(("--target", module.params["target"]))
    cmake(build_args)
    module.exit_json(changed=True, rc=0, **module.params)  # calls sys.exit(0)


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(main())
