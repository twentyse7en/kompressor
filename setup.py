#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages


requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Abijith B",
    author_email='abijithbahuleyan@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Compress image using k-means algorithm.",
    entry_points={
        'console_scripts': [
            'kompressor=kompressor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description= "",
    include_package_data=True,
    keywords='kompressor',
    name='kompressor',
    packages=find_packages(include=['kompressor', 'kompressor.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/twentyse7en/kompressor',
    version='0.1.0',
    zip_safe=False,
)
