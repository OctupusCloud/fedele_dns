from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

with open(path.join(top_level_directory, 'requirements.txt')) as file:
    required = file.read().splitlines()

setup(
    name='fedele_dns',
    version='0.21.17',
    description='DNS',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Octupus',
    author_email='info@octupus.com',
    url='https://github.com/octupuscloud/O4N_FEDELE_DNS',
    install_requires=required,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords=['fedele', 'fedele-extension', 'extension'],
)
