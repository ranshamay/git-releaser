from setuptools import setup, find_packages

setup(
    name='git_releaser',
    version='11.0.0',
    description='A quick script to commit, handle versionning and generate changelogs',
    long_description=open('README.rst').read(),
    author='Ran Shamay',
    author_email='ran.shamay89@gmail.com',
    url='https://github.com/ranshamay89/git-releaser',
    license='MIT',
    packages=find_packages(),

    package_data={
        'git_releaser': ['auto-changelog', 'bumpversion'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': ['git-releaser=git_releaser.__main__:main'],
    },

    install_requires=[
        'auto-changelog',
        'bumpversion',
    ],

    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='git releaser',

)
