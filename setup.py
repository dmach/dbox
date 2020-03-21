#!/usr/bin/python3


from distutils.core import setup


setup(
    name='dbox',
    version='1.0',
    description='Tool for developing, building, testing and debugging software in unprivileged Podman containers',
    author='Daniel Mach',
    author_email='dmach@redhat.com',
    url='https://github.com/dmach/dbox',
    scripts=[
        "dbox",
        "gitc",
        "gitc-recursive",
    ],
)
