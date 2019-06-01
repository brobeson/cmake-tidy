import argparse
import sys

__version__ = '0.0.0'

def make_parser():
    parser = argparse.ArgumentParser(
        description='Analyze CMake scripts for formatting and style mistakes.',)
    parser.add_argument('--version',
        action='version',
        version=__version__,
        help='Display the version, and exit.')
    parser.add_argument('files',
        default='./CMakeLists.txt',
        nargs='*',
        help='The CMake files to analyze. The default is ./CMakeLists.txt')
    return parser

def main():
    print("Running cmake_lint.main()")
    return 0


if __name__ == '__main__':
    parser = make_parser()
    arguments = parser.parse_args()
    sys.exit()
