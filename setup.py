from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'tensorflow-gpu==2.0.0a0',
    'oauth2client>=4.1.3',
    'google-api-python-client>=1.7.8',
    'matplotlib>=3.0.3',
    'Click',
]

setup(
    name='cifar_10_example',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cifar-10-inference=cifar_10_example_client.inference:main',
            'cifar-10-meta=cifar_10_example_client.meta_info:main',
        ],
    },
    description='AI Platform example for CIFAR-10 model.')
