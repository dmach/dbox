DBox
====

DBox is a tool for developing, building, testing and debugging software
in unprivileged [Podman](https://podman.io/) containers.

Unlike [Toolbox](https://github.com/containers/toolbox) which is focused
at developing desktop applications, DBox simplifies work with software
stacks that consist of multiple projects. It automatically overrides
environment paths such as PATH, PYTHONPATH or LD_LIBRARY_PATH in the containers
and that makes the compiled binaries and libraries instantly available.

You may be wondering what the "D" in DBox stands for.
It's DNF-stack-in-a-Box, because DBox was originally written
to simplify development of the [DNF](https://github.com/rpm-software-management/dnf) stack.


Install
=======

    pip3 install --user git+https://github.com/dmach/dbox.git


Usage
=====


Clone stack configuration to the local host:

    $ dbox stack-clone https://raw.githubusercontent.com/dmach/dbox/stacks/dnf-4.dbox.yaml
    Cloned stack: dnf-4
    Initialize with: dbox stack-init dnf-4


Initialize stack:

    $ mkdir <feature>
    $ cd <feature>
    $ dbox stack-init dnf-4


Create and enter an evironment:

    # build a podman image for the current stack based on the specified base image
    $ dbox create fedora:latest [--no-cache]
    $ dbox enter fedora:latest

    # check that we are really in a container
    [root@0aabbccddeef dbox]$ pwd
    /root/dbox


Clone projects:

    $ dbox clone dnf libdnf ...


Build projects:

    $ dbox build dnf


Use the programs immediately after they are built:

    $ which dnf
    /root/dbox/dnf/_install/fedora-latest/usr/bin/dnf


Important
=========

It is advised to always create a new directory with fresh clones of git projects for each feature and delete it after the work is completed.
Developing features in multiple branches and switching among them may lead to various issues due to sharing various caches.


Additional Tools
================

DBox comes with additional tools to make your git workflows easier.


gitc
----

The `gitc` program is a `git clone` wrapper that caches git repos in ~/.cache/gitc.
That makes cloning previously cloned git repos nearly instant.
It also supports extended syntax for switching to a branch, commit
or a pull request reference after the clone is finished.


gitc-recursive
--------------

The `gitc-recursive` program calls `gitc` recursively and inspects related
GitHub pull requests for `Requires:` or `Tests:` references and clones
all of them to the working directory. The git repositories are switched
according to the pull request references.


License
=======

* DBox licensed under GPLv2+
* See [COPYING](COPYING.md) for more details
