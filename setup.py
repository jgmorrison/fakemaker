from setuptools import setup

VERSION = '0.0.2'

setup(
<<<<<<< HEAD
    name = "fakemaker",
=======
    name = "fake_maker",
>>>>>>> 7639aa97c757e5aeb094a8fcde7869ad4e6ddd4b
    version = VERSION,
    author = "John Morrison",
    author_email = "jgmorrison84@gmail.com",
    description = ("A tool for quickly generating a CSV of user data."),
    test_suite = "nose.collector",
    install_requires = "fake-factory",
<<<<<<< HEAD
    packages = ["fakemaker", "tests"]
=======
    packages = ["fake_maker", "tests"]
>>>>>>> 7639aa97c757e5aeb094a8fcde7869ad4e6ddd4b
)
