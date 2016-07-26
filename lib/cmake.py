""" Ansible module for building projects with CMake.

See the DOCUMENTATION and EXAMPLES strings below for more information.

"""
from __future__ import print_function

from os.path import abspath
from subprocess import Popen
from subprocess import PIPE


from ansible.module_utils.basic import AnsibleModule


__all__ = "main",


__version__ = "0.1.0"  # PEP 0440 with Semantic Versioning


DOCUMENTATION = """
module: cmake
short_description: Build a project using CMake.
notes:
- U(github.com/mdklatt/ansible-cmake-module)
version_added: "2.1"
author: Michael Klatt
options:
  build_type:
    description: CMake build type to use.
    required: false
    default: Debug
    choices: [Debug, Release, RelWithDebInfo, MinSizeRel]
  binary_dir:
    description: Destination for binaries.
    required: true
  source_dir:
    description: |
      Location of C(CMakeLists.txt). This is required the first time a project
      is built, or use it to tell CMake to regenerate the build files.
    required: false
  target:
    description: The name of the target to build.
    required: false
  executable:
    description: Path to the C(cmake) executable.
    required: false
  vars:
    description: A dictionary of build variables.
    required: false
"""  # must be valid YAML


EXAMPLES = """
# Build a project.
- cmake:
    source_dir: /path/to/project
    binary_dir: /path/to/broject/build

# Build and install a built project.
- cmake:
    source_dir: /path/to/project
    binary_dir: /path/to/project/build
    target: clean

# Clean a built project (source_dir is not required).
- cmake:
    binary-dir: /path/to/project/build
    target: clean
"""  # plain text


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
        # (Re)generate build files.
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
