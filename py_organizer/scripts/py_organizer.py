"""Main script of py-organizer."""
from py_organizer.cli import cli
from py_organizer.organizer import mover


def main() -> None:
    """Move files script."""
    directory = cli.parse_arguments()
    mover.move_all_files_in_dir(directory)


if __name__ == '__main__':
    main()
