"""
Generate a changelog straight from your git commits.

Usage: git-releaser [options]

Options:
    -r=REPO --repo=REPO     Path to the repository's root directory
    -t=TITLE --title=TITLE  The changelog's title [Default: CHANGELOG]
    -d=DESC --description=DESC
                            Your project's description
    -o=OUTFILE --output=OUTFILE
                            The place to save the generated changelog 
                            [Default: CHANGELOG.md]
    -t=TEMPLATEDIR --template-dir=TEMPLATEDIR
                            The directory containing the templates used for
                            rendering the changelog 
    -h --help               Print this help text
    -V --version            Print the version number
"""
import bumpversion
import docopt
import os
import sys

# from git_releaser import __version__

"""
Release a new version to git.

Usage: git-releaser [options]

options:
    -r=REPO --repo=REPO     Path to the repository's root directory
    -h --help               Print this help text
    -V --version            Print the version number
"""
CONFIG_FILE_LOCATION = os.path.join(os.getcwd(), 'setup.cfg')


def main():
    args = docopt.docopt(__doc__, version='0.1.0')
    # cz(["commit"])
    changelog_args = list()
    changelog_args.append('--repo')
    if '--repo' not in sys.argv:
        changelog_args.append(os.getcwd())
    else:
        changelog_args.append(args.get('--repo'))
    changelog_args.append("--template-dir")
    changelog_args.append("/Users/ran_shamay/devl/Code/auto-changelog/auto_changelog/templates")
    bumpversion.main(['--allow-dirty', '--config-file', CONFIG_FILE_LOCATION, "major", "--tag", "--commit"],
                     changelog_args)


if __name__ == "__main__":
    main()
