#!/usr/bin/env python3
import argparse
import sys
import subprocess
import re
import os


DEFAULT_DISTRO = 'ubuntu'
DISTROS = {'ubuntu', 'alpine'}
assert DEFAULT_DISTRO in DISTROS


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


def _distro(text):
    if text not in DISTROS:
        print('Incorrect distribution choose one of ' + ', '.join(list(DISTROS)))
        sys.exit(1)
    return text


def _extract_release(tag):
    match = re.match(r'^v(\d+)\.(\d+)\.(\d+)$', tag)
    if not match:
        return False, None, None, None

    return True, int(match.group(1)), int(match.group(2)), int(match.group(3))


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('tag', help='The tag name or branch name to build')
    parser.add_argument('distro', type=_distro, default=DEFAULT_DISTRO, nargs='?', help='The distribution base to build')
    parser.add_argument('-a', '--all', action='store_true', help='Generate all the image names')
    parser.add_argument('-l', '--latest', action='store_true', help='Generate latest tag')
    return parser.parse_args()


def build_docker_image(source_tag, docker_tag, distro):
    print('Creating new docker img {} (from: {} distro: {})...'.format(docker_tag, source_tag, distro))
    docker_file_path = os.path.join(PROJECT_ROOT, distro, 'Dockerfile')
    cmd = [
        'docker',
        'build',
        '-t', docker_tag,
        '--build-arg', 'ledger_tag={}'.format(source_tag),
        '-f', docker_file_path,
        PROJECT_ROOT,
    ]
    subprocess.check_call(cmd)


def tag_docker_image(source_tag, new_tag):
    print('Creating new docker tag {} (from: {})...'.format(new_tag, source_tag))
    cmd = ['docker', 'tag', source_tag, new_tag]
    subprocess.check_call(cmd)


def build_docker_tags(args):
    label_suffix = '' if args.distro == DEFAULT_DISTRO else '-{}'.format(args.distro)

    # determine if this happens to be a release build
    is_release, major, minor, patch = _extract_release(args.tag)

    labels = []
    if is_release:
        labels.append('{}.{}.{}'.format(major, minor, patch))
        if args.all:
            labels.append('{}.{}'.format(major, minor))
            if major > 0:
                labels.append('{}'.format(major))
    else:
        labels.append(args.tag)

    if args.latest:
        labels.append('latest')

    # add the label suffixes and image name
    return list(map(lambda x: 'fetchai/constellation:{}{}'.format(x,label_suffix), labels))


def main():
    args = parse_commandline()

    # build the list of docker tags that are to be made from this version
    tags = build_docker_tags(args)
    assert len(tags) >= 1

    # build the first image
    build_docker_image(args.tag, tags[0], args.distro)

    # just create tags from the first one for the remainder of the images
    for tag in tags[1:]:
        tag_docker_image(tags[0], tag)


if __name__ == '__main__':
    main()
