"""
The primary module within the cmake_tidy package.

"""

import argparse

__version__ = "0.0.0"


def _make_parser():
    parser = argparse.ArgumentParser(
        description="Analyze CMake scripts for formatting and style mistakes."
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Display the version, and exit.",
    )
    parser.add_argument(
        "files",
        default="./CMakeLists.txt",
        nargs="*",
        help="The CMake files to analyze. The default is ./CMakeLists.txt",
    )
    return parser


def main():
    """Perform all the work of cleaning up CMake files."""
    print("Running cmake_lint.main()")
    # parser = _make_parser()
    # arguments = parser.parse_args()
    return 0
