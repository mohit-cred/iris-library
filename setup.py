from setuptools import setup, find_packages
import pathlib
import pkg_resources

with pathlib.Path('./iris/requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(name='iris-library',
      version='0.0.2',
      description='This is a test package.',
      author='Mohit Agrawal',
      author_email='mohit.agrawal@cred.club',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "test.*"]),
      install_requires=install_requires,
      )