from setuptools import setup, find_packages

setup(
    name='git_releaser',
    version='69.0.3',
    description='A quick script to commit, handle versioning and generate changelogs',
    long_description=open('README.rst').read(),
    author='Ran Shamay',
    author_email='ran.shamay89@gmail.com',
    url='https://github.com/ranshamay89/git-releaser',
    license='MIT',
    packages=find_packages(),
    package_data={
        'git-releaser': ['git-releaser/templates/*.jinja2'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': ['git-releaser=git_releaser.__main__:main'],
    },
    install_requires=[
        'bumpversion==0.5.12',
        'docopt'
    ]
)
