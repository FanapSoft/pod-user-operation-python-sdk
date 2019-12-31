import setuptools
from setuptools import setup
from .user_operation import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pod-user-operation",
    version=__version__,
    url="https://github.com/FanapSoft/pod-user-operation-python-sdk",
    license="MIT",
    author="ReZa ZaRe",
    author_email="rz.zare@gmail.com",
    description="This package for implementation of POD platform User Operation APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["pod", "user operation", "pod sdk"],
    packages=setuptools.find_packages(exclude=("build", "dist")),
    install_requires=[
        "pod-base>=1,<2"
    ],
    classifiers=[
        "Natural Language :: English",
        "Natural Language :: Persian",
    ],
    python_requires='>=2.7',
    package_data={
        'user_operation': ['*.ini', '*.json']
    },
    project_urls={
        "Documentation": "http://docs.pod.ir/v1.0.0.2/PODSDKs/python/5202/user-operation",
        "Source": "https://github.com/FanapSoft/pod-user-operation-python-sdk",
        "Tracker": "https://github.com/FanapSoft/pod-user-operation-python-sdk/issues"
    }
)
