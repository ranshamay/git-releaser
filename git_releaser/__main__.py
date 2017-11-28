"""
Bumpversion and generate a changelog straight from your git commits.

Usage: git-releaser [options]

options:
    -r --repo [default:os.getcwd()]        Path to the repository's root directory
    -h --help                              Print this help text
    -p --promote [default:patch]           Major,minor or patch version [Default: patch]
    -V --version                           Print the version number

"""
import os

import docopt

import bumpversion
from git_releaser import __version__

CONFIG_FILE_LOCATION = os.path.join(os.getcwd(), 'setup.cfg')


def main():
    args = docopt.docopt(__doc__, version=__version__)
    changelog_args = list()
    changelog_args.append('--repo')
    base_name = os.getcwd()
    if '--repo' in args and args['--repo'] is not None:
        base_name = args.get('--repo')
    changelog_args.append(base_name)
    repo_name = os.path.basename(base_name)
    changelog_args.append('--repo-name')
    changelog_args.append(repo_name)
    changelog_args.append("--template-dir")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(BASE_DIR, 'templates')
    changelog_args.append(template_dir)
    promote_kinds = ['patch', 'major', 'minor']
    next_version_bump_policy = 'patch'
    if args.get('--promote') in promote_kinds:
        next_version_bump_policy = args['--promote']
    bumpversion.main(
        ['--allow-dirty', '--config-file', CONFIG_FILE_LOCATION, next_version_bump_policy, "--tag", "--commit"],
        changelog_args)
    print """type `git push --tags origin master` to push all changes to git"""


if __name__ == "__main__":
    main()
