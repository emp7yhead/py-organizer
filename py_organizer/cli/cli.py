"""Function to parse arguments in CLI."""
import argparse
import os


def parse_arguments():
    """
    Parse options flags and directory to organize.

    Returns:
        Namespace
    """
    parser = argparse.ArgumentParser(
        prog='py-organizer',
        usage='py-organizer [options] <dir>',
        description='Organizes files in current or chosen directory.',
        add_help=False,
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='py-organizer 0.1.0',
    )
    parser.add_argument(
        '-h',
        '--help',
        action='help',
        help='dispaly help for command',
    )
    parser.add_argument(
        'dir',
        nargs='?',
        const=os.getcwd(),
        default=os.getcwd(),
        help='directory to organize',
        type=str,
    )
    args = parser.parse_args()
    return args.dir
