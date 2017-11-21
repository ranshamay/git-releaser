"""
Bumpversion and generate a changelog straight from your git commits.

Usage: git-releaser [options]

options:
    -r --repo                           Path to the repository's root directory
    -t --template-dir                   The directory containing the templates used for
                                        rendering the changelog
    -h --help                           Print this help text
    -p --promote [default:patch]        Major,minor or patch version [Default: patch]
    -V --version                        Print the version number
"""
import bumpversion
import docopt
import os
import sys
from git_releaser import __version__

CONFIG_FILE_LOCATION = os.path.join(os.getcwd(), 'setup.cfg')


def main():
    args = docopt.docopt(__doc__, version=__version__)
    # cz(["commit"])
    changelog_args = list()
    changelog_args.append('--repo')
    if '--repo' not in sys.argv:
        changelog_args.append(os.getcwd())
    else:
        changelog_args.append(args.get('--repo'))
    changelog_args.append("--template-dir")
    changelog_args.append("/Users/ran_shamay/devl/Code/auto-changelog/auto_changelog/templates")
    promote_kinds = ['patch', 'major', 'minor']
    next_version_bump_policy = 'patch'
    if args.get('--promote') in promote_kinds:
        next_version_bump_policy = args['--promote']
    bumpversion.main(
        ['--allow-dirty', '--config-file', CONFIG_FILE_LOCATION, next_version_bump_policy, "--tag", "--commit"],
        changelog_args)
    print """type "git push" to push all changes to git"""


if __name__ == "__main__":
    main()
