from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession

import os
import smsgateway


# Lists of requirements and dependency links which are needed during runtime, testing and setup
install_requires = []
tests_require = []
dependency_links = []

# Inject test requirements from requirements_test.txt into setup.py
requirements_file = parse_requirements(os.path.join('deployment', 'requirements.txt'), session=PipSession())
for req in requirements_file:
    install_requires.append(str(req.req))
    if req.link:
        dependency_links.append(str(req.link))

# Inject test requirements from requirements_test.txt into setup.py
requirements_test_file = parse_requirements(os.path.join('deployment', 'requirements_test.txt'), session=PipSession())
for req in requirements_test_file:
    tests_require.append(str(req.req))
    if req.link:
        dependency_links.append(str(req.link))


setup(
    name='django-smsgateway',
    version=smsgateway.__version__,
    url='https://github.com/vikingco/smsgateway',
    license='commercial',
    description='SMS gateway for sending text messages',
    long_description=open('README.rst', 'r').read(),
    author='VikingCo NV/Medialaan',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,  # Don't create egg files, Django cannot find templates in egg files.
    install_requires=install_requires,
    setup_requires=['pytest-runner', ],
    tests_require=tests_require,
    dependency_links=dependency_links,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
