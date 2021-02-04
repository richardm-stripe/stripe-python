import os
import sys
from codecs import open
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = "-n auto"

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(
    os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

version_contents = {}
with open(os.path.join(here, "stripe", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name="stripe",
    version=version_contents["VERSION"],
    description="Python bindings for the Stripe API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Stripe",
    author_email="support@stripe.com",
    url="https://github.com/stripe/stripe-python",
    license="MIT",
    keywords="stripe api payments",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"stripe": ["data/ca-certificates.crt"]},
    zip_safe=False,
    install_requires=[
        'requests >= 2.20',
    ],
    python_requires=">=3.6",
    tests_require=[
        'pytest >= 6.2.2',
        "pytest-mock >= 3.5.1",
        "pytest-xdist >= 2.2.0",
        "pytest-cov >= 2.11.1",
        "coverage >= 5.4",
    ],
    cmdclass={"test": PyTest},
    project_urls={
        "Bug Tracker": "https://github.com/stripe/stripe-python/issues",
        "Documentation": "https://stripe.com/docs/api/python",
        "Source Code": "https://github.com/stripe/stripe-python",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
