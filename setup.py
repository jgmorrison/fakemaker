from setuptools import setup

VERSION = '0.0.2'

setup(
    name = "fake_maker",
    version = VERSION,
    author = "John Morrison",
    author_email = "jgmorrison84@gmail.com",
    description = ("A tool for quickly generating a CSV of user data."),
    test_suite = "nose.collector",
    install_requires = "fake-factory",
    packages = ["fake_maker", "tests"]
)
