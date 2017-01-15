=====
cmake
=====
..  _Ansible: http://docs.ansible.com/ansible
..  _CMake: https://cmake.org

This is an `Ansible`_ module for building projects using `CMake`_. CMake must
already be installed on the target machine.


Options
=======
- ``binary_dir``: destination for binaries (required)
- ``source_dir``: location of ``CMakeLists.txt``
- ``build_type``: CMake build type; defaults to ``Debug``
- ``target``: target to build
- ``cache_vars``: dictionary of cache variables to set


Notes
=====
The ``source_dir`` is required for a new build, or it can be used to tell CMake
to regenerate build files.



Installation
============
Ansible searches for for modules specified by the ``ANSIBLE_LIBRARY``
environment variable or the ``library`` paramater in an ``ansible.cfg`` file.

The module can also be distributed with a role by placing it in the role's
``library`` directory. The module will be available to that role and any role
called afterwards.


Testing
=======
..  code-block::

    $ export ANSIBLE_LIBRARY=lib
    $ pytest --ansible-host-pattern=localhost test/
