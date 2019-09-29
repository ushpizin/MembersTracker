import setuptools


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name='MembersTracker',
    version='0.1.dev0',
    packages=['memberstracker'],
    install_requires=requirements,
)
