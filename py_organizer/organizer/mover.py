"""Functions for moving files."""
import os
import shutil
from contextlib import suppress

from alive_progress import alive_bar

OTHER_FORMATS = 'other'
FOLDER_TEMPLATES = {  # noqa: WPS407
    '.jpg': 'images',
    '.pdf': 'documents',
    '.mkv': 'videos',
    '.zip': 'archives',
    'other': 'other',
}


def move_all_files_in_dir(source_folder: str) -> None:
    """Move all files in directory.

    Args:
        source_folder: folder where files will be organized.
    """
    list_of_files = os.listdir(source_folder)
    with alive_bar(len(list_of_files)) as move_bar:
        for file_in_dir in list_of_files:
            file_to_move, destination = get_file_and_destination(
                source_folder,
                file_in_dir,
                )
            move_file(file_to_move, destination)
            move_bar()


def get_file_and_destination(source_folder, file_in_dir):
    """Get file path and destination path.

    Args:
        source_folder: folder where files will be organized.
        file_in_dir: file name.

    Returns:
        file_to_move: str
        destination: str
    """
    _, ext = os.path.splitext(file_in_dir)
    file_to_move = os.path.join(source_folder, file_in_dir)
    destination = os.path.join(source_folder, FOLDER_TEMPLATES.get(
        ext, OTHER_FORMATS,
        ),
    )
    return file_to_move, destination


def move_file(file_to_move: str, destination: str) -> None:
    """Move file in chosen destination.

    Args:
        file_to_move: path to file.
        destination: directory for moving files to.
    """
    if os.path.isfile(file_to_move):
        create_dir(destination)
        shutil.move(file_to_move, destination)
        print('File moved {0}'.format(file_to_move))  # noqa: WPS421


def create_dir(destination: str) -> None:
    """Create directory for files.

    Args:
        destination: path where to create directory.
    """
    with suppress(FileExistsError):
        os.mkdir(destination)
