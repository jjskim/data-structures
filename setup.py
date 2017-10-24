"""Setup module for data-structures package."""

from setuptools import setup

setup(
    name="data-structures",
    description="Implementations of various data structures in Python",
    package_dir={"": "src"},
    author="Joseph Kim",
    author_email="joseph.kim.kr@gmail.com",
    py_modules=['linked_list'],
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "pytest-watch", "tox"],
        "development": ["ipython"]
    },
    entry_points={
    }
)
