==============
Git Releaser
==============
Version:53.0.0
A quick script that will generate a changelog for any git repository using 
`conventional style` commit messages.


Installation
============

Pip
---

auto-changelog is up on PyPI, so you can install it with::

    pip install auto-changelog

From Source
-----------

Otherwise, you can install from source by cloning the repository from Github::

    git clone https://github.com/Michael-F-Bryan/auto-changelog.git

And install the package::

    python setup.py install


Usage
=====

Calling The Program
-------------------

The package is callable using the `python -m` shortcut::

    python -m auto_changelog

Or alternatively, you can use the provided command::

    auto-changelog


Formatting Your Commit Messages
-------------------------------

Of course, none of this is going to work if your commit messages are all over
the place. The program currently only understands commit messages written
following the `Angular commit message conventions`_. This means that your
commit messages should look something like this::

    <type>(<scope>): <subject>
    <BLANK LINE>
    <body>
    <BLANK LINE>
    <footer>

The `type` and `subject` fields are mandatory, everything else is optional.

These are some of the valid types that `Angular` use:


feat 
    A new feature
fix 
    A bug fix
docs
    Documentation only changes
style
    Changes that do not affect the meaning of the code (white-space, 
    formatting, missing semi-colons, etc) 
refactor
    A code change that neither fixes a bug nor adds a feature
perf
    A code change that improves performance
test
    Adding missing tests
chore
    Changes to the build process or auxiliary tools and libraries such as 
    documentation generation 

.. note:: The types field should be lower case, although the parser itself is 
          case insensitive.

For more detailed information, please check out `Angular's contributing
guide`_.

Examples
========

Below are a couple screenshots showing the result of the `auto-changelog`
command.

.. image:: examples/git_log_one_line.jpg
    :alt: Result of "git log --oneline --graph --decorate"

.. image:: examples/generated_commit_message.jpg
    :alt: Generated change log


.. _Angular commit message conventions: https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit
.. _Angular's contributing guide: https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit
